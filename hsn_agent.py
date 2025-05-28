from google.adk import Agent
import pandas as pd

# Load Excel
df = pd.read_excel("HSN_SAC.xlsx")
df.columns = df.columns.str.strip()
df['HSNCode'] = df['HSNCode'].astype(str)


def validate_code(code: str) -> str:
    if not code.isdigit():
        return "❌ Invalid HSN code: must be numeric."

    result = df[df['HSNCode'] == code]
    if not result.empty:
        return f"✅ HSN Code {code}: {result.iloc[0]['Description']}"
    else:
        return "❌ Invalid HSN code: not found in database."


# The ADK Agent just uses instruction-based prompting (no tools or functions)
agent = Agent(
    name="hsn_code_validator",
    model="gemini-2.0-flash-exp",
    description="Validates Indian HSN codes and provides their description.",
    instruction=f"""
        You are an HSN Code Validator Agent.

        When the user sends an HSN code, you will check if it exists in the dataset,
        and return the description if found.

        Only respond with:
        - ✅ HSN Code <code>: <description>
        - ❌ Invalid HSN code: <reason>

        Use the dataset below:

        {df.to_string(index=False)}
    """
)
