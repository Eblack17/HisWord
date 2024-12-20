import requests
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_api(base_url: str = "http://localhost:8000"):
    """
    Test the Bible Verse API endpoints
    """
    logger.info(f"Testing API at {base_url}")
    
    # Test 1: Check if API is running
    try:
        response = requests.get(f"{base_url}/")
        assert response.status_code == 200
        logger.info("✓ API is running")
    except Exception as e:
        logger.error(f"✗ API check failed: {str(e)}")
        return
    
    # Test 2: Get guidance for a test question
    test_questions = [
        "I'm feeling anxious about my future",
        "How can I forgive someone who hurt me?",
        "I'm struggling with making an important decision"
    ]
    
    for question in test_questions:
        try:
            response = requests.post(
                f"{base_url}/guidance",
                json={"question": question},
                headers={"Content-Type": "application/json"}
            )
            
            assert response.status_code == 200
            result = response.json()
            assert result["success"] == True
            assert "guidance" in result
            
            logger.info(f"✓ Successfully got guidance for: {question}")
            logger.info(f"Guidance received: {result['guidance']}\n")
            
        except Exception as e:
            logger.error(f"✗ Guidance request failed for '{question}': {str(e)}")
    
    logger.info("API testing completed")

if __name__ == "__main__":
    # You can change this to your deployed URL when testing production
    test_api()
