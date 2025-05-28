# 🔍 HSN-Code-Validation-Agent

A Streamlit-powered web tool to validate Indian **HSN (Harmonized System of Nomenclature)** codes using a local Excel dataset and a Google ADK Agent (Gemini 2.0 Flash).

---

## 📁 Project Structure

```
HSN-Code-Validation-Agent/
├── main.py            # Streamlit app interface
├── hsn_agent.py       # Validation logic + Google ADK Agent
├── __init__.py        # Package initializer
├── .env               # Environment variables (e.g., API keys)
├── HSN_SAC.xlsx       # HSN codes dataset (not included in repo)
```

---

## 🚀 Features

* ✅ Validates numeric HSN codes from the official dataset
* 🧠 Uses Google ADK agent with Gemini 2.0 Flash
* 💾 Local Excel dataset for offline-first behavior
* 🌐 Simple web interface via Streamlit

---

## 🔐 Environment Variables

This project uses a `.env` file to store sensitive configuration values like API keys.

Create a `.env` file in the project root with content like:

```
GOOGLE_API_KEY=your-google-api-key-here
```

> The `.env` file is **not committed to version control** for security reasons. You must manually create it.

Make sure you load the environment variables in your Python script using:
## 📦 Installation

Install required dependencies:

```
pip install streamlit pandas google-generativeai python-dotenv google-adk
```

---

## ▶️ Running the App

```
streamlit run main.py
```

Ensure the following before running:

* `HSN_SAC.xlsx` is present in the root directory
* `.env` contains a valid `GOOGLE_API_KEY`

---

## 💡 Example Usage

### ✅ Valid Input

```
Input: 1001
Output: ✅ HSN Code 1001: Wheat and meslin
```

### ❌ Invalid Input

```
Input: ABC123
Output: ❌ Invalid HSN code: must be numeric.
```

---

## 🤖 Agent Description

A Gemini-powered agent (`hsn_code_validator`) responds with:

* ✅ HSN Code `<code>`: `<description>`
* ❌ Invalid HSN code: `<reason>`

---

## 📝 License

This project is intended for educational and prototype use.

---

## 👤 Author

Created by \[Rounak raj]. Contributions and feedback welcome!

This project is licensed under the MIT License.

Author
Created by [Rounak Raj]
