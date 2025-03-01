# Code Review LLM

## Overview
This project is a simple **code review application** using **Coder LLM** models to analyze and improve Python code. The app provides feedback, suggests improvements, and enhances readability and maintainability. It then translates the review results into **Korean** and displays them using **Streamlit**.

## Features
- **Code Review:** Uses **LLM models** to analyze Python code and provide suggestions.
- **Translation:** Automatically translates review results into Korean using **DeepL API**.
- **User Interface:** Built with **Streamlit** for an interactive experience.

## Technologies Used
- **Python**
- **Streamlit**
- **Ollama** (for LLM-powered code review)
- **OpenAI API** (for translation, optional)
- **DeepL API** (for high-quality translations)

## Installation
### 1. Clone the Repository
```bash
$ git clone https://github.com/yourusername/code-review-llm.git
$ cd code-review-llm
```

### 2. Install Dependencies
```bash
$ pip install -r requirements.txt
```

### 3. Set API Keys
Ensure you have the required API keys for **OpenAI** and **DeepL**.
```bash
export OPENAI_API_KEY="your_openai_api_key"
export DEEPL_API_KEY="your_deepl_api_key"
```

## Usage
### Running the Streamlit App
```bash
$ streamlit run app.py
```

### Running Code Review from CLI
```bash
$ python code_review_llm.py <your_python_file>
```

## Project Structure
```
.
├── app.py                   # Streamlit UI for code review
├── code_review_llm.py        # Core logic for LLM-based code review and translation
├── requirements.txt          # Required Python packages
├── README.md                 # Project documentation
```

## Supported LLM Models
- **yi-coder:1.5b**
- **qwen2.5-coder**
- **deepseek-coder:6.7b-instruct**

## Contributing
Feel free to fork this repository, create a branch, and submit a pull request with your improvements!

## License
This project is licensed under the MIT License.

