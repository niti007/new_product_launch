# Product Analysis Dashboard

A Streamlit-based application that performs comprehensive product analysis using AI agents powered by CrewAI and LangChain. The application generates detailed reports covering market research, technological assessment, and business analysis for any given product.

## Features

- Market demand analysis and marketing strategy recommendations
- Technical feasibility assessment and manufacturing requirements
- Business model evaluation with scalability analysis and revenue projections
- Real-time analysis using AI agents with different expertise
- Interactive web interface built with Streamlit

## Prerequisites

- Python 3.8+
- Streamlit
- CrewAI
- LangChain
- Groq API key
- Serper API key for web search capabilities

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with:
```
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

## Project Structure

```
├── backend/
│   ├── agents.py    # Contains ProductAnalysisAgents class
│   └── tasks.py     # Contains Productanalysistask class
├── app.py           # Main Streamlit application
├── requirements.txt
└── README.md
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Enter a product name in the input field

3. Click "Analyze Product" to generate reports

The application will generate three reports:
- Market Research Report
- Technology Assessment Report
- Business Analysis Report

## Features in Detail

### Market Research Analysis
- Target audience identification
- Market demand assessment
- Marketing strategy recommendations
- Competition analysis

### Technology Assessment
- Manufacturing requirements
- Technical feasibility analysis
- Required technologies evaluation
- Production approach recommendations

### Business Analysis
- Scalability assessment
- Revenue stream identification
- Business model evaluation
- Product launch timeline
- Goals and milestones

