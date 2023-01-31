import os
import openai
import requests
from login import API_KEY

openai.api_key = API_KEY
id = "MED/36104476/"

r = requests.get(
    f"https://www.ebi.ac.uk/europepmc/webservices/rest/article/{id}?resultType=core&format=json"
)

data = r.json()

abstract_text = data["result"]["abstractText"]
print(abstract_text)
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f'Extract all cell mentions in the following text:\n Text: "{abstract_text}" Cell types:',
    temperature=1,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"],
)

print([a.strip() for a in response["choices"][0]["text"].split(",")])
