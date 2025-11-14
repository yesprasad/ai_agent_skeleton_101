Wellness AI Agent
The AI agent is designed for employees of health insurance subscribers—typically working for companies that offer wellness benefits via providers

end users are - Employees, HR to get answers to their benefits.
Say a compancy "COM" has taken a wellness plan from a health insurance provider like "HIP",
the HR and employees of the COM comapany can use this AI Agent to get answers on their benefits.

simple tasks that this AI agent can answer can be - 
What’s the max I can claim for gym membership?
Summarize mental health benefits.
Compare nutrition vs mental health support cost or coverage.

```mermaid
flowchart TD
    A[Start: User Query\n(e.g., "Max gym claim?")] --> B[Input Preprocessing\n(Clean, classify intent)]
    B --> C{Intent Matches Benefits?}
    C -->|No| D[Error / Clarify Response\n(e.g., "Ask about wellness only")]
    C -->|Yes| E[Retrieve Relevant Docs\n(Vector DB search on benefits data)]
    E --> F[Augment Prompt with Context\n(Retrieved chunks + query)]
    F --> G[LLM Generation\n(Answer via model like GPT)]
    G --> H[Post-Process Output\n(Format, cite sources)]
    H --> I[End: Deliver Response\n(e.g., "Max $500/year for gym")]
    D --> I

    style A fill:#e1f5fe
    style I fill:#c8e6c9
