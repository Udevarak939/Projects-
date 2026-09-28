# Enterprise LLM Data Analyst Agent

A portfolio-grade agentic analytics project inspired by the current enterprise move from chat-based assistance toward agents that can use business context, tools, and data to complete multi-step analytical work.

## What it does
A user asks a business question in natural language, such as:
"Why did revenue decline last month, which segments drove the change, and what should I investigate next?"

The agent:
1. Identifies the analytical intent.
2. Inspects an approved semantic schema.
3. Generates SQL.
4. Validates the SQL against allowed tables/columns.
5. Executes read-only queries.
6. Runs follow-up analysis when the first result is insufficient.
7. Produces a concise answer with KPI evidence and SQL used.
8. Logs latency, query cost proxy, tool calls, and evaluation results.

## Architecture
`User -> Planner -> Schema Retriever -> SQL Generator -> SQL Validator -> Read-only DB Tool -> Analyst/Evaluator -> Evidence-backed Answer`

## Core technologies
Python, SQL, PostgreSQL, Pandas, Streamlit, LLM API, embeddings/vector search, RAG, structured outputs, tool/function calling, evaluation, logging.

## Agent features
- Schema-aware Text-to-SQL
- RAG over KPI definitions and business glossary
- Read-only SQL execution
- Multi-step investigation
- Result-grounded explanations
- Citation/evidence objects
- SQL safety checks
- Prompt/version tracking
- Offline evaluation set

## Evaluation
Create a test set of business questions with expected SQL intent and required metrics. Track:
- SQL execution success
- Answer correctness
- Metric consistency
- Unsupported-claim rate
- Tool-call count
- Response latency

## Suggested repository structure
```text
enterprise-llm-data-agent/
├── app/
│   ├── agent.py
│   ├── planner.py
│   ├── sql_generator.py
│   ├── sql_validator.py
│   ├── tools.py
│   └── evaluator.py
├── data/
├── semantic_layer/
│   ├── metrics.yml
│   └── glossary.md
├── rag/
│   ├── index.py
│   └── retriever.py
├── evals/
│   └── benchmark.json
├── dashboard/
│   └── app.py
├── requirements.txt
└── README.md
```

## Why this project is current
Enterprise AI work is increasingly centered on agents that can reason over company context and take actions through tools. Current industry examples also emphasize grounded enterprise retrieval, observable agentic workflows, and AI-assisted work over analytical data. citeturn623033search0turn623033search6turn623033search13turn623033search17

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python rag/index.py
streamlit run dashboard/app.py
```

Keep credentials in environment variables and expose only approved read-only tools to the agent.

## Resume-ready impact
Engineered an enterprise LLM data analyst agent using RAG, schema-aware Text-to-SQL, tool calling, SQL validation, and evaluation to answer multi-step business questions with evidence-backed insights and production-oriented guardrails.
