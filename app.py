from flask import Flask, request, jsonify
from ai_agents import get_biblical_guidance
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>His Word API</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                h1 { color: #333; }
                pre { background: #f4f4f4; padding: 15px; border-radius: 5px; }
            </style>
        </head>
        <body>
            <h1>His Word API</h1>
            <p>Use this API to get biblical guidance for any situation.</p>
            <h2>API Usage:</h2>
            <pre>
POST /guidance
Content-Type: application/json

{
    "question": "Your situation or question here"
}
            </pre>
        </body>
    </html>
    """

@app.route('/guidance', methods=['POST'])
def guidance():
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'Please provide a question in the request body'}), 400
        
        question = data['question']
        if not question.strip():
            return jsonify({'error': 'Question cannot be empty'}), 400
        
        # Get guidance
        result = get_biblical_guidance(question)
        
        return jsonify({
            'success': True,
            'guidance': result['guidance']
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
