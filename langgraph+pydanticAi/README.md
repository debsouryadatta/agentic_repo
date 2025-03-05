## Project-1 Overview:
**Archon:**
Archon is an AI agent that is able to create other AI agents using an advanced agentic coding workflow and framework knowledge base to unlock a new frontier of automated agents.

### Why use both LangGraph and Pydantic AI?
- The results of using only pydantic ai for this purpose are not satisfactory. We need something more advanced and more detailed to make sure its reading through the pydantic ai documentation correctly and using it correctly thats where we need a graph approach, an agentic workflow i.e. langgraph.
- We will have the Langgraph for building the workflow and the pydantic ai for building the agents with the tools required for the workflow with routing and conditional edges as and when required.
- We can even use the human in the loop, which can be implemented using the langgraph.
- Archon v1 was built just using pydantic ai, just like the RAG agent we built using pydantic ai docs but changing the system prompt so that it provides the code for the agents that users are asking for. But still the results are not satisfactory.
- Archon v2 will use both langgraph and pydantic ai.

### Files:
- streamlit_ui.py -> The chat ui for users to interact with the langgraph + pydantic ai agent builder.
- crawl_pydantic_ai_docs.py -> The website crawler that crawls the pydantic ai documentation and stores it in the supabase database.
- ollama_site_pages.sql & site_pages.sql -> The sql file that creates the site_pages table in the supabase database with dynamic functions for easy RAG
- pydantic_ai_coder.py -> The agent that codes the agent based on the deps, user_input and the message_history. Similar to RAG agent we built using pydantic ai docs.
- archon_graph.py -> The main langgraph workflow with pydantic ai agents and tools.


### Steps:
1. Writing the code for the archon_graph.py
2. Taking in the imports from pydantic_ai, langgraph, typing, dotenv, openai, supabase, logfire and pydantic_ai_coder.py
3. Defining the base_url, api_key, is_ollama
4. Defining the reasoner_llm_model and the reasoner_agent
5. Defining the router_agent and the end_conversation_agent with primary_llm_model
---
6. Defining the nodes, first with the "define_scope_with_reasoner" -> It create a detailed scoped document required for building the agent that user has requested. It also takes in the list of document pages in the system prompt and provides the document pages that are relevant, in the scope document itself.
7. Next node "coder_agent" -> It calls the pydantic_ai_coder agent with the deps, user input and the message_history. It takes in the scope document in the system prompt and provides the code for the agent which gets streamed back to the user to the streamlit ui. The writer can be passed on any node function(by default in langgraph) as a parameter which helps in streaming of the response.
8. Imp note -> The result.new_messages_json() given by the pydantic ai agents contains the human and ai messages as well as the tool calls user,etc.
9. Next node "get_next_user_message" -> Interrupts the graph to get the user's next message(Human in the loop)
10. Next router function "route_user_message" -> It determines if the user is finished creating their AI agent or not based on the user's new input.
11. Next node "finish_conversation" -> End the conversation for creating an AI agent by giving instructions for how to execute the agent and they saying a nice goodbye to the user. It takes in the whole message_history and curates the final response.
---
12. Building the workflow, adding the nodes and the edges between them.
13. Adding a conditional edge with a router function(route_user_message) in between "get_next_user_message" and "finish_conversation" -> It checks if the user's new input is more related to ending the conversation or modifying the agent. Based on that the flow goes to the appropriate node.
14. Finally providing the memory saver checkpointer which checkpoints the State as the graph works through each node. We can also use thread_id just like chat_id to save the conversation state to that id.

---

### My doubt question to cole:
Hey, this was just fantastic, I guess langgraph + pydantic ai will be my goto for my next agents.
Had a question to clear, when we send an initial message in the streamlit ui, the first response coming from the graph gets stuck in the interrupt and not ending the conversation till we say that "the agent is perfect, we can end". Or if we say "modify a specific part", it will go again to the coder_agent node and again get stuck on the interrupt right? So am I thinking the right way or there is a mismatch in my thinking, will be very helpful if you could clear this up!

### For usuage of this project:
Follow this docs -> https://github.com/coleam00/Archon/blob/main/iterations/v2-agentic-workflow/README.md

