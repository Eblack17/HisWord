from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_agents import get_biblical_guidance
from dotenv import load_dotenv
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "His Word API is running",
        "endpoints": {
            "/": "API documentation",
            "/guidance": "POST - Get biblical guidance for your question"
        }
    })

@app.route('/guidance', methods=['POST'])
def guidance():
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'Please provide a question in the request body'}), 400
        
        question = data['question']
        if not question.strip():
            return jsonify({'error': 'Question cannot be empty'}), 400
        
        logger.info(f"Processing question: {question}")
        result = get_biblical_guidance(question)
        
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
    return jsonify({"error": "The requested resource was not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
