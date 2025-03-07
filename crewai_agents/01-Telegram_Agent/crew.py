from crewai import Agent, Task, Crew, LLM
from composio_crewai import ComposioToolSet, App
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    api_key=os.getenv("GROQ_API_KEY"),
    model="groq/deepseek-r1-distill-llama-70b",
    verbose=True,
    temperature=0.1  # Lower temperature for more focused responses
)

toolset = ComposioToolSet()
tools = toolset.get_tools(actions=['GOOGLECALENDAR_FIND_EVENT', 'GOOGLECALENDAR_CREATE_EVENT', 'GOOGLECALENDAR_DELETE_EVENT', 'GOOGLECALENDAR_UPDATE_EVENT'])


telegram_agent = Agent(
    role="telegram_agent",
    goal="Manage Google Calendar events",
    backstory="You are a helpful assistant that can help users manage their Google Calendar events.",
    llm=llm,
    tools=tools,
    verbose=True
)

telegram_agent_task = Task(
    description="Help the user with their requests: {user_input}. Remember today's date is {date}",
    expected_output="A very simple and concise answer to user's response",
    agent=telegram_agent
)

crew = Crew(
    agents=[telegram_agent],
    tasks=[telegram_agent_task],
    verbose=True
)

result = crew.kickoff()
print("Result:", result)