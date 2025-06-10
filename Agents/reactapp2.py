from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_react_agent(
    model="gpt-4o",
    tools=[get_weather],
    prompt="You are a helpful assistant"
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "Give me the wather in bay area"}]}
)
print(result["messages"][-1].content)