import requests
import json

def test_api(url, question):
    """Test the His Word API with a question."""
    try:
        # Make the API request
        response = requests.post(
            f"{url}/guidance",
            json={"question": question},
            headers={"Content-Type": "application/json"}
        )
        
        # Print the response status
        print(f"Status Code: {response.status_code}")
        
        # Pretty print the response
        print("\nResponse:")
        print(json.dumps(response.json(), indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Replace with your Railway URL
    API_URL = "https://hisword-production.up.railway.app"
    
    # Test questions
    questions = [
        "How can I find peace in difficult times?",
        "What does the Bible say about love?",
        "How to deal with anxiety?"
    ]
    
    print("Testing His Word API...")
    print("-" * 50)
    
    for question in questions:
        print(f"\nTesting question: {question}")
        print("-" * 50)
        test_api(API_URL, question)
        print("-" * 50)
