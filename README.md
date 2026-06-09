# Web Scraper Automation: Autonomous Knowledge Graph Agent

A modular, decoupled data engineering pipeline and autonomous AI agent designed to convert unstructured media links into deeply contextual, structured knowledge repositories.

By leveraging **Playwright** for resilient, session-aware browser automation and **Gemini** for dual-stage linguistic processing, this system executes a continuous loop of extraction, sanitization, and biographical profiling without manual intervention.

## 🚀 Core Features

* **Session-Aware Browser Reuse:** Implements a single persistent Chromium context across the entire batch execution cycle, bypassing anti-bot constraints and eliminating cold-start multi-tab load penalties.
* **Dual-Stage LLM Pipeline:** Decouples raw entity extraction from deep biographical synthesis to maximize data integrity and token efficiency.
* **Historical Figure Override & Failsafe:** Built-in prompt engineering directives to ensure objective, historicist archiving of controversial figures while filtering out unverified or obscure entities via strict `UNKNOWN` triggers.
* **Automated Categorization & Routing:** Dynamically parses structural routing tags from the agent response to seamlessly sort output Markdown files into dedicated domain folders.
* **Obsidian-Ready Output:** Generates rich Markdown files pre-formatted with YAML frontmatter tags and explicit internal `[[Wiki-Links]]` for instantaneous data visualization inside a personal knowledge management system.

## 📁 Repository Structure

```text
.
├── gemini_engine.py          # Browser automation driver & low-level network worker
├── master_orchestrator.py     # Central pipeline conductor executing cyclic jobs
├── auth_setup.py              # Session authentication utility for manual login profiling
├── youtube_links.csv         # Input target queue containing source URLs
├── data/                      # Encapsulated data directory (Ignored from version control)
│   ├── master_processed_names.txt  # State-machine ledger tracking indexed profiles
│   ├── raw_extraction_logs/        # Audit trails of raw entity lists per video link
│   └── profiles/                  # Dynamically routed knowledge tree
│       ├── Actors/
│       ├── Politics_and_History/
│       └── Science_and_Tech/
└── ytchannel_link_scraper/    # Utility module for upstream link gathering

```

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Automation Framework:** Playwright (Async Python API)
* **AI Integration:** Google Gemini (Web Automation Layer)
* **Knowledge Format:** Markdown + YAML Frontmatter (Obsidian Compatible)
