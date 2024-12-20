from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_agents import get_biblical_guidance
from dotenv import load_dotenv
import os
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/health')
def health():
    """Health check endpoint"""
    logger.info("Health check endpoint accessed")
    return jsonify({"status": "healthy", "message": "API is running"}), 200

@app.route('/')
def home():
    logger.info("Home endpoint accessed")
    return """
    <html>
        <head>
            <title>His Word API</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    margin: 40px; 
                    line-height: 1.6;
                    color: #333;
                }
                h1 { color: #2c3e50; }
                pre { 
                    background: #f8f9fa; 
                    padding: 15px; 
                    border-radius: 5px;
                    border: 1px solid #e9ecef;
                }
                .status {
                    background: #d4edda;
                    color: #155724;
                    padding: 10px;
                    border-radius: 5px;
                    margin: 20px 0;
                }
            </style>
        </head>
        <body>
            <h1>His Word API</h1>
            <div class="status">Status: API is running!</div>
            <p>Use this API to get biblical guidance for any situation.</p>
            <h2>API Endpoints:</h2>
            <h3>1. Health Check</h3>
            <pre>
GET /health
            </pre>
            <h3>2. Get Biblical Guidance</h3>
            <pre>
POST /guidance
Content-Type: application/json

{
    "question": "Your situation or question here"
}
            </pre>
            <p>Example response:</p>
            <pre>
{
    "success": true,
    "guidance": {
        "verse": "Bible verse here",
        "explanation": "Why this verse is relevant",
        "application": "How to apply it"
    }
}
            </pre>
        </body>
    </html>
    """

@app.route('/guidance', methods=['POST'])
def guidance():
    logger.info("Guidance endpoint accessed")
    try:
        data = request.get_json()
        logger.info(f"Received data: {data}")
        
        if not data or 'question' not in data:
            logger.error("No question provided in request")
            return jsonify({'error': 'Please provide a question in the request body'}), 400
        
        question = data['question']
        if not question.strip():
            logger.error("Empty question provided")
            return jsonify({'error': 'Question cannot be empty'}), 400
        
        # Get guidance
        logger.info(f"Getting guidance for question: {question}")
        result = get_biblical_guidance(question)
        logger.info("Guidance received successfully")
        
        return jsonify({
            'success': True,
            'guidance': result['guidance']
        })
    
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.errorhandler(404)
def not_found(e):
    logger.error(f"404 error: {request.url}")
    return jsonify({"error": "The requested resource was not found"}), 404

@app.errorhandler(500)
def server_error(e):
    logger.error(f"500 error: {str(e)}")
    return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    logger.info(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port)
