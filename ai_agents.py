import os
from openai import OpenAI
from pydantic import BaseModel
from typing import Dict, Any
from dotenv import load_dotenv
from pydantic_ai import Agent

# Load environment variables
load_dotenv()

class BibleVerseAgent(Agent):
    name: str = "Bible Verse Agent"
    model: str = "gpt-3.5-turbo"
    system_prompt: str = """You are a knowledgeable biblical advisor. For any given question or situation, provide:
1. A specific, relevant Bible verse (with exact reference)
2. A brief explanation of how this verse relates to the situation
3. Practical advice on how to apply this wisdom

Keep your response concise and focused on these key aspects."""

    def __init__(self):
        super().__init__()
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
            # Create the messages for the API
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"Please provide biblical guidance for this situation: {question}"}
            ]

            # Get completion from OpenAI
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages
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
