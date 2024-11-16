import google.generativeai as genai
import os
import sys

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

if len(sys.argv) < 2:
    print("Usage: python script.py <argument>")
else:
    network_load = sys.argv[1]
    status = sys.argv[2]

# with open('UC_code_to_scan.py', 'r') as file:
#     content = file.read()
# print(content)
response = model.generate_content(f"Deployment status based on network_load is as follows ${status}. Predict what will be the deployment_status when network_load is ${network_load}. Give a one word answer from success or failure.")
print(response.text)

