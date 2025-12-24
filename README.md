# LangGraph Template Project

This repository is a clean and minimal **LangGraph-based Python project template** designed for building, experimenting, and deploying **LLM-powered agents**.

It follows best practices for:
- Python project structure
- Dependency management using **uv**
- Environment variable handling
- Git hygiene using `.gitignore`

---

## 📁 Project Structure

```text
LANGGRAPH-TEMPLATE/
│
├── src/                # Application source code
├── tests/              # Unit and integration tests
│
├── .qodo/              # Tool-specific or local config (ignored by git)
├── .venv/              # Python virtual environment (ignored)
│
├── .env.example        # Sample environment variables
├── .gitignore          # Git ignore rules
├── .python-version     # Python version for consistency
├── main.py             # Application entry point
├── pyproject.toml      # Project metadata and dependencies
├── requirements.txt    # Dependency list (reference)
├── uv.lock             # Locked dependencies for reproducibility
└── README.md           # Project documentation
