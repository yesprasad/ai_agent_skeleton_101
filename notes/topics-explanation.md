🧩 "Reasoning = Planning how to achieve a goal using what I know and can do."
what is reasoning in an AI Agent? 
understand the user intent, collect what all resources are available at hand to address the intent
use the resources to accomplish the task to complete the intent and respond.

User asks: "What’s covered in mental health support?"
Perceive: It’s a question.
Reason: → I can best answer this if I run a RAG search over wellness documents.
Act: → Retrieve top chunks → construct prompt → send to LLM → return response.

A bit more on the Act step - 

Retrieve top chunks - to do this, the user question is converted to an embedding
the embedding is then sent to ChromDB to do a similarity search/ symantic search.
ChromaDB/ Vector database returns matching chunks 1 up to 10. 
These chunks along with the user question are fed into the LLM which processes them,
frames a user friendly, readable answer which is the response. 
LLM system can also be built to respond with citations for confidence.