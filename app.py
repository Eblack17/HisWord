from flask import Flask, request, jsonify
from ai_agents import get_biblical_guidance
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "His Word API is running"
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
    app.run()
