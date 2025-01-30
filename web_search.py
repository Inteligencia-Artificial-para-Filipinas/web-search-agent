from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

web_search_agent = Agent(
    name="Web Search Agent",
    model=OpenAIChat(id="gpt-3.5-turbo"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    description="Search the web for information",
    show_tool_calls=True,
    markdown=True
)

while True:
    user_input = input("Enter your query (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    web_search_agent.print_response(user_input, stream=True)