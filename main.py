import pandas as pd

# Load Excel file
df = pd.read_excel("HSN_SAC.xlsx")
df.columns = df.columns.str.strip()
df['HSNCode'] = df['HSNCode'].astype(str)


def validate_hsn_code(code):
    if not code.isdigit():
        return {"status": "invalid", "error": "HSN code must be numeric."}

    result = df[df['HSNCode'] == code]
    if not result.empty:
        return {"status": "valid", "description": result.iloc[0]['Description']}
    else:
        return {"status": "invalid", "error": "HSN code not found."}


#  Simulate Agent Loop
print("👋 Welcome to the HSN Code Validation Agent")
while True:
    user_input = input("Enter an HSN code (or 'exit' to quit): ").strip()
    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    # Simulate intent recognition (ValidateHSNCode)
    response = validate_hsn_code(user_input)
    if response['status'] == 'valid':
        print(f"✅ Valid HSN Code: {user_input} - {response['description']}")
    else:
        print(f"❌ Invalid HSN Code: {response['error']}")
