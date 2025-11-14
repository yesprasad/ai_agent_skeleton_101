rag_ai_agent/
├── agent/
│   ├── perceive.py
│   ├── reason.py
│   └── act.py
├── core/
│   ├── embedder.py
│   ├── retriever.py
│   ├── llm_interface.py
│   └── chunker.py
├── Documents/
│   └── wellness_plan.txt
├── main.py
└── requirements.txt

``` mermaid
flowchart TD
    A[🧑‍💻 User Input] --> B[🔍 Perceive Intent]
    B --> C[🧠 Reason - Generate Plan]
    C --> D[🤖 Act - Execute Plan]
    
    D --> E[📚 Retrieve Context (ChromaDB)]
    D --> F[💬 LLM Response (Ollama)]
    
    E --> F
    F --> G[🎯 Final Response to User]
    ```
