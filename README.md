# Bible Verse Finder

A Python application that provides relevant biblical guidance based on your situation or question. This app uses AI to analyze your input and find the most appropriate Bible verse along with practical applications.

## Features

- Intelligent analysis of user situations and questions
- Provides relevant Bible verses with context
- Explains why the verse is relevant
- Offers practical application steps
- Modern, user-friendly GUI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bible-verse-finder.git
cd bible-verse-finder
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

1. Run the application:
```bash
# On Windows:
run_app.bat
# On Unix or MacOS:
python bible_app_gui.py
```

2. Enter your situation, question, or topic in the text box
3. Click "Get Guidance"
4. The app will provide:
   - A relevant Bible verse
   - An explanation of its relevance
   - Practical application steps

## Dependencies

- Python 3.8+
- customtkinter
- openai
- python-dotenv
- pydantic
- pydantic-ai

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
