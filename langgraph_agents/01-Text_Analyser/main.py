from typing import TypedDict, List # for defining the state
from langgraph.graph import StateGraph, END, message # for creating the whole graph workflow
from langchain.prompts import PromptTemplate 
from langchain.schema import HumanMessage
from langchain_core.runnables.graph import MermaidDrawMethod
from IPython.display import display, Image
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
load_dotenv()

# 1. Defining the state and the llm
class State(TypedDict):
    text: str
    classification: str
    entities: List[str]
    summary: str

llm = ChatGroq(
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
)



# 2. Define the Node Functions
def classification_node(state: State):
    "Research, News, Blog, Other"
    prompt = PromptTemplate(
        input_variable = ["text"],
        template = """
        Classify the following text into one of the categories: News, Blog, Research , or Other.
        Text: {text}
        Category:
        """
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    classification = llm.invoke([message]).content.strip()
    return {"classification": classification}

def entity_extraction_node(state: State):
    prompt = PromptTemplate(
        input_variable = ["text"],
        template = """
        Extract all the entities (Person, Organization, Location) from the following text. Provide the result as a comma separated list.
        Text: {text}
        Entities:
        """
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    entities = llm.invoke([message]).content.strip().split(", ")
    return {"entities": entities}

def summarization_node(state: State):
    prompt = PromptTemplate(
        input_variable = ["text"],
        template = """
        Summarize the following text in one short sentence.
        Text: {text}
        Summary:
        """
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    summary = llm.invoke([message]).content.strip()
    return {"summary": summary}



# 3. Create tools & Build Workflow
workflow = StateGraph(State)

workflow.add_node("classification_node", classification_node)
workflow.add_node("entity_extraction_node", entity_extraction_node)
workflow.add_node("summarization_node", summarization_node)

workflow.set_entry_point("classification_node")

workflow.add_edge("classification_node", "entity_extraction_node")
workflow.add_edge("classification_node", "summarization_node")
workflow.add_edge("summarization_node", END)

app = workflow.compile()


# 4. Visualize the Workflow
display(
    Image(
        app.get_graph().draw_mermaid_png(
            draw_method=MermaidDrawMethod.API
        )
    )
)


# 5. Testing the Pipeline
SAMPLE_TEXT = """
OpenAI has announced the GPT-4 model, which is a large multimodal model that exhibits human-level performance on various professional benchmarks. It is developed to improve the alignment and safety of AI systems.
additionally, the model is designed to be more efficient and scalable than its predecessor, GPT-3. The GPT-4 model is expected to be released in the coming months and will be available to the public for research and development purposes.
"""
state_input = {"text": SAMPLE_TEXT}
result = app.invoke(state_input)
print(f"Result: {result}")

