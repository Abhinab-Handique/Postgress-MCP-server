📊 Database Talk: PostgreSQL MCP Server
This project implements a Model Context Protocol (MCP) server integrated into a FastAPI application. It allows Large Language Models (LLMs) like Claude or Cursor to interact directly with your PostgreSQL database using natural language to perform standard user management tasks.

🚀 Key Features
AI-Powered CRUD: Manage your users table via natural language (Get, Create, Delete).

FastAPI Integration: Mounted as a sub-application sharing the same database engine and lifespan.

Automatic Schema Sync: Database tables are created automatically on startup.

Secure Tooling: The LLM only sees specific tools you expose, preventing unauthorized database actions.

🛠️ Installation & Setup
Clone the repository:

Bash

git clone <your-repo-url>
cd <repo-folder>
Install dependencies:

Bash

pip install fastapi fastmcp sqlalchemy psycopg2-binary uvicorn
Configure Environment: Ensure your PostgreSQL connection string is set in your database configuration file.

Run the Server:

Bash

uvicorn main:app --reload
🤖 Exposed AI Tools
The LLM discovers the following capabilities automatically:

get_user: Retrieves user details by ID or fetches the full list.

create_user: Adds a new record to the database (e.g., "Add a user named John Doe").

delete_user: Removes a record based on a specific identifier.

🔗 Connection Details
When using an MCP client (like Claude Desktop), use the following SSE (Server-Sent Events) configuration:

URL: https://<your-ngrok-url>/mcp/sse

Method: SSE

Note: Visiting /mcp in a browser will return a 404. Use the /mcp/sse endpoint for AI client connections.

📁 Project Structure
app/controller/: API route definitions.

app/core/: Database engine and Base model setup.

main.py: The entry point where the MCP server is mounted to FastAPI.
