# Corporate MCP Server 🔌🤖

A production-ready Model Context Protocol (MCP) server that exposes corporate tools and data sources to AI agents and LLM clients.

## Overview

MCP (Model Context Protocol) is an open standard created by Anthropic in 2024 that allows AI models to securely connect to external tools and data sources. This server exposes corporate data — companies, employees, and system status — as MCP tools that any compatible AI client can use.

## What is MCP?

Think of MCP as a **universal plugin system for AI agents**:
- Before MCP: every agent had its own way of connecting to tools
- With MCP: one standard server exposes tools, any compatible client consumes them

Compatible clients include Claude Desktop, and any LLM agent built with the MCP SDK.

## Available Tools

| Tool | Description | Parameters |
|------|-------------|-----------|
| `get_company_info` | Get detailed company information | `company_id` (acme-corp, globex) |
| `search_employees` | Search employees by department/location | `department`, `location` (optional) |
| `get_system_status` | Get operational status of systems | `system_name` (optional) |

## Features

- 🔌 **MCP compliant** — works with any MCP-compatible client
- 🏢 **Corporate data** — companies, employees, system monitoring
- ✅ **Fully tested** — 8 unit tests covering all tools
- 🔒 **Secure** — no sensitive data exposed, environment-based config
- 🐍 **Pure Python** — no database required, easy to extend

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Protocol | MCP (Model Context Protocol) |
| Runtime | Python 3.11+ asyncio |
| Server | MCP Python SDK |
| Testing | pytest |

## Getting Started

### Prerequisites

- Python 3.11+
- Claude Desktop (optional, for interactive testing)

### Installation

1. Clone the repository
```bash
git clone https://github.com/Pablo4costa/corporate-mcp-server.git
cd corporate-mcp-server
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate       # Linux/Mac
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the server
```bash
python -m app.main
```

The server communicates via stdio and is ready to accept MCP client connections.

## Connect to Claude Desktop

Add this to your Claude Desktop config file (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "corporate": {
      "command": "python",
      "args": ["-m", "app.main"],
      "cwd": "/path/to/corporate-mcp-server"
    }
  }
}
```

Once connected, Claude Desktop can use all corporate tools directly in conversation.

## Running Tests
```bash
pytest tests/ -v
```

Expected output:
```
tests/test_server.py::test_get_company_info_found PASSED
tests/test_server.py::test_get_company_info_not_found PASSED
tests/test_server.py::test_search_employees_by_department PASSED
tests/test_server.py::test_search_employees_by_location PASSED
tests/test_server.py::test_search_employees_all PASSED
tests/test_server.py::test_get_system_status_all PASSED
tests/test_server.py::test_get_system_status_specific PASSED
tests/test_server.py::test_get_system_status_not_found PASSED

8 passed in 0.04s
```

## Project Structure
```
corporate-mcp-server/
├── app/
│   ├── main.py           # Entry point
│   ├── server.py         # MCP server definition and tool handlers
│   ├── tools/
│   │   ├── company.py    # Company information tool
│   │   ├── employees.py  # Employee search tool
│   │   └── systems.py    # System status tool
│   └── resources/
│       └── data.py       # Corporate data (replace with DB in production)
├── tests/
│   └── test_server.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Extending the Server

To add a new tool:

1. Create a function in `app/tools/`
2. Register it in `app/server.py` with `@app.list_tools()` and `@app.call_tool()`
3. Add tests in `tests/test_server.py`

In production, replace the mock data in `app/resources/data.py` with real database connections.

## License

MIT