# Mainframe RACF SIEM Intelligence Agent

**An agentic AI system that analyzes synthetic SMF Type 80 (RACF) logs to detect security incidents, perform threat hunting, and recommend z/OS-specific remediation steps.**

Welcome to the MainframeSecurityAiZOsRacfLogAnalysis Crew project, powered by [crewAI](https://crewai.com).

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![crewAI](https://img.shields.io/badge/crewAI-0.51+-orange.svg)](https://www.crewai.com/)
[![RAG](https://img.shields.io/badge/RAG-Enabled-green.svg)]()

---

## 🎯 Project Goal

Bridge **legacy z/OS mainframe security** (RACF + SMF logging) with **modern AI-driven SIEM** capabilities.

This project demonstrates how to apply agentic AI (crewAI + RAG) to interpret complex mainframe security logs — a rare and highly valuable skill in federal, financial, and enterprise environments.

## ✨ Key Features

- **Synthetic SMF/RACF Log Generator** — Creates realistic logs with injected attack scenarios (brute-force, access violations, privilege escalation)
- **Multi-Agent AI Workflow**:
  - **Log Parser Agent** — Ingests and structures raw SMF-style logs
  - **Threat Hunter Agent** — Uses RAG to match events against known mainframe attack patterns
  - **Incident Responder Agent** — Generates plain-language summaries and z/OS remediation commands (JCL/TSO)
- **Knowledge Base** — IBM Redbooks, RACF best practices, and MITRE ATT&CK for z/OS / Mainframe
- **Professional Reporting** — Clean, audit-ready incident reports

## 🛠️ Tech Stack

- **Orchestration**: crewAI + LangChain
- **LLM**: Google Gemini (via Google AI Studio)
- **RAG**: Chroma vector database
- **Data**: Synthetic SMF Type 80 (RACF) logs in JSON/CSV
- **Languages**: Python 3.11+

## 📁 Project Structure
mainframe-racf-siem-agent/
├── mock_mainframe_smf.py          # Synthetic log generator (with attack injection)
├── src/
│   ├── agents/                    # Log Parser, Threat Hunter, Incident Responder
│   ├── tools/
│   ├── knowledge_base/            # IBM Redbooks + MITRE ATT&CK documents
│   └── workflows/
├── synthetic_smf_logs.json
├── synthetic_smf_logs.csv
├── README.md
└── requirements.txt


## 🚀 Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/deadpoet/mainframe-racf-siem-agent.git
   cd mainframe-racf-siem-agent
   
2. **Install dependencies**
   pip install -r requirements.txt
   
3. **Generate synthetic logs**
   python mock_mainframe_smf.py

4. **Run the AI Agent (coming soon — currently building)**
   python run_agent.py

### Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/mainframe_security_intelligence_platform/config/agents.yaml` to define your agents
- Modify `src/mainframe_security_intelligence_platform/config/tasks.yaml` to define your tasks
- Modify `src/mainframe_security_intelligence_platform/crew.py` to add your own logic, tools and specific args
- Modify `src/mainframe_security_intelligence_platform/main.py` to add custom inputs for your agents and tasks


## 📊 Sample Output
- **Detected Incident:**
- High Severity: Multiple RACF logon failures (12 attempts in 8 minutes) by user BRUTEFORCE from IP 192.168.45.112 targeting TSO.LOGON.
- Possible Attack: Brute-force credential attack.
- **Recommended Action:**
  ```jcl
REVOKE BRUTEFORCE
SETROPTS REFRESH RACLIST(GENERIC)
SEARCH FILTER(UID(==BRUTEFORCE))

## 🎓 Why This Project Matters
- Demonstrates deep z/OS + RACF domain knowledge
- Shows practical application of AI to legacy systems (highly sought after in government and financial sectors)
- Portfolio piece for Cybersecurity Analyst, Cloud Security, GRC, and Mainframe Security roles

## 🔮 Future Enhancements
- Real-time log streaming simulation
- Integration with open-source SIEM (Wazuh / ELK)
- Web UI (Streamlit) for log upload and analysis
- Support for additional SMF record types (Type 30, 110, etc.)

Author: deadpoet
Focus: Mainframe Security | Cloud Security | AI-enhanced Cybersecurity
