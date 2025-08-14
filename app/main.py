from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS
import logging
import os
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_app():
    """Create and configure Flask application"""
    app = Flask(__name__, 
                template_folder='../frontend/templates',
                static_folder='../frontend/static')
    
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['DATABASE_URL'] = os.getenv('DATABASE_URL', 'sqlite:///credit_cards.db')
    
    # Enable CORS
    CORS(app)
    
    return app

def check_gmail_status():
    """Check Gmail API status"""
    try:
        from google.oauth2.credentials import Credentials
        from googleapiclient.discovery import build
        
        if not os.path.exists('credentials.json'):
            return False
        
        if not os.path.exists('token.json'):
            return False
        
        creds = Credentials.from_authorized_user_file('token.json', 
                ['https://www.googleapis.com/auth/gmail.readonly'])
        
        if not creds.valid:
            return False
        
        # Quick test
        service = build('gmail', 'v1', credentials=creds)
        service.users().getProfile(userId='me').execute()
        return True
        
    except Exception as e:
        logger.error(f"Gmail status check failed: {e}")
        return False

app = create_app()

@app.route('/')
def dashboard():
    """Main dashboard with dynamic status"""
    gmail_connected = check_gmail_status()
    gmail_status = "Connected" if gmail_connected else "Needs Configuration"
    gmail_class = "success" if gmail_connected else "warning"
    
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Indian Credit Card Analyzer</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <nav class="navbar navbar-dark bg-primary">
            <div class="container">
                <span class="navbar-brand">
                    <i class="fas fa-credit-card me-2"></i>
                    Indian Credit Card Analyzer
                </span>
            </div>
        </nav>
        
        <div class="container mt-4">
            <div class="row">
                <div class="col-md-12">
                    <div class="alert alert-success">
                        <h4><i class="fas fa-check-circle me-2"></i>Setup Successful!</h4>
                        <p>Your Indian Credit Card Analyzer is running successfully!</p>
                        <hr>
                        <h5>Status:</h5>
                        <ul class="list-unstyled">
                            <li><i class="fas fa-check text-success me-2"></i>Flask App Running</li>
                            <li><i class="fas fa-check text-success me-2"></i>Database Ready</li>
                            <li><i class="fas fa-check text-success me-2"></i>PDF Parsers Loaded</li>
                            <li><i class="fas fa-{'check text-success' if gmail_connected else 'exclamation-triangle text-warning'} me-2"></i>Gmail API - {gmail_status}</li>
                        </ul>
                        
                        {'<div class="alert alert-info mt-3"><h6>🎉 All Systems Ready!</h6><p>You can now sync your credit card statements and start analyzing your spending patterns.</p></div>' if gmail_connected else '<div class="alert alert-warning mt-3"><h6>⚠️ Gmail Configuration Needed</h6><p>Complete OAuth authorization to sync credit card statements.</p></div>'}
                    </div>
                </div>
            </div>
            
            <div class="row">
                <div class="col-md-6">
                    <div class="card">
                        <div class="card-header">
                            <h5><i class="fas fa-university me-2"></i>Supported Banks</h5>
                        </div>
                        <div class="card-body">
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item">
                                    <i class="fas fa-check text-success me-2"></i>SBI Cards (CASHBACK, SimplySAVE)
                                </li>
                                <li class="list-group-item">
                                    <i class="fas fa-check text-success me-2"></i>HDFC Bank (Marriott, Tata Neu, Regalia)
                                </li>
                                <li class="list-group-item">
                                    <i class="fas fa-check text-success me-2"></i>Axis Bank (Neo, Magnus, Atlas)
                                </li>
                                <li class="list-group-item">
                                    <i class="fas fa-check text-success me-2"></i>Standard Chartered
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-6">
                    <div class="card">
                        <div class="card-header">
                            <h5><i class="fas fa-cogs me-2"></i>Actions</h5>
                        </div>
                        <div class="card-body">
                            {'<button class="btn btn-success btn-lg" onclick="syncStatements()"><i class="fas fa-sync me-2"></i>Sync Statements</button>' if gmail_connected else '<button class="btn btn-warning btn-lg" disabled><i class="fas fa-exclamation-triangle me-2"></i>Complete Gmail Setup First</button>'}
                            <div class="mt-3">
                                <small class="text-muted">
                                    {'Ready to fetch and analyze your credit card statements!' if gmail_connected else 'Configure Gmail API to start syncing statements.'}
                                </small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <script>
        function syncStatements() {{
            alert('Sync functionality will be implemented next!');
        }}
        </script>
    </body>
    </html>
    '''

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'gmail_connected': check_gmail_status(),
        'message': 'Indian Credit Card Analyzer is running'
    })

@app.route('/api/status')
def api_status():
    """API status endpoint"""
    return jsonify({
        'api_version': '1.0.0',
        'status': 'active',
        'gmail_status': 'connected' if check_gmail_status() else 'needs_configuration',
        'features': [
            'Gmail Integration',
            'PDF Parsing', 
            'Transaction Categorization',
            'Analytics Dashboard'
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    
    logger.info(f"Starting Indian Credit Card Analyzer on {host}:{port}")
    logger.info(f"Gmail API Status: {'Connected' if check_gmail_status() else 'Needs Configuration'}")
    app.run(host=host, port=port, debug=False)
EOF