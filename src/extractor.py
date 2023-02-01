import os
import openai
import requests
from login import API_KEY


def main():
    id = "MED/36104476/"

    r = requests.get(
        f"https://www.ebi.ac.uk/europepmc/webservices/rest/article/{id}?resultType=core&format=json"
    )

    data = r.json()

    abstract_text = data["result"]["abstractText"]
    print(abstract_text)
    cells = extract_cells_from_text(text=abstract_text, API_KEY=API_KEY)
    print(cells)


def extract_cells_from_text(text, API_KEY):
    openai.api_key = API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'Extract all cell types present in the following text:\n Text: "{text}" Cell types:',
        temperature=1.0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"],
    )

    return [a.strip() for a in response["choices"][0]["text"].split(",")]


if __name__ == "__main__":
    main()
