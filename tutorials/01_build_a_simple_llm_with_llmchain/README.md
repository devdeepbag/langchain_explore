# Tutorial 01: Build a Simple LLM Application with LCEL

This tutorial guides you through building a simple LLM application using LangChain. You'll chain together components like language models, prompt templates, and output parsers using LangChain Expression Language (LCEL). The application translates text from English to another language.

Based on https://github.com/devdeepbag/langchain_explore

## Overview

- **Set Up**: Install dependencies and configure environment variables.
- **Language Models**: Interact with models like OpenAI's GPT.
- **Prompt Templates**: Format user input for the model.
- **LCEL**: Chain components with the `|` operator.
- **Deployment**: Deploy your application with LangServe.

## Files

### `main.py`

This script demonstrates how to create a LangChain-based application that translates text from English to a specified language.

- **How to Run**:
  ```bash
  python3 tutorials/01_build_a_simple_llm_with_llmchain/main.py
  ```
- **Output**: The translated text is displayed in the console.

### `serve.py`

This script sets up a FastAPI server to serve the LangChain application as a REST API using LangServe. It allows you to interact with the translation model through a web interface.

- **How to Run**:
  ```bash
  python3 tutorials/01_build_a_simple_llm_with_llmchain/serve.py
  ```
- **Access**: After running the server, visit [http://localhost:8000/chain/playground/](http://localhost:8000/chain/playground/) to interact with the chatbot.

## Differences

- **`main.py`**: Runs the translation logic directly as a script and outputs the result to the console.
- **`serve.py`**: Deploys the translation logic as a REST API, enabling interaction through a web interface.

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/devdeepbag/langchain_explore.git
    cd langchain_explore/tutorials/01_build_a_simple_llm_with_llmchain
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    Create a `.env` file in the directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## Resources

- [LangChain Documentation](https://python.langchain.com/v0.2/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [LangServe Documentation](https://smith.langchain.com/)

---

Happy coding!
