# ATS Resume Checker

A Streamlit app that scores a resume for Applicant Tracking System (ATS) compatibility and suggests concrete improvements, powered by Google's Gemini Flash model.

## Features

- Upload a resume as PDF, DOCX or TXT
- Optionally paste a job description for keyword matching
- Overall ATS score (0-100) with a breakdown: formatting, keywords, content impact, completeness, readability
- Strengths, weaknesses and prioritized improvements
- Missing keywords and rewritten example bullet points
- Download the report as JSON

## Tech stack

- [Streamlit](https://streamlit.io) for the UI
- [Gemini API](https://ai.google.dev) via the `google-genai` SDK (default model: `gemini-2.5-flash`)
- `pypdf` and `python-docx` for reading resumes

## Run locally

```bash
git clone https://github.com/<your-username>/ats-resume-checker.git
cd ats-resume-checker
pip install -r requirements.txt

export GEMINI_API_KEY="your_key"   # Windows PowerShell: $env:GEMINI_API_KEY="your_key"
streamlit run app.py
```

Get a free API key at https://aistudio.google.com/apikey. If no key is set, the app shows a key field in the sidebar.

## Configuration

| Setting | Where | Notes |
|---|---|---|
| `GEMINI_API_KEY` | environment variable or `.streamlit/secrets.toml` | Required |
| `GEMINI_MODEL` | environment variable or sidebar field | Defaults to `gemini-2.5-flash` |

Example `.streamlit/secrets.toml` (never commit this file):

```toml
GEMINI_API_KEY = "your_key"
```

## Deploy on Streamlit Community Cloud

1. Push this repo to GitHub.
2. Go to https://share.streamlit.io, click **Create app**, and select the repo, branch `main`, and main file `app.py`.
3. Under **Advanced settings → Secrets**, add `GEMINI_API_KEY = "your_key"`.
4. Click **Deploy**.

## Limits and notes

- Max file size: 5 MB. Very long resumes are truncated to the first 30,000 characters.
- Scanned or image-only PDFs can't be read; use a text-based PDF or DOCX.
- Resume text is sent to Google's Gemini API for analysis and is not stored by this app.
- The score is an AI estimate, not the output of a real ATS. Use it as guidance.

## Project structure

```
app.py             # Streamlit app
requirements.txt   # Python dependencies
README.md
```
