import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")


with open('UC_code_to_scan.py', 'r') as file:
    content = file.read()
print(content)
response = model.generate_content(f"Below given is a python code. Build test casefor this code.\n {content} \n Response should have only code. Module to import is code_to_scan")
print("Unit test cases generated are ----")
print(response.text)
code=response.text
lines = code.split('\n')
lines = [line for line in lines if '```' not in line]
filtered_code = '\n'.join(lines)
print(filtered_code)
# Open file in write mode
with open("/tmp/test_case.py", "w") as file:
    file.write(f"{filtered_code}")
