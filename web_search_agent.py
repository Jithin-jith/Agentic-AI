import os
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import  Groq
from dotenv import load_dotenv
load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(model = "llama-3.3-70b-versatile",
        api_key=os.environ.get("GROQ_API_KEY")),
    tools=[DuckDuckGo(news=True,search=True)],
    instructions=["detailed description"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)
web_agent.print_response("Tell me about South Korea plane crash", stream=True)
