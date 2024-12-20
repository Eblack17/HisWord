# His Word API

A RESTful API that provides biblical guidance and wisdom for any life situation. Using AI-powered analysis, it finds relevant Bible verses and practical applications for your specific circumstances.

## Features

- Scenario Analysis: Understands the context and emotional aspects of your situation
- Biblical Guidance: Provides relevant Bible verses with explanations
- Practical Application: Offers actionable ways to apply biblical wisdom

## API Endpoints

### GET /
Returns API status and documentation

### POST /guidance
Get biblical guidance for your situation

**Request Body:**
```json
{
    "question": "Your situation or question here"
}
```

**Response:**
```json
{
    "success": true,
    "data": {
        "scenario": "Your input question",
        "analysis": "Analysis of your situation",
        "guidance": "Bible verse and practical application"
    }
}
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/HisWord.git
cd HisWord
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

5. Run the application:
```bash
python app.py
```

## Usage

Send a POST request to the /guidance endpoint:

```bash
curl -X POST http://localhost:8000/guidance \
  -H "Content-Type: application/json" \
  -d '{"question":"How can I find peace in difficult times?"}'
```

## Dependencies

- Flask: Web framework
- OpenAI: AI model for analysis
- Pydantic: Data validation
- Python-dotenv: Environment variable management

## License

This project is licensed under the MIT License - see the LICENSE file for details.
