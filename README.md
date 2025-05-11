# Document Analysis Agent

An AI-powered document analysis tool leveraging the Claude API to process, analyze, and extract insights from various document types.

![Document Analysis Demo](./examples/document_analysis_demo.png)

## Features

- **Document Loading**: Process PDF, DOCX, and TXT files
- **Intelligent Summarization**: Generate concise summaries of any document
- **Information Extraction**: Extract specific entities like dates, names, and monetary values
- **Question Answering**: Ask specific questions about document content
- **Document Comparison**: Compare two documents and identify similarities and differences

## Technical Architecture

This agent uses a modular architecture:
- Core document processing engine in `app/main.py`
- Streamlit web interface in `interface/web_app.py`
- Claude API for advanced language understanding and generation

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YourUsername/DocumentAnalysisAgent.git
cd DocumentAnalysisAgent
