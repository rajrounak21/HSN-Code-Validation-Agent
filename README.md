# HSN-Code-Validation-Agent

👋 Welcome to the HSN Code Validation Agent — a simple Python command-line tool to validate HSN codes and retrieve their descriptions from an Excel dataset.

---

## Overview

This agent allows users to input an HSN (Harmonized System of Nomenclature) code and checks whether the code exists in the provided dataset (`HSN_SAC.xlsx`). It returns the corresponding description for valid codes or an error message for invalid inputs.

---

## Features

- Validates if the input HSN code is numeric.
- Checks the existence of the HSN code in the dataset.
- Returns the description of the valid HSN code.
- Interactive command-line interface for continuous user inputs.
- Exit option to quit the agent gracefully.

---

## Prerequisites

- Python 3.x
- pandas library

---

## Installation

1. Clone this repository or download the script file.

2. Make sure you have `pandas` installed. If not, install it using pip:
   pip install pandas

3.Ensure the Excel file HSN_SAC.xlsx is in the same directory as the script or provide the correct path to it.
Usage
Run the Python script:

python main.py
You will see the prompt:

👋 Welcome to the HSN Code Validation Agent
Enter an HSN code (or 'exit' to quit):
Enter any numeric HSN code to check its validity and get the description.

Type exit to quit the agent.

Code Explanation
The script loads the HSN data from HSN_SAC.xlsx into a pandas DataFrame.

It cleans the column names and converts the HSNCode column to string for comparison.

The validate_hsn_code function checks:

If the code is numeric.

If it exists in the dataset.

A simple interactive loop allows repeated validation until the user types exit.

Example
Enter an HSN code (or 'exit' to quit): 1001
✅ Valid HSN Code: 1001 - Wheat and meslin

Enter an HSN code (or 'exit' to quit): ABC123
❌ Invalid HSN Code: HSN code must be numeric.

Enter an HSN code (or 'exit' to quit): 9999
❌ Invalid HSN Code: HSN code not found.

Enter an HSN code (or 'exit' to quit): exit
👋 Goodbye!
License
This project is licensed under the MIT License.

Author
Created by [Rounak Raj]
