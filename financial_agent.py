import os
from phi.agent import Agent
from phi.model.groq import  Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
load_dotenv()


web_search_agent = Agent(
    name="Web Search Agent",
    role="Searrch the web for Information",
    model = Groq(
        model = "llama-3.3-70b-versatile",
        api_key=os.environ.get("GROQ_API_KEY")),
    tools=[DuckDuckGo(news=True,search=True)],
    instructions=["Alwasy include the sources"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)
#web_search_agent.print_response("Latest news from India", stream=True)

finance_agent = Agent(
    name="Finance Agent",
    model = Groq(
        model = "llama-3.3-70b-versatile",
        api_key=os.environ.get("GROQ_API_KEY")),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True,stock_fundamentals=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)
#finance_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)


multi_ai_agent = Agent(
    team=[web_search_agent,finance_agent],
    model = Groq(
        model = "llama-3.3-70b-versatile",
        api_key=os.environ.get("GROQ_API_KEY")),
    instructions=[web_search_agent.instructions[0],finance_agent.instructions[0]],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
    
)

multi_ai_agent.print_response('Summarise analyst recommendation and share the latest news for NVIDIA.',stream=True)
