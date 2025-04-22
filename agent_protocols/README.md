## Project-1 Overview:
**MCP Server with mem0:**
This project demonstrates how to build an MCP server in python where it exposes 3 tools - save_memory, get_all_memories, search_memories which is built using Mem0. It can be used by any agent(mcp client) to connect to this mcp server and use the tools.


### Steps:
1. Importing the necessary dependencies
2. Creating the Mem0Context class for async context management, you can compare it to singleton pattern for managing the mem0 client so that it is only created once and reused across the application
3. Defining the mcp tools: save_memory, get_all_memories, search_memories
4. Finally starting the mcp server when file is run

**Youtube Tutorial:** [Watch the tutorial here](https://youtu.be/lbyPJqCI-tw?si=KM9sQGKF28LtEQ5e)
<br>
**Github:** [Github Link](https://github.com/coleam00/mcp-mem0)


---


