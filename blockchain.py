import hashlib
import json
import time
from typing import List, Set, Optional
from urllib.parse import urlparse

class Transaction:
    """
    Represents an academic certificate transaction in the blockchain.
    """
    def __init__(self, student_name: str, degree: str, institution: str):
        self.student_name = student_name
        self.degree = degree
        self.institution = institution

    def to_dict(self):
        return self.__dict__

class Block:
    """
    Represents a block in the blockchain.
    """
    def __init__(self, index: int, timestamp: float, transactions: List[Transaction], previous_hash: str, nonce: int = 0):
        self.index = index
        self.timestamp = timestamp
        self.transactions = [tx.to_dict() for tx in transactions]
        self.previous_hash = previous_hash
        self.nonce = nonce

    def to_dict(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }

    def compute_hash(self):
        block_string = json.dumps(self.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    """
    Blockchain data structure with PoW and consensus for academic certificates.
    """
    def __init__(self, difficulty: int = 4):
        self.chain: List[Block] = []
        self.current_transactions: List[Transaction] = []
        self.nodes: Set[str] = set()
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), [], '0')
        self.chain.append(genesis_block)

    def register_node(self, address: str):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc or parsed_url.path)

    def new_transaction(self, student_name: str, degree: str, institution: str) -> int:
        # Transaction validation
        if not student_name or not degree or not institution:
            return False
        tx = Transaction(student_name, degree, institution)
        self.current_transactions.append(tx)
        return self.last_block.index + 1

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def proof_of_work(self, block: Block) -> str:
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block: Block, proof: str) -> bool:
        previous_hash = self.last_block.compute_hash()
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        self.chain.append(block)
        return True

    def is_valid_proof(self, block: Block, block_hash: str) -> bool:
        return (block_hash.startswith('0' * self.difficulty) and block_hash == block.compute_hash())

    def mine(self, miner_address: str) -> Optional[Block]:
        if not self.current_transactions:
            return None
        # Add a certificate reward for mining
        self.new_transaction("System", "Mining Reward Certificate", miner_address)
        block = Block(
            index=self.last_block.index + 1,
            timestamp=time.time(),
            transactions=self.current_transactions,
            previous_hash=self.last_block.compute_hash()
        )
        proof = self.proof_of_work(block)
        self.add_block(block, proof)
        self.current_transactions = []
        return block

    def is_chain_valid(self, chain: List[Block]) -> bool:
        previous_block = chain[0]
        for block in chain[1:]:
            if block.previous_hash != previous_block.compute_hash():
                return False
            if not self.is_valid_proof(block, block.compute_hash()):
                return False
            previous_block = block
        return True

    def replace_chain(self, new_chain: List[Block]) -> bool:
        if len(new_chain) > len(self.chain) and self.is_chain_valid(new_chain):
            self.chain = new_chain
            return True
        return False 