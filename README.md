# 📚 ScholarChain

<div align="center">

![ScholarChain Logo](https://img.shields.io/badge/ScholarChain-Academic%20Credential%20Verification-blue?style=for-the-badge&logo=blockchain)
![Python](https://img.shields.io/badge/Python-3.7+-green?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-red?style=for-the-badge&logo=flask)
![Blockchain](https://img.shields.io/badge/Blockchain-P2P%20Network-orange?style=for-the-badge&logo=bitcoin)

**A sophisticated Peer-to-Peer blockchain network for academic credential verification**

[🚀 Quick Start](#-quick-start) • [📖 Features](#-features) • [🛠️ Installation](#️-installation) • [📋 Usage](#-usage) • [🔧 API Reference](#-api-reference)

</div>

---

## 🎯 Overview

ScholarChain is a cutting-edge blockchain simulation designed specifically for academic credential verification. It demonstrates core blockchain concepts through a practical, educational application where multiple nodes maintain synchronized copies of academic credentials using Proof-of-Work consensus.

### 🌟 Key Highlights

| Feature | Description |
|---------|-------------|
| 🔐 **Academic Focus** | Specialized for educational credential verification |
| 🌐 **P2P Network** | Multiple nodes with automatic synchronization |
| ⛏️ **Proof-of-Work** | Secure mining with adjustable difficulty |
| 🧠 **Consensus** | Longest chain rule for conflict resolution |
| 🖥️ **Modern UI** | Dark theme with glassmorphism design |
| 📊 **Real-time Stats** | Live network monitoring and analytics |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### 1️⃣ Install Dependencies
```bash
# Clone the repository
git clone <your-repo-url>
cd scholarchain

# Install required packages
pip install -r requirements.txt
```

### 2️⃣ Launch Network Nodes
```bash
# Terminal 1 - Node 1
python app.py -p 5000

# Terminal 2 - Node 2  
python app.py -p 5001

# Terminal 3 - Node 3
python app.py -p 5002
```

### 3️⃣ Access Dashboard
Open your browser and navigate to:
- **Node 1:** http://localhost:5000/dashboard
- **Node 2:** http://localhost:5001/dashboard  
- **Node 3:** http://localhost:5002/dashboard

---

## 📖 Features

### 🔐 Core Blockchain Features
- ✅ **Block Structure** - Immutable blocks with timestamps and hashes
- ✅ **Transaction Management** - Academic credential issuance and validation
- ✅ **Proof-of-Work Mining** - Secure block creation with adjustable difficulty
- ✅ **Chain Validation** - Cryptographic integrity verification
- ✅ **Genesis Block** - Initial block creation and network bootstrap

### 🌐 Network Features
- ✅ **Node Discovery** - Automatic peer registration and discovery
- ✅ **Chain Synchronization** - Real-time blockchain replication across nodes
- ✅ **Consensus Algorithm** - Longest chain rule for conflict resolution
- ✅ **Fault Tolerance** - Graceful handling of node failures
- ✅ **Network Monitoring** - Live peer status and chain length tracking

### 🖥️ User Interface
- ✅ **Modern Dashboard** - Dark theme with glassmorphism design
- ✅ **Real-time Statistics** - Live network metrics and block counts
- ✅ **Interactive Forms** - Easy credential issuance and block mining
- ✅ **Responsive Design** - Works on desktop and mobile devices
- ✅ **Visual Feedback** - Success/error messages and status indicators

---

## 🛠️ Installation

### System Requirements
| Component | Requirement |
|-----------|-------------|
| **Python** | 3.7 or higher |
| **RAM** | 512MB minimum |
| **Storage** | 100MB free space |
| **Network** | Local network access |

### Step-by-Step Setup

#### 1. Environment Setup
```bash
# Create virtual environment (recommended)
python -m venv scholarchain-env

# Activate virtual environment
# Windows:
scholarchain-env\Scripts\activate
# macOS/Linux:
source scholarchain-env/bin/activate
```

#### 2. Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# Verify installation
python -c "import flask, requests; print('✅ Dependencies installed successfully!')"
```

#### 3. Configuration
```bash
# No additional configuration required
# The application uses default settings optimized for development
```

---

## 📋 Usage Guide

### 🎓 Issuing Academic Credentials

#### Via Web Dashboard
1. Navigate to any node's dashboard
2. Fill in the credential form:
   - **Student Name:** Full name of the student
   - **Degree:** Academic degree or certificate
   - **Institution:** Issuing educational institution
3. Click "Issue Credential"

#### Via API
```bash
# PowerShell (Windows)
Invoke-WebRequest -Uri "http://localhost:5000/transactions/new" `
  -Method POST `
  -Body '{"student_name": "John Doe", "degree": "Bachelor of Computer Science", "institution": "MIT"}' `
  -ContentType "application/json"

# cURL (macOS/Linux)
curl -X POST -H "Content-Type: application/json" \
  -d '{"student_name": "John Doe", "degree": "Bachelor of Computer Science", "institution": "MIT"}' \
  http://localhost:5000/transactions/new
```

### ⛏️ Mining Blocks

#### Via Web Dashboard
1. Ensure there are pending credentials
2. Click "Mine New Block"
3. Wait for Proof-of-Work completion
4. View the new block in the blockchain

#### Via API
```bash
# PowerShell
Invoke-WebRequest -Uri "http://localhost:5000/mine"

# cURL
curl http://localhost:5000/mine
```

### 🌐 Network Management

#### Registering Peers
```bash
# Register multiple nodes with Node 1
Invoke-WebRequest -Uri "http://localhost:5000/nodes/register" `
  -Method POST `
  -Body '{"nodes": ["http://localhost:5001", "http://localhost:5002"]}' `
  -ContentType "application/json"
```

#### Synchronizing Chains
```bash
# Trigger consensus and sync
Invoke-WebRequest -Uri "http://localhost:5000/nodes/resolve"
```

### 📊 Monitoring Network

#### View Blockchain
```bash
# Get full blockchain
Invoke-WebRequest -Uri "http://localhost:5000/chain"

# View in browser
http://localhost:5000/chain
```

#### Check Network Status
```bash
# List registered peers
Invoke-WebRequest -Uri "http://localhost:5000/nodes"

# View in dashboard
http://localhost:5000/dashboard
```

---

## 🔧 API Reference

### Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message |
| `GET` | `/dashboard` | Web dashboard |
| `GET` | `/chain` | Full blockchain |
| `POST` | `/transactions/new` | Issue credential |
| `GET` | `/mine` | Mine new block |
| `POST` | `/nodes/register` | Register peers |
| `GET` | `/nodes` | List peers |
| `GET` | `/nodes/resolve` | Trigger consensus |

### Detailed API Documentation

#### 🔗 Get Blockchain
```http
GET /chain
```

**Response:**
```json
{
  "chain": [
    {
      "index": 0,
      "timestamp": 1640995200.0,
      "transactions": [],
      "previous_hash": "0",
      "nonce": 0
    }
  ],
  "length": 1
}
```

#### 📜 Issue Credential
```http
POST /transactions/new
Content-Type: application/json
```

**Request Body:**
```json
{
  "student_name": "John Doe",
  "degree": "Bachelor of Computer Science", 
  "institution": "MIT"
}
```

**Response:**
```json
{
  "message": "Credential will be added to Block 1"
}
```

#### ⛏️ Mine Block
```http
GET /mine
```

**Response:**
```json
{
  "message": "New Block Forged",
  "index": 1,
  "transactions": [...],
  "nonce": 12345,
  "previous_hash": "abc123..."
}
```

#### 🌐 Register Peers
```http
POST /nodes/register
Content-Type: application/json
```

**Request Body:**
```json
{
  "nodes": [
    "http://localhost:5001",
    "http://localhost:5002"
  ]
}
```

---

## 🧪 Testing & Examples

### Sample Workflow

#### 1. Start Network
```bash
# Terminal 1
python app.py -p 5000

# Terminal 2  
python app.py -p 5001

# Terminal 3
python app.py -p 5002
```

#### 2. Register Peers
```bash
# Register all nodes with each other
Invoke-WebRequest -Uri "http://localhost:5000/nodes/register" `
  -Method POST `
  -Body '{"nodes": ["http://localhost:5001", "http://localhost:5002"]}' `
  -ContentType "application/json"
```

#### 3. Issue Credentials
```bash
# Issue multiple credentials
Invoke-WebRequest -Uri "http://localhost:5000/transactions/new" `
  -Method POST `
  -Body '{"student_name": "Alice Johnson", "degree": "Master of Science", "institution": "Stanford"}' `
  -ContentType "application/json"

Invoke-WebRequest -Uri "http://localhost:5001/transactions/new" `
  -Method POST `
  -Body '{"student_name": "Bob Smith", "degree": "PhD", "institution": "Harvard"}' `
  -ContentType "application/json"
```

#### 4. Mine Blocks
```bash
# Mine on different nodes
Invoke-WebRequest -Uri "http://localhost:5000/mine"
Invoke-WebRequest -Uri "http://localhost:5001/mine"
```

#### 5. Sync Network
```bash
# Trigger consensus
Invoke-WebRequest -Uri "http://localhost:5000/nodes/resolve"
```

### Expected Results
- ✅ All nodes show the same blockchain length
- ✅ Credentials are visible across all nodes
- ✅ Network statistics update in real-time
- ✅ Consensus resolves any conflicts automatically

---

## 🚨 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **Port already in use** | Use different ports: `python app.py -p 5003` |
| **PowerShell curl errors** | Use `Invoke-WebRequest` instead of `curl` |
| **Dashboard not loading** | Check if Flask server is running |
| **Peers not showing** | Register peers using `/nodes/register` |
| **404 favicon errors** | Harmless - can be ignored |

### Debug Commands

```bash
# Check if nodes are running
netstat -an | findstr :5000
netstat -an | findstr :5001
netstat -an | findstr :5002

# Test node connectivity
Invoke-WebRequest -Uri "http://localhost:5000/chain"
Invoke-WebRequest -Uri "http://localhost:5001/chain"
Invoke-WebRequest -Uri "http://localhost:5002/chain"
```

### Log Analysis
- Check terminal output for error messages
- Monitor network requests in browser developer tools
- Verify all required dependencies are installed

---

## 📚 Educational Concepts

### Blockchain Fundamentals
- **Blocks:** Immutable data containers with cryptographic links
- **Transactions:** Academic credential records
- **Hashing:** SHA-256 cryptographic fingerprinting
- **Proof-of-Work:** Computational puzzle for block validation
- **Consensus:** Agreement mechanism for network synchronization

### Network Architecture
- **P2P Communication:** Direct node-to-node interaction
- **Node Discovery:** Automatic peer identification
- **Chain Replication:** Synchronized blockchain copies
- **Conflict Resolution:** Longest chain consensus rule
- **Fault Tolerance:** Graceful handling of node failures

---

## 🤝 Contributing

### Development Setup
```bash
# Fork the repository
git clone <your-fork-url>
cd scholarchain

# Create feature branch
git checkout -b feature/new-feature

# Make changes and test
python app.py -p 5000

# Commit and push
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

### Code Style
- Follow PEP 8 Python style guidelines
- Add docstrings to all functions
- Include type hints where appropriate
- Write clear commit messages

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Flask Framework** - Web application framework
- **Blockchain Community** - Educational resources and inspiration
- **Academic Institutions** - Real-world use case inspiration

---

<div align="center">

**Made with ❤️ for blockchain education**

[⬆️ Back to Top](#-scholarchain)

</div> 