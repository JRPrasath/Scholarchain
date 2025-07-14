from flask import Flask, jsonify, request, render_template, redirect, url_for
from uuid import uuid4
import requests
from blockchain import Blockchain, Block, Transaction

app = Flask(__name__)

# Unique identifier for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/')
def index():
    return "📚 ScholarChain - Academic Credential Verification Network is running. See the README for API usage.", 200

@app.route('/chain', methods=['GET'])
def full_chain():
    """Return the full blockchain."""
    chain_data = [block for block in blockchain.chain]
    return jsonify({
        'chain': [block.__dict__ for block in blockchain.chain],
        'length': len(blockchain.chain)
    }), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Add a new academic certificate transaction to the blockchain."""
    values = request.get_json()
    required = ['student_name', 'degree', 'institution']
    if not all(k in values for k in required):
        return 'Missing values', 400
    result = blockchain.new_transaction(values['student_name'], values['degree'], values['institution'])
    if not result:
        return jsonify({'message': 'Invalid certificate. Check student name, degree, and institution.'}), 400
    response = {'message': f'Certificate will be added to Block {result}'}
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    """Mine a new block and broadcast to peers."""
    block = blockchain.mine(node_identifier)
    if not block:
        return jsonify({'message': 'No certificates to mine'}), 400
    response = {
        'message': 'New Block Forged',
        'index': block.index,
        'transactions': block.transactions,
        'nonce': block.nonce,
        'previous_hash': block.previous_hash
    }
    # Broadcast new block to peers (optional, for bonus)
    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    """Register new nodes in the network."""
    values = request.get_json()
    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400
    for node in nodes:
        blockchain.register_node(node)
    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    """Consensus algorithm: resolve conflicts by replacing chain with the longest one in the network."""
    replaced = resolve_conflicts()
    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': [block.__dict__ for block in blockchain.chain]
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': [block.__dict__ for block in blockchain.chain]
        }
    return jsonify(response), 200

@app.route('/nodes', methods=['GET'])
def list_nodes():
    """List all known peer nodes."""
    return jsonify({'nodes': list(blockchain.nodes)}), 200

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    import requests
    message = None
    error = None
    if request.method == 'POST':
        if 'mine' in request.form:
            block = blockchain.mine(node_identifier)
            if block:
                message = f"Block {block.index} mined!"
            else:
                error = "No certificates to mine."
        elif 'add_transaction' in request.form:
            student_name = request.form.get('student_name')
            degree = request.form.get('degree')
            institution = request.form.get('institution')
            if student_name and degree and institution:
                result = blockchain.new_transaction(student_name, degree, institution)
                if not result:
                    error = "Invalid certificate. All fields are required."
                else:
                    message = "Certificate added!"
            else:
                error = "All fields are required."
    chain = blockchain.chain
    peers = list(blockchain.nodes)
    # Fetch peer chain lengths
    peer_chains = []
    for peer in peers:
        try:
            r = requests.get(f"http://{peer}/chain", timeout=2)
            if r.status_code == 200:
                data = r.json()
                peer_chains.append({'peer': peer, 'length': data['length']})
            else:
                peer_chains.append({'peer': peer, 'length': 'Unavailable'})
        except Exception:
            peer_chains.append({'peer': peer, 'length': 'Unavailable'})
    return render_template('dashboard.html', chain=chain, peers=peers, message=message, error=error, peer_chains=peer_chains)

@app.route('/favicon.ico')
def favicon():
    return '', 204

def resolve_conflicts():
    """Consensus algorithm: Longest valid chain wins."""
    neighbours = blockchain.nodes
    new_chain = None
    max_length = len(blockchain.chain)
    for node in neighbours:
        try:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain_data = response.json()['chain']
                chain = []
                for block_data in chain_data:
                    block = Block(
                        index=block_data['index'],
                        timestamp=block_data['timestamp'],
                        transactions=[Transaction(**tx) for tx in block_data['transactions']],
                        previous_hash=block_data['previous_hash'],
                        nonce=block_data['nonce']
                    )
                    chain.append(block)
                if length > max_length and blockchain.is_chain_valid(chain):
                    max_length = length
                    new_chain = chain
        except Exception as e:
            continue
    if new_chain:
        blockchain.chain = new_chain
        return True
    return False

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port) 