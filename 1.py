from pathlib import Path

# Root project directory
root = Path("ai-agent-platform")

# Directories
directories = [
    "app/api/routes",
    "app/agents",
    "app/tools",
    "app/schemas",
    "app/services",
    "tests",
]

# Files
files = [
    "app/__init__.py",
    "app/main.py",

    "app/api/routes/agent.py",

    "app/agents/graph.py",
    "app/agents/state.py",
    "app/agents/nodes.py",

    "app/tools/order_tool.py",
    "app/tools/search_tool.py",
    "app/tools/weather_tool.py",

    "app/schemas/agent.py",

    "app/services/agent_service.py",

    "app/config.py",

    ".env",
    ".env.example",
    ".gitignore",
    ".dockerignore",
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    "README.md",
]


def create_project():
    # Create directories
    for directory in directories:
        path = root / directory
        path.mkdir(parents=True, exist_ok=True)

    # Create files
    for file in files:
        path = root / file
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)

    print(f"Project created successfully: {root.resolve()}")


if __name__ == "__main__":
    create_project()