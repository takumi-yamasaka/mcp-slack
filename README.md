# MCP Client for Trast Project

Multi-provider Chat Protocol (MCP) client application for the Trast project. This application helps new team members understand project specifications through a ChatGPT-like interface.

## Features

- Chat interface for querying project information
- Knowledge base for the Trast project
- Conversation history tracking
- Responsive UI design

## Technology Stack

- **Backend**: Python with FastAPI
- **Frontend**: React with TypeScript
- **Database**: PostgreSQL
- **Containerization**: Docker
- **AI Integration**: OpenAI API

## Project Structure

```
mcp-slack/
├── backend/                # FastAPI backend
│   └── mcp_backend/
│       ├── app/
│       │   ├── api.py      # API endpoints
│       │   ├── config.py   # Configuration settings
│       │   ├── database.py # Database connection
│       │   ├── main.py     # Main application
│       │   ├── models.py   # Database models
│       │   └── schemas.py  # Pydantic schemas
│       └── .env            # Environment variables
├── frontend/               # React frontend
│   └── mcp_frontend/
│       ├── src/
│       │   ├── components/ # React components
│       │   ├── services/   # API services
│       │   ├── types/      # TypeScript types
│       │   └── App.tsx     # Main application
│       └── .env            # Environment variables
└── docker/                 # Docker configuration
    ├── Dockerfile.backend  # Backend Dockerfile
    ├── Dockerfile.frontend # Frontend Dockerfile
    ├── docker-compose.yml  # Docker Compose config
    └── nginx.conf          # Nginx configuration
```

## Setup and Installation

### Prerequisites

- Docker and Docker Compose
- OpenAI API key

### Environment Variables

Create a `.env` file in the backend directory with the following variables:

```
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=postgresql://postgres:postgres@db:5432/mcp
```

### Running with Docker

1. Clone the repository
2. Set up environment variables
3. Build and start the containers:

```bash
cd mcp-slack
docker-compose -f docker/docker-compose.yml up --build
```

4. Access the application at http://localhost:80

### Development Setup

#### Backend

```bash
cd backend/mcp_backend
poetry install
poetry run fastapi dev app/main.py
```

#### Frontend

```bash
cd frontend/mcp_frontend
npm install
npm run dev
```

## Usage

1. Open the application in your browser
2. Start asking questions about the Trast project
3. The AI will provide answers based on the project knowledge base
