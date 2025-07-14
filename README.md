# 🎓 ScholarChain: Academic Credential Blockchain Network

ScholarChain is a peer-to-peer blockchain network built with Flask and Python, designed for secure academic credential verification. Each node maintains its own blockchain, can issue academic credentials, mine new blocks using Proof-of-Work, connect to peer nodes, and synchronize with the network—all through a modern, user-friendly dashboard.

---

## 🚀 Features
- Issue and view academic credentials (student name, degree, institution)
- Mine new blocks (Proof-of-Work) to add credentials to the blockchain
- Connect to peer nodes for a decentralized network
- Sync your blockchain with the longest valid chain (consensus)
- View all connected peers and the current blockchain in real time
- Modern dark-themed dashboard for easy interaction

---

## ⚙️ How It Works

### Issuing Credentials
- Users submit academic credentials (student name, degree, institution) via the dashboard.
- Credentials are stored as pending transactions until mined.

### Mining (Proof-of-Work)
- When you click "Mine Block", the node solves a computational puzzle.
- Once solved, a new block is created containing the pending credentials.
- The block is added to the chain and credentials are cleared from the pending list.

### Chain Syncing (Consensus)
- Nodes may fall out of sync. The "Sync Chain" feature checks all peers.
- If a peer has a longer, valid chain, the node replaces its own chain (Longest Chain Rule).

---

## 📁 Project Structure

```
scholar_chain/
├── app.py / node1.py      # Flask app (one per node)
├── templates/
│   └── index.html         # Dashboard UI
├── static/
│   └── style.css          # Dark theme styling
├── README.md
```

---

## ▶️ Setup & Run

Install dependencies:
```bash
pip install flask requests
```

Start node 1:
```bash
python node1.py  # Runs on port 5000
```

Start node 2:
```bash
python node2.py  # Runs on port 5001
```

Open your browser at:
- http://localhost:5000/
- http://localhost:5001/

---

## 🖥️ UI Preview

Modern dashboard with panels to:
- Issue academic credentials
- Connect peers
- Mine blocks
- View connected nodes and blockchain

**Screenshots:**

![Image](path/to/image.png)

![Image2](path/to/image2.png)


---

## 📡 API Endpoints

| Method | Endpoint             | Description                                 |
|--------|----------------------|---------------------------------------------|
| GET    | /                    | UI dashboard for each node                  |
| GET    | /chain               | Returns full blockchain                     |
| POST   | /transactions/new    | Adds a new academic credential              |
| GET    | /mine                | Mines a new block (Proof-of-Work)           |
| POST   | /nodes/register      | Registers a peer node                       |
| GET    | /nodes/resolve       | Consensus: replaces with longer valid chain |
| GET    | /nodes               | Lists connected peer nodes                  |

---

**Made with ❤️ for academic credential verification and blockchain education.** 