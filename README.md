# AI Travel Planner

An AI-powered travel planning application built with Python, LangGraph, and Streamlit. The application uses AI agents and external tools to assist users with travel research and itinerary planning.

## Features

- AI-assisted travel planning and recommendations.
- Flight information retrieval using the Aviationstack API.
- Web research using Tavily.
- AI agent orchestration using LangGraph.
- Interactive web interface built with Streamlit.
- Travel plans saved as Markdown files.

## Tech Stack

- **Python** – Core programming language.
- **LangGraph** – AI agent orchestration and workflow management.
- **Streamlit** – Interactive web application interface.
- **Aviationstack API** – Flight information.
- **Tavily** – Web search and research.
- **Requests** – HTTP requests to external APIs.
- **Python-dotenv** – Environment variable management.

## Project Structure

```text
ai-travel-planner/
│
├── tools/
│   ├── flight_tool.py
│   └── tavily_tool.py
│
├── travel_plans/
│
├── frontend.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/cceebb/ai-travel-planner.git
cd ai-travel-planner
```

### 2. Create a virtual environment

```bash
python -m venv langgraph_env
```

### 3. Activate the virtual environment

**Windows:**

```bash
langgraph_env\Scripts\activate
```

**macOS / Linux:**

```bash
source langgraph_env/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the root directory and add the required API keys:

```env
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Replace the placeholder values with your own API keys.

**Important:** Never commit or upload your `.env` file or expose your API keys publicly.

### 6. Run the application

```bash
streamlit run frontend.py
```

The application will open in your browser, usually at `http://localhost:8501`.

## Environment Variables

| Variable | Description |
|---|---|
| `AVIATIONSTACK_API_KEY` | API key for retrieving flight information |
| `TAVILY_API_KEY` | API key for web search and research |

## Security

- API keys are stored in a local `.env` file.
- Sensitive environment files are excluded through `.gitignore`.
- Never share API keys in source code or public repositories.

## Author

**GitHub:** [@cceebb](https://github.com/cceebb)

## License

No open-source license has been added yet. All rights are reserved by the author unless a license is added.