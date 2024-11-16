import google.generativeai as genai
import os
import sys

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")


with open('UC_code_to_scan.py', 'r') as file:
    content = file.read()
print(content)
response = model.generate_content(f"Below given is a python code. Optimise the code.\n {content} \n Add this string at the begining of response - Optimised code is")
print(response.text)

SONARQUBE_CREDS = sys.argv[1]
sonarqube_status=$(curl -H "Authorization: Basic $SONARQUBE_CREDS" "http://9.46.241.25:9000/api/project_branches/list?project=SmpleApp")
print(sonarqube_status)

with open('code_optimisations.txt', 'w') as file:
    file.write(response.text)
