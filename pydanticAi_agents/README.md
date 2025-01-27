
## Project-1 Overview:
**RAG Agent:**
This project implements an advanced Retrieval-Augmented Generation (RAG) system that crawls and processes the Pydantic AI documentation. It features both basic RAG and agentic RAG capabilities, where the latter allows the LLM to dynamically query the vector database multiple times for comprehensive responses. The system includes a website crawler, Supabase vector storage, and a Streamlit UI for user interaction.

### Steps:
1. Normal RAG without agentic -> Simply the result given from vector db is passed to LLM and generates the response, here the LLM can't call the vector db again if the results from vector db are not enough. There's where agentic RAG comes in.
2. Agentic RAG -> The RAG is given as tool to the LLM, so the LLM can call the vector db again if the results from vector db are not enough.
3. RAG Website Crawler -> Supabase Setup -> Ai Agent Setup -> Agentic RAG -> Streamlit Ui
```
RAG Website Crawler(crawl_pydantic_ai_docs.py)

1. main func() --> get_pydantic_ai_docs_urls(), crawl_parallel(urls)

2. get_pydantic_ai_docs_urls()

3. crawl_parallel() --> process_url(url), process_and_store_document(url, result.markdown_v2.raw_markdown)

4. process_and_store_document() --> chunk_text(markdown), process_chunk(chunk, i, url), insert_chunk(chunk)

5. process_chunk() --> get_title_and_summary(chunk, url), get_embedding(chunk)

6. Individual Functions -> chunk_text(), insert_chunk(), get_title_and_summary(), get_embedding()
```
4. Setup the supabase db, write the sql scripts for creating the tables and a database func for similarity search. Finally executing the script in supabase.
5. Setting up the ai agent with pydantic ai -> 1. Defining the dependencies. 2. Defining the agent. 3. Defining the tools
6. Trying out the basic RAG without agentic -> i.e. just using the retrieve_relevant_documentation() tool -> It works but the response after just using this tool is not just sufficient, suppose there is an long example code in the docs, then it results in giving a small portion of the code instead of the whole long code.
7. Then trying it with adding more tools so that the agent get more context and can use those extra tools to get the whole long code.
8. Adding in list_documentation_pages() and get_page_content() tools and a well defined system prompt to use these tools.
9. Finally adding in the web ui using streamlit, using streaming responses from pydantic ai.

**Conclusion:** What I learned from this project is, adding more tools so that agent can be more accurate with its responses, writing a well defined system prompt to use those tools and overall working of when what to do. All these increases the accuracy and quality of the responses and make the ai agent more practical.

**Youtube Tutorial:** [Watch the tutorial here](https://youtu.be/_R-ff4ZMLC8?si=CGCJM0SoMmNczXe4)

---