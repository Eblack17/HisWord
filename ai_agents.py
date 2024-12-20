import os
from openai import OpenAI
from pydantic import BaseModel
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class BibleVerseAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def provide_guidance(self, question: str) -> Dict[str, Any]:
        """
        Provide biblical guidance based on the user's question.
        
        Args:
            question (str): The user's question or situation
            
        Returns:
            Dict[str, Any]: Dictionary containing the guidance
        """
        try:
            # Create the prompt for the API
            prompt = f"""Given this situation or question: "{question}"
            Please provide relevant biblical guidance. Focus on providing:
            1. A specific, relevant Bible verse
            2. A brief explanation of how this verse relates to the situation
            3. Practical advice on how to apply this wisdom

            Format the response as a concise, direct message."""

            # Get completion from OpenAI
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a knowledgeable biblical advisor."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Extract the response
            guidance = completion.choices[0].message.content

            return {"guidance": guidance}
            
        except Exception as e:
            raise Exception(f"Error getting biblical guidance: {str(e)}")

def get_biblical_guidance(question: str) -> Dict[str, Any]:
    """
    Helper function to get biblical guidance.
    
    Args:
        question (str): The user's question
        
    Returns:
        Dict[str, Any]: Dictionary containing the guidance
    """
    agent = BibleVerseAgent()
    return agent.provide_guidance(question)
