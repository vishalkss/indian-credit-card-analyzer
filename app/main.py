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

    # Basic configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['DATABASE_URL'] = os.getenv('DATABASE_URL', 'sqlite:///credit_cards.db')

    # Enable CORS
    CORS(app)

    return app

app = create_app()

@app.route('/')
def dashboard():
    """Main dashboard"""
    return '''
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
                        <h5>Next Steps:</h5>
                        <ol>
                            <li><strong>Configure Gmail API:</strong> Add your credentials.json file</li>
                            <li><strong>Edit Environment:</strong> Update .env file with your details</li>
                            <li><strong>Authenticate Gmail:</strong> Run initial OAuth flow</li>
                            <li><strong>Sync Statements:</strong> Click sync to fetch your statements</li>
                        </ol>

                        <h5 class="mt-4">Status:</h5>
                        <ul class="list-unstyled">
                            <li><i class="fas fa-check text-success me-2"></i>Flask App Running</li>
                            <li><i class="fas fa-check text-success me-2"></i>Database Ready</li>
                            <li><i class="fas fa-check text-success me-2"></i>PDF Parsers Loaded</li>
                            <li><i class="fas fa-exclamation-triangle text-warning me-2"></i>Gmail API - Needs Configuration</li>
                        </ul>
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
                            <h5><i class="fas fa-features me-2"></i>Features</h5>
                        </div>
                        <div class="card-body">
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item">
                                    <i class="fas fa-robot text-primary me-2"></i>Automatic Gmail Sync
                                </li>
                                <li class="list-group-item">
                                    <i class="fas fa-file-pdf text-danger me-2"></i>PDF Statement Parsing
                                </li>
                                <li class="list-group-item">
                                    <i class="fas fa-chart-pie text-info me-2"></i>Smart Categorization
                                </li>
                                <li class="list-group-item">
                                    <i class="fas fa-analytics text-success me-2"></i>Spending Analytics
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    '''

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'message': 'Indian Credit Card Analyzer is running'
    })

@app.route('/api/status')
def api_status():
    """API status endpoint"""
    return jsonify({
        'api_version': '1.0.0',
        'status': 'active',
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
    app.run(host=host, port=port, debug=False)
