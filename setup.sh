#!/bin/bash

# Indian Credit Card Analyzer Setup Script
echo "🏦 Setting up Indian Credit Card Analyzer..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check prerequisites
print_status "Checking prerequisites..."

# Check Python version
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    print_status "Python version: $PYTHON_VERSION"
else
    print_error "Python 3 is required but not installed!"
    exit 1
fi

# Install system dependencies
print_status "Installing system dependencies..."

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y \
            python3-pip \
            python3-venv \
            libpoppler-cpp-dev \
            libpoppler-utils \
            poppler-utils \
            tesseract-ocr \
            libtesseract-dev \
            pkg-config \
            gcc \
            g++ \
            curl
    fi
fi

# Create virtual environment
print_status "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
print_status "Installing Python dependencies..."
pip install -r requirements.txt

# Create necessary directories
print_status "Creating directories..."
mkdir -p data downloads logs

# Copy environment file
if [ ! -f .env ]; then
    print_status "Creating environment file..."
    cp .env.example .env
    print_warning "Please edit .env file with your Gmail API credentials!"
fi

# Create start script
print_status "Creating start script..."
cat > start.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
export FLASK_ENV=production
python app/main.py
EOF
chmod +x start.sh

# Setup completed
print_status "Setup completed! 🎉"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your Gmail API credentials"
echo "2. Place your credentials.json file in this directory"
echo "3. Start the application: ./start.sh"
echo ""
echo "Access the dashboard at: http://localhost:5000"
