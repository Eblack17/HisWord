from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from pydantic_ai import Agent
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables!")

client = OpenAI(api_key=api_key)

class ScenarioAnalysisAgent(Agent):
    name: str = "Scenario Analysis Agent"
    model: str = "gpt-3.5-turbo"
    system_prompt: str = """You are an expert at understanding human situations and emotions. For any given scenario, word, or question, provide:
1. Core Situation: Clearly identify what the person is dealing with or asking about
2. Emotional Context: Analyze the underlying emotions, feelings, or state of mind
3. Spiritual Need: Identify the spiritual guidance or comfort they might be seeking

Keep your response concise and focused on these key aspects to help provide relevant biblical guidance."""
    
    def analyze_scenario(self, scenario: str) -> Dict[str, str]:
        try:
            logger.info(f"Analyzing scenario: {scenario}")
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"Analyze this situation: {scenario}"}
            ]
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            analysis = completion.choices[0].message.content
            logger.info(f"Analysis completed successfully")
            return {
                "analysis": analysis
            }
        except Exception as e:
            logger.error(f"Error in analyze_scenario: {str(e)}")
            raise

class BibleVerseAgent(Agent):
    name: str = "Bible Verse Agent"
    model: str = "gpt-3.5-turbo"
    system_prompt: str = """You are a Bible expert who finds the perfect verse for any situation. For the given input, provide:
1. The Single Most Relevant Bible Verse: Choose one verse that best addresses the situation (include exact reference)
2. Why This Verse: In no more than two sentences, explain why this verse perfectly matches their situation
3. Practical Application: In exactly three sentences, provide specific and actionable ways to apply this verse's wisdom to their life

Keep your response structured with these three sections, being concise yet impactful."""
    
    def provide_guidance(self, scenario: str, analysis: str) -> Dict[str, str]:
        try:
            logger.info("Providing biblical guidance")
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"""Based on this scenario: {scenario}
                
And this analysis: {analysis}

Please provide:
1. The Single Most Relevant Bible Verse
2. Why This Verse
3. Practical Application"""}
            ]
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            guidance = completion.choices[0].message.content
            logger.info("Guidance provided successfully")
            return {
                "guidance": guidance
            }
        except Exception as e:
            logger.error(f"Error in provide_guidance: {str(e)}")
            raise

def get_biblical_guidance(scenario: str) -> Dict[str, str]:
    try:
        logger.info("Starting biblical guidance process")
        # Initialize agents
        analyzer = ScenarioAnalysisAgent()
        bible_advisor = BibleVerseAgent()
        
        # First, analyze the scenario
        analysis_result = analyzer.analyze_scenario(scenario)
        
        # Then, get biblical guidance based on the analysis
        guidance_result = bible_advisor.provide_guidance(scenario, analysis_result["analysis"])
        
        logger.info("Biblical guidance process completed successfully")
        return {
            "scenario": scenario,
            "analysis": analysis_result["analysis"],
            "guidance": guidance_result["guidance"]
        }
    except Exception as e:
        logger.error(f"Error in get_biblical_guidance: {str(e)}")
        raise

def main():
    # Example usage
    scenario = "I'm feeling anxious about my future and career decisions. How can I trust God's plan?"
    
    try:
        result = get_biblical_guidance(scenario)
        
        print("\n=== Your Scenario ===")
        print(scenario)
        print("\n=== Scenario Analysis ===")
        print(result["analysis"])
        print("\n=== Biblical Guidance ===")
        print(result["guidance"])
    except Exception as e:
        print(f"Error during example usage: {str(e)}")

if __name__ == "__main__":
    main()
