# AI Agents Portfolio

A collection of specialized AI agents built to demonstrate practical
applications of large language models for business process optimization.
Each agent serves a specific business function and leverages Claude API
for advanced natural language understanding and generation.

## Overview

This portfolio showcases my expertise in:
- Building practical AI applications for business use cases
- Leveraging large language models (specifically Claude) for task
automation
- Developing web-based interfaces for AI tools using Streamlit
- Implementing a structured project layout for multiple agents

## Agents

### Document Analysis Agent
Process, analyze, and extract insights from business documents with
intelligent summarization, information extraction, and question answering
capabilities.

[View Project](main.py)

### Data Analysis Agent
Analyze datasets, generate statistical insights, and create visualizations
with AI-powered interpretation and recommendations.

[View Project](data_analysis_agent/app.py)

## Project Structure

This repository is organized into two main agents:

-   **Document Analysis Agent:**
    -   Entry point: `main.py`
    -   Core logic: `app/core.py`
-   **Data Analysis Agent:**
    -   Entry point: `data_analysis_agent/app.py`
    -   Core logic: `data_analysis_agent/core.py`

Shared configurations like `requirements.txt` and `.env.example` are in the root directory.

## Setup and Running

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up API Key:**
    -   Rename `.env.example` to `.env`.
    -   Open `.env` and replace `your_api_key_here` with your actual Anthropic API key:
        ```
        ANTHROPIC_API_KEY=sk-ant-your-api-key
        ```

5.  **Run an Agent:**
    -   **To run the Document Analysis Agent:**
        ```bash
        streamlit run main.py
        ```
    -   **To run the Data Analysis Agent:**
        ```bash
        streamlit run data_analysis_agent/app.py
        ```

## Technologies Used

- Python 3.8+
- Anthropic Claude API
- Streamlit (for web interfaces)
- Pandas, Matplotlib, Seaborn (for data analysis)
- PyPDF, NLTK (for document processing)

## Contact

Feel free to reach out with any questions or collaboration opportunities:

- Email: [your-email@example.com]
- LinkedIn: [Your LinkedIn Profile]
