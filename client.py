# Assumes the FastAPI app from above is already defined
from fastmcp import FastMCP
from fastmcp.client import Client
import asyncio

# Convert to MCP server
client = Client("main.py")
async def demo():
    async with client:
        # List available tools
        tools = await client.list_tools()
        print(f"Available tools: {[t.name for t in tools]}")
        
        # Create a product
 

if __name__ == "__main__":
    asyncio.run(demo())