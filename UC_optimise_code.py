import google.generativeai as genai
import os
import sys
import requests

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")


with open('UC_code_to_scan.py', 'r') as file:
    content = file.read()
print(content)
genai_response = model.generate_content(f"Below given is a python code. Optimise the code.\n {content} \n Add this string at the begining of response - Optimised code is")

SONARQUBE_CREDS = sys.argv[1]

url = "http://9.46.241.25:9000/api/project_branches/list?project=SmpleApp"
headers = {'Authorization': f'Basic {SONARQUBE_CREDS}'}

sonarqube_response = requests.get(url, headers=headers)
print(response.text)


with open('/tmp/code_optimisations.txt', 'w') as file:
    file.write(genai_response.text + '\n\n')
    file.write(sonarqube_response.text)
