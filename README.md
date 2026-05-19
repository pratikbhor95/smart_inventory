# 🏠 Smart Home Inventory Assistant (Phase 1)

An intelligent, self-hosted home inventory system powered by local AI, a PostgreSQL vector database, and dual frontend interfaces. This project turns your always-on Windows PC into a private home server that can understand human synonyms (e.g., matching "hair maker" to "comb") via semantic vector search.

---

## 🏗️ System Architecture

The project relies on an **API-First Architecture** where a centralized FastAPI engine acts as the singular source of truth. Both the Next.js Administrative Dashboard and the Telegram Bot query the same backend endpoints, ensuring perfect synchronization without duplicated business logic.

```
                  ┌─────────────────────────────────────────────────────────────┐
                  │                       YOUR WINDOWS PC                       │
                  │                                                             │
                  │   ┌──────────────────┐           ┌──────────────────────┐   │
                  │   │  Ollama Engine   │◄─────────►│  PostgreSQL Database │   │
                  │   │(nomic-embed-text)│           │     (pgvector)       │   │
                  │   └────────▲─────────┘           └──────────▲───────────┘   │
                  │            │                                │               │
                  │            └───────────────┬────────────────┘               │
                  │                            ▼                                │
                  │               ┌──────────────────────────┐                  │
                  │               │    FastAPI Backend App   │                  │
                  │               └────────────▲─────────────┘                  │
                  └────────────────────────────┼────────────────────────────────┘
                                               │
                               ┌───────────────┴───────────────┐
                               ▼                               ▼
                       ┌───────────────┐               ┌───────────────┐
                       │  Phase 1 UI   │               │  Phase 1 UI   │
                       │ Telegram Bot  │               │ Next.js Admin │
                       │ (Mobile Lens) │               │ (Web Control) │
                       └───────────────┘               └───────────────┘
```

---

## 🛠️ Tech Stack & Purpose

### 🧠 Core Infrastructure
* **Windows OS (Local Host):** Serves as the continuous, always-on server environment, allowing instant access to local hard drive folders for photo storage without cloud hosting fees.
* **Docker Desktop:** Runs the containerized PostgreSQL environment reliably with isolated resources.
* **PostgreSQL (v17):** The central relational database management system tracking item locations, quantities, and structural storage units.
* **`pgvector` Extension:** Empowers Postgres to run high-dimensional mathematical distance operations directly inside SQL scripts for AI vector evaluations.

### 🤖 Local AI Runtime
* **Ollama Engine:** A free, private tool running locally on your hardware to compute deep learning operations without sending household profiles to external companies.
* **`nomic-embed-text` Model:** Translates plaintext names, descriptions, and spaces into a 768-dimension continuous coordinate space to evaluate conceptual linguistic associations.

### ⚡ Application Logic
* **Python 3.11+:** Orchestrates data handling, background text manipulation, and operational pipelines.
* **FastAPI:** High-performance async web platform facilitating data transactions between the storage systems and the frontend interfaces.

### 📱 Frontend Delivery Channels
* **Next.js (React):** A rich browser-based administrative interface optimized for heavy tasks like bulk Excel uploads and catalog layouts.
* **Telegram Bot API:** A lightweight, cross-platform mobile interface enabling rapid vocal or written search inquiries, structured menu toggling, and visual photo delivery.

---

## 📋 Phase 1 Feature Matrix

### 🖥️ Next.js Administrative Dashboard
* **Single Product Intake Form:** Input name, custom notes/synonyms, room coordinates, storage subdivisions, quantities, and specific volume metrics (e.g., *pieces, pairs, kg*), alongside an integrated graphic file attachment module.
* **Bulk Excel Importer:** Drag-and-drop parser processing standard `.xlsx` spreadsheets, including cross-examination safeguards to warn users if a product entry references a filename missing from the local photos catalog.
* **Master Inventory Grid:** Unified administration board showing real-time item rows, storage locations, metrics, and active image thumbnails.

### 📱 Telegram Chat Interface
* **`/stats` Diagnostics Command:** Returns local system health data (CPU load, active RAM allocations, and primary hard drive metrics) with a secure middleware barrier restricting access to authorized Telegram IDs.
* **Natural Language Semantic Engine:** Allows standard chat queries (e.g., *"Where did I put the hair maker?"*). Resolves intent to the nearest database vector and outputs matching names, locations, and balances.
* **Smart Association Triggers:** Detects high-priority kitchen queries (e.g., *"Tea"*), returns the core target location, and appends suggestions for associated inventory pairs (*Sugar, Milk*).
* **`/locate [Location]` Module:** Retrieves an itemized summary of a drawer or shelf and structures matching imagery into a single native Telegram Media Album with custom caption text metadata.

---

## 💾 Core Database Design (`items`)

| Column Name | Data Type | Modifiers | Description |
| :--- | :--- | :--- | :--- |
| `id` | SERIAL | PRIMARY KEY | Unique item tracking code |
| `name` | VARCHAR(255) | NOT NULL | Canonical identifier (e.g., *Comb*) |
| `description`| TEXT | | Explanatory context, synonyms, or tags |
| `room` | VARCHAR(100) | NOT NULL | Physical macro placement (e.g., *Bedroom*) |
| `storage_unit`| VARCHAR(100) | NOT NULL | Micro storage zone (e.g., *Drawer 2*) |
| `quantity` | NUMERIC(10,2) | NOT NULL | Current numeric count or mass value |
| `unit` | VARCHAR(50) | NOT NULL | Quantitative scale metric (*pieces, pairs, kg*) |
| `image_name` | VARCHAR(255) | DEFAULT 'placeholder.jpg'| Linked filename inside local folder |
| `embedding` | VECTOR(768) | | Mathematical vector output from Ollama |

---

## 🚀 Setting Up Locally

### 1. Initialize Postgres via Docker
Ensure Docker Desktop is open on your Windows PC. Create a `docker-compose.yml` file with your settings and run:
```bash
docker compose up -d
```
Connect via any database utility using port `5432` and execute this foundational statement once to enable vector extensions:
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

### 2. Pull the AI Embedding Model
In your Windows Command Prompt, execute:
```bash
ollama pull nomic-embed-text
```

### 3. Initialize the Core Application Directory
Create the local file structure required to host file uploads:
```text
📦 home-inventory
 ┣ 📂 data
 ┃ ┗ 📂 product_photos
```
All system images processed by either Next.js or the Excel automation scripts will populate this `product_photos` directory.
