# 📂 Project Directory Structure 

This document defines the standard layout tree for the Smart Home Inventory Assistant ecosystem. Follow this organization precisely to maintain a clean decoupling between the administrative dashboard (`frontend`), the core application engine (`backend`), and the conversational agent (`telegram_bot`).

```text
📦 home-inventory
 ┣ 📂 backend
 ┃ ┣ 📂 app
 ┃ ┃ ┣ 📂 api
 ┃ ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┃ ┣ 📜 admin.py          # Form uploads & Excel ingestion logic
 ┃ ┃ ┃ ┗ 📜 search.py         # Vector similarity search endpoints
 ┃ ┃ ┣ 📂 core
 ┃ ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┃ ┣ 📜 config.py         # App environment constants & DB settings
 ┃ ┃ ┃ ┗ 📜 database.py       # SQLAlchemy engine & session initialization
 ┃ ┃ ┣ 📂 models
 ┃ ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┃ ┗ 📜 item.py           # Core SQLAlchemy models for 3NF tables
 ┃ ┃ ┣ 📂 schemas
 ┃ ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┃ ┗ 📜 item.py           # Pydantic models for request/response validation
 ┃ ┃ ┗ 📜 main.py             # FastAPI entry point, CORS configuration
 ┃ ┣ 📜 .env                  # Private database strings and Ollama URL
 ┃ ┣ 📜 Dockerfile            # Container definition for the FastAPI backend
 ┃ ┗ 📜 requirements.txt      # Python dependencies (fastapi, psycopg2, pandas)
 ┣ 📂 data
 ┃ ┣ 📂 product_photos        # Master local filesystem vault for item images
 ┃ ┗ 📜 inventory_template.xlsx # Ingestion reference template
 ┣ 📂 frontend
 ┃ ┣ 📂 app
 ┃ ┃ ┣ 📂 admin
 ┃ ┃ ┃ ┣ 📂 add-item
 ┃ ┃ ┃ ┃ ┗ 📜 page.js         # Single item administrative form
 ┃ ┃ ┃ ┣ 📂 import
 ┃ ┃ ┃ ┃ ┗ 📜 page.js         # Excel drop-zone interface
 ┃ ┃ ┃ ┗ 📜 page.js           # Inventory grid and monitoring hub
 ┃ ┃ ┣ 📜 layout.js           # Next.js structural container
 ┃ ┃ ┗ 📜 page.js             # Root application redirection landing
 ┃ ┣ 📜 package.json          # Node app packages & runtime scripts
 ┃ ┗ 📜 next.config.js        # Config defining local static file routing
 ┣ 📂 telegram_bot
 ┃ ┣ 📜 .env                  # Bot API token & restriction user list
 ┃ ┣ 📜 bot.py                # BotFather connection polling daemon
 ┃ ┗ 📜 handlers.py           # Functions executing /stats, /locate, & natural queries
 ┣ 📜 .gitignore              # Ignores data images, node_modules, and env profiles
 ┗ 📜 docker-compose.yml      # Master script managing PostgreSQL & pgvector