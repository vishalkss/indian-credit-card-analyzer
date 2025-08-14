# 🏦 Indian Credit Card Analyzer

A comprehensive self-hosted solution for analyzing credit card statements from major Indian banks.

## ✨ Features

- **Gmail Integration**: Automatically fetches credit card statements
- **Multi-Bank Support**: SBI, HDFC, Axis, Standard Chartered, and more
- **PDF Parsing**: Intelligently extracts transaction data
- **Smart Analytics**: Spending patterns, categorization, insights
- **Privacy First**: All data stays on your server

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Gmail Account with API access
- Raspberry Pi 4 (recommended) or any Linux/macOS/Windows system

### Installation

1. **Extract and setup**:
```bash
# Extract the project
unzip indian-credit-card-analyzer.zip
cd indian-credit-card-analyzer

# Run setup script
chmod +x setup.sh
./setup.sh
```

2. **Configure Gmail API**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create project → Enable Gmail API
   - Create OAuth 2.0 credentials (Desktop Application)
   - Download `credentials.json` to project folder

3. **Configure Environment**:
```bash
# Edit .env file with your details
nano .env

# Update these values:
GMAIL_CLIENT_ID=your_client_id_here
GMAIL_CLIENT_SECRET=your_client_secret_here
GMAIL_USER_EMAIL=your_email@gmail.com
USER_FIRST_NAME_4_CHARS=VISH  # First 4 chars of your name
USER_DOB_DDMM=1411            # Your DOB in DDMM format
```

4. **Start Application**:
```bash
# Direct start
./start.sh

# Or using Docker
docker-compose up -d
```

5. **Access Dashboard**:
Open browser: `http://localhost:5000`

## 🏦 Supported Banks

| Bank | Status | Cards |
|------|--------|-------|
| SBI Cards | ✅ Ready | CASHBACK, SimplySAVE, Prime |
| HDFC Bank | ✅ Ready | Marriott, Tata Neu, Regalia |
| Axis Bank | ✅ Ready | Neo, Magnus, Atlas |
| Standard Chartered | ✅ Ready | Ultimate, Manhattan |

## 📊 Features

### Dashboard
- Overview of all credit cards
- Monthly spending trends
- Category-wise spending analysis
- Payment due alerts

### Analytics
- Spending patterns by category
- Top merchants analysis
- Cashback optimization
- Recurring transaction detection

### Automation
- Auto-sync statements from Gmail
- PDF password handling
- Smart transaction categorization
- Payment reminders

## 🛠️ Troubleshooting

### Gmail Authentication
```bash
# Delete token and re-authenticate
rm token.json
source venv/bin/activate
python -c "from app.gmail_client import GmailClient; GmailClient().authenticate()"
```

### PDF Password Issues
- Verify `USER_FIRST_NAME_4_CHARS` matches your credit card name
- Check `USER_DOB_DDMM` format (14th Nov = 1411)
- Try `USER_DOB_DDMMYY` if DDMM doesn't work

### Port Conflicts
```bash
# Change port in .env
PORT=5001

# Or kill existing process
sudo lsof -ti:5000 | xargs kill -9
```

## 🔐 Security

- ✅ Self-hosted - your data stays local
- ✅ Encrypted PDF handling
- ✅ OAuth-based Gmail access
- ✅ No third-party data sharing

## 📝 License

MIT License - Feel free to use and modify!

## 🤝 Support

For issues and questions:
- Check this README
- Review the setup script output
- Ensure all prerequisites are installed

---

**Made with ❤️ for Indian credit card users**
