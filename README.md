# HisWord - Bible Verse API

An AI-powered API that provides relevant biblical guidance based on user situations or questions. This API uses advanced language models to analyze input and find the most appropriate Bible verse along with practical applications.

## Features

- Intelligent analysis of user situations and questions
- Returns relevant Bible verses with context
- Provides explanations of verse relevance
- Offers practical application steps
- Simple and easy-to-use API

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Eblack17/HisWord.git
cd HisWord
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

The API provides a simple interface to get biblical guidance. Here's a basic example:

```python
from ai_agents import get_biblical_guidance

# Get guidance for a situation
scenario = "I'm feeling anxious about my future"
result = get_biblical_guidance(scenario)

# The result contains:
# - scenario: The original input
# - analysis: AI's analysis of the situation (optional)
# - guidance: Bible verse, explanation, and application

# Print the guidance
print(result["guidance"])
```

See `example.py` for more usage examples.

### Response Format

The API returns a dictionary with the following structure:

```python
{
    "scenario": "The original input text",
    "analysis": "AI's analysis of the situation and context",
    "guidance": "1. Bible verse with reference\n2. Explanation of relevance\n3. Practical application steps"
}
```

## Dependencies

- Python 3.8+
- openai
- python-dotenv
- pydantic

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
