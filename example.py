from ai_agents import get_biblical_guidance

def main():
    # Example scenarios
    scenarios = [
        "I'm feeling anxious about my future",
        "How can I forgive someone who hurt me?",
        "I need guidance about a difficult decision",
    ]
    
    print("Bible Verse Finder API Example\n")
    
    for scenario in scenarios:
        try:
            print(f"\n=== Scenario: {scenario} ===")
            result = get_biblical_guidance(scenario)
            
            # Print the guidance
            print("\nGuidance:")
            print(result["guidance"])
            print("\n" + "="*50)
            
        except Exception as e:
            print(f"Error processing scenario '{scenario}': {str(e)}")

if __name__ == "__main__":
    main()
