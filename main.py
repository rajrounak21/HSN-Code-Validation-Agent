import streamlit as st
from hsn_agent import validate_code  # adjust import based on your structure

st.set_page_config(page_title="HSN Validator", page_icon="🔍")
st.title("🔍 HSN Code Validator")
st.markdown("Enter an **HSN Code** to validate and get its description.")

code_input = st.text_input("HSN Code", "")

if st.button("Validate"):
    if code_input:
        response = validate_code(code_input.strip())
        if isinstance(response, str):
            if response.startswith("✅"):
                st.success(response)
            else:
                st.error(response)
        else:
            st.error("Unexpected response type.")
    else:
        st.warning("Please enter an HSN code.")


