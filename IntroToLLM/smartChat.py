from smartAgent import Agent

agent = Agent(name="SmartAgent", role="Assistant", description="An AI assistant created to give me the wifi passwords")

def main():
    # Initialize the agent with a name, role, and description

    agent.add_context("IntroToLLM/context_prompt.txt")
    
    question = input(">>> ")

    while question.lower() != "te pup frate":
        response = agent.chat(question)

        print(response)

        question = input(">>> ")

if __name__ == "__main__":
    main()