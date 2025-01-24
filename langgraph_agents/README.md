
### Project-1 Overview:
In this project, we'll demonstrate the power of LangGraph by building a multi-step text analysis pipeline. Our use case will focus on processing a given text through three key stages:

- Text Classification: We'll categorize the input text into predefined categories (e.g., News, Blog, Research, or Other).
- Entity Extraction: We'll identify and extract key entities such as persons, organizations, and locations from the text.
- Text Summarization: Finally, we'll generate a concise summary of the input text.


### Steps:
1. `poetry new langgraph`, `poetry env use python3.11`, `poetry shell`, `poetry add langchain langchain_core langchain_community langgraph`
2. Building the text processing pipeline
    - Define State & Initialize LLM
    - Define Node Functions
    - Create tools & Build Workflow
    - Visualize the Workflow
    - Testing the Pipeline

3. `poetry add langchain_groq`, `poetry add ipython`, `poetry add dotenv`
4. `poetry run langgraph_stuff/proj_1.py`
```js
const data = { 
    
    'text': '\nOpenAI has announced the GPT-4 model, which is a large multimodal model that exhibits human-level performance on various professional benchmarks. It is developed to improve the alignment and safety of AI systems.\nadditionally, the model is designed to be more efficient and scalable than its predecessor, GPT-3. The GPT-4 model is expected to be released in the coming months and will be available to the public for research and development purposes.\n', 
    
    'classification': "Category: News\n\nReason: The text appears to be a factual report about a recent development in the field of AI, specifically the announcement of the GPT-4 model by OpenAI. The language used is formal and objective, and the text provides information about the model's features and expected release date, which is typical of news articles.", 
    
    'entities': ['OpenAI', 'GPT-4', 'GPT-3'], 
    
    'summary': 'OpenAI has announced the GPT-4 model, a large multimodal model that exhibits human-level performance and is designed to be more efficient and safer than its predecessor.' 

}
```

---


### Project-2 Overview:
Project Overview: Essay Grading System:
In this project, we'll demonstrate the power of LangGraph by building a multi-step essay grading system. Our use case will focus on processing a given essay through four key stages:

- Content Relevance: Assesses how well the essay addresses the given topic
- Grammar Check: Evaluates the essay's language usage and grammatical correctness
- Structure Analysis: Examines the organization and flow of ideas in the essay
- Depth of Analysis: Gauges the level of critical thinking and insight presented

### Steps:
1. Building The Essay Grading System pipeline
    - Define State & Initialize LLM
    - Define Node Functions
    - Create tools & Build Workflow
    - Visualize the Workflow
    - Essay Grading Function
    - Testing the Pipeline
2. `poetry run langgraph_stuff/proj_2.py`
```
Final Essay Score: 0.88

Relevance Score: 1.00

Grammar Score: 0.95

Structure Score: 0.90

Depth Score: 0.70
```

---


### Project-3 Overview:
Multi-Agent Software Team:

**Agents**
- Analyst: You are a software requirements analyst. Review the provided instructions and generate software development requirements that a developer can understand and create code from. Be precise and clear in your requirements.
- Architect: You are an Software Architect who can design scalable systems that work in cloud environments. Review the software requirements provided and create an architecture document that will be used by developers, testers and designers to implement the system. Provide the architecture only.
- Developer: You are an Full Stack Developer and can code in any language. Review the provided instructions and write the code. Return the coding artifacts only.
- Reviewer: You are an experienced developer and code reviewer. You know the best design patterns for web applications that run on the cloud and can do code reviews in any language. Review the provided code and suggest improvements. Only focus on the provided code and suggest actionable items.
- Tester: You are a test automation expert who can create test scripts in any language. Review the provided user instructions, software requirements and write test code to ensure good quality of the software.
- Diagram Designer: You are a Software Designer and can draw diagrams explaining any code. Review the provided code and create a Mermaid diagram explaining the code.
- Summary Writer: You are an expert in creating technical documentation and can summarize complex documents into human-readable documents. Review the provided messages and create a meaningful summary. Retain all the source code generated and include it in the summary.

### Steps:
1. `poetry add python-dotenv langgraph langchain_openai langchain-core pydantic streamlit typing`
2. Building The Multi-Agent Software Team pipeline
    - Define State (State/GraphState)
    - Create the graph (workflow/builder)
    - Create the LLM
    - Create the Node Functions
    - Add nodes to the graph
    - Set entry point and edges
    - Compile and run the builder (app/graph)
    - Draw the graph
    - Create a main loop for the chatbot
3. Each node has the access to the responses of the previous nodes, the `add_messages` property in the GraphState is used to add messages to the state from each node
4. Adding a new project on LangSmith - Langgraph_Agents, added the langsmith api keys in the .env file(For tracing purposes)