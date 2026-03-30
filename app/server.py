from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from app.tools.company import get_company_info
from app.tools.employees import search_employees
from app.tools.systems import get_system_status
import json

app = Server("corporate-mcp-server")

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="get_company_info",
            description="Get detailed information about a company by its ID. Available companies: acme-corp, globex",
            inputSchema={
                "type": "object",
                "properties": {
                    "company_id": {
                        "type": "string",
                        "description": "The company ID (e.g. acme-corp, globex)"
                    }
                },
                "required": ["company_id"]
            }
        ),
        Tool(
            name="search_employees",
            description="Search employees by department and/or location. Departments: Engineering, HR, Finance. Locations: New York, Chicago, Remote",
            inputSchema={
                "type": "object",
                "properties": {
                    "department": {
                        "type": "string",
                        "description": "Department name (Engineering, HR, Finance)"
                    },
                    "location": {
                        "type": "string",
                        "description": "Location (New York, Chicago, Remote)"
                    }
                }
            }
        ),
        Tool(
            name="get_system_status",
            description="Get operational status of corporate systems. Leave empty to get all systems.",
            inputSchema={
                "type": "object",
                "properties": {
                    "system_name": {
                        "type": "string",
                        "description": "System name (api-gateway, database-primary, cache-redis, ml-inference, storage-s3)"
                    }
                }
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "get_company_info":
        result = get_company_info(arguments["company_id"])
    elif name == "search_employees":
        result = search_employees(
            department=arguments.get("department"),
            location=arguments.get("location")
        )
    elif name == "get_system_status":
        result = get_system_status(
            system_name=arguments.get("system_name")
        )
    else:
        result = {"error": f"Unknown tool: {name}"}

    return [TextContent(type="text", text=json.dumps(result, indent=2))]

async def run():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())