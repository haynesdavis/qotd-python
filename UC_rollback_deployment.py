import google.generativeai as genai
import os
import sys


genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

if len(sys.argv) < 2:
    print("Usage: python script.py <argument>")
else:
    cpu_load = sys.argv[1]
    actual_response = sys.argv[2]

    print(f"Arguments passed: {cpu_load}, {actual_response}")

# print(f"There are two conditions to check if app failed on deployment. App is failed when cpu_load is 1. App is failed when actual_response is not similar to expected_response. Their values are cpu_load={cpu_load},  actual_response={actual_response} and expected_response={expected_response}. You should infer if app is running or not from these values. Reply False when app is not running. Do not reply code. Give an answer from True or False.")
response = model.generate_content(f"There are two conditions to check if app failed on deployment. App is failed when cpu_load is 1. App is failed when actual_response has the word fail or similar meaning word in it. Their values are cpu_load={cpu_load}. actual_response is {actual_response}. Reply True when app is running and False when app is not running. Do not reply code. Give an answer from True or False.")
print(response.text)

