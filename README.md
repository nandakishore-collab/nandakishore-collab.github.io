# CodeMentor AI

**An AI-powered coding mentor that helps beginner programmers understand errors, debug code, and learn programming concepts through clear, step-by-step explanations.**

> **Project status:** Early-stage MVP / learning project. This repository provides a working starter application, not a production-ready product.

## The problem

Beginner programmers often see an error message without understanding what caused it, how to fix it, or how to avoid the same mistake. Copying a solution may remove the immediate error but does not necessarily teach the underlying concept.

## The solution

CodeMentor AI lets a learner submit a code snippet and describe what they are stuck on. It uses an AI model to explain the likely issue in accessible language, suggest a correction, and identify a concept to practise next.

## Current features

- Explain an error or unexpected output.
- Review a code snippet for likely bugs and improvements.
- Explain code line by line or at a high level.
- Ask for an algorithm or problem-solving hint.
- Choose the programming language and the kind of help needed.
- Receive a structured response intended for beginners.
- Keep the API key in an environment variable rather than in source code.

## How it works

1. The learner chooses a help mode and programming language.
2. The learner enters a code snippet and describes the problem.
3. The application builds a focused tutoring prompt.
4. The Anthropic API generates an explanation and suggestions.
5. The response is shown in the Streamlit interface.

**Important:** This MVP sends the submitted code and question to Anthropic's API. Do not submit passwords, API keys, personal data, confidential coursework, or proprietary code unless you have permission to share it with the service.

## Technology stack

- **Python** — application logic
- **Streamlit** — web interface
- **Anthropic Python SDK** — model API client
- **Claude model** — configurable through `ANTHROPIC_MODEL`
- **pytest** — basic automated tests

This is an LLM-powered application. It does not train a custom machine-learning model in this initial version.

## Repository structure

```text
codementor-ai/
├── app.py                     # Streamlit application
├── src/
│   └── codementor/
│       ├── __init__.py
│       └── mentor.py           # Prompt construction and API call
├── tests/
│   └── test_mentor.py         # Unit tests (no API key required)
├── .env.example               # Environment variable template
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- An Anthropic API account and API key for live AI responses
- Internet access when requesting an AI response

API access may incur charges. Check your account's current pricing, usage limits, and any credits before using the application. Credits or startup-program approval are not guaranteed.

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/codementor-ai.git
cd codementor-ai
```

Replace `YOUR_GITHUB_USERNAME` with your GitHub username. If you used a different repository name, update the URL and folder name accordingly.

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure your API key

Copy `.env.example` to `.env`.

**Windows PowerShell:**

```powershell
Copy-Item .env.example .env
```

**macOS / Linux:**

```bash
cp .env.example .env
```

Open `.env` and set your key:

```dotenv
ANTHROPIC_API_KEY=your_real_api_key_here
ANTHROPIC_MODEL=claude-sonnet-4-6
```

Use a model ID currently enabled for your Anthropic account. The model name above is a default example and may need to be changed as model availability evolves.

**Never commit `.env` or publish your API key.** The `.gitignore` file is configured to ignore `.env`.

### 5. Start the application

```bash
streamlit run app.py
```

Streamlit should open the app in your browser. If it does not, open the local URL shown in your terminal (usually `http://localhost:8501`).

## Run tests

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the test suite:

```bash
python -m pytest
```

The unit tests do not make API calls and do not require a real API key.

## Example usage

**Language:** Python  
**Help mode:** Explain an error  
**Code:**

```python
numbers = [1, 2, 3]
print(numbers[3])
```

**Question:** `Why does this fail, and how should I fix it?`

The mentor should explain that Python list indexes start at `0`, so a three-element list has valid indexes `0`, `1`, and `2`. The response should suggest an appropriate fix and explain why it works.

## Responsible use and limitations

- AI explanations can be wrong or incomplete. Verify important suggestions and run tests before relying on them.
- The app does not execute submitted code. It reasons about the code from the prompt and may not reproduce runtime behavior.
- The app currently does not save conversation history or provide user accounts.
- The app requires an Anthropic API key for AI responses; the repository itself does not provide free API access.
- Do not use the tool to submit code you do not have permission to share.
- This prototype does not provide a sandbox for running untrusted code.

## Roadmap

- [ ] Add sample beginner debugging exercises.
- [ ] Add a small set of deterministic checks for common Python errors.
- [ ] Add a feedback button to evaluate the usefulness of explanations.
- [ ] Add optional conversation history with clear privacy controls.
- [ ] Add automated linting and continuous integration.
- [ ] Evaluate response quality using a documented test set.

Roadmap items are planned work, not completed features.

## Contributing

Bug reports, documentation improvements, and well-scoped pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before contributing.

## License

This project is released under the MIT License. See [LICENSE](LICENSE).

## Author

Created as a student AI application project. Replace this line with your name, GitHub profile, and contact details when you are ready to publish them.
