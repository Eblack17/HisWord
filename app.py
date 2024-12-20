from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_agents import get_biblical_guidance
import os
import logging
import sys

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    logger.info("Home endpoint accessed")
    return jsonify({
        "status": "online",
        "message": "His Word API is running",
        "endpoints": {
            "/": "API documentation",
            "/guidance": "POST - Get biblical guidance for your situation"
        },
        "example": {
            "request": {
                "method": "POST",
                "endpoint": "/guidance",
                "body": {
                    "question": "How can I find peace in difficult times?"
                }
            }
        }
    })

@app.route('/guidance', methods=['POST'])
def guidance():
    try:
        logger.info("Guidance endpoint accessed")
        data = request.get_json()
        if not data:
            logger.warning("No JSON data in request")
            return jsonify({'error': 'Request must include JSON data'}), 400
            
        if 'question' not in data:
            logger.warning("No question field in request data")
            return jsonify({'error': 'Please provide a question in the request body'}), 400
        
        question = data['question']
        if not question.strip():
            logger.warning("Empty question provided")
            return jsonify({'error': 'Question cannot be empty'}), 400
        
        logger.info(f"Processing question: {question[:50]}...")
        result = get_biblical_guidance(question)
        logger.info("Successfully generated guidance")
        
        return jsonify({
            'success': True,
            'data': result
        })
    
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}", exc_info=True)
        return jsonify({
            'success': False,
            'error': 'An internal server error occurred. Please try again later.'
        }), 500

@app.errorhandler(404)
def not_found(e):
    logger.warning(f"404 error: {request.url}")
    return jsonify({
        'success': False,
        'error': 'The requested endpoint does not exist'
    }), 404

@app.errorhandler(405)
def method_not_allowed(e):
    logger.warning(f"405 error: {request.method} {request.url}")
    return jsonify({
        'success': False,
        'error': 'The method is not allowed for this endpoint'
    }), 405

@app.errorhandler(500)
def server_error(e):
    logger.error(f"500 error: {str(e)}", exc_info=True)
    return jsonify({
        'success': False,
        'error': 'An internal server error occurred. Please try again later.'
    }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    logger.info(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port)
