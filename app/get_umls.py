import requests

# Read the API key from the file
with open("/usr/secrets/umls_key.txt", "r") as file:
    api_key = file.read().strip()

base_url = "https://uts-ws.nlm.nih.gov/download"
files_to_download = [
    "https://download.nlm.nih.gov/umls/kss/2024AB/MRCONSO.RRF",
    "https://download.nlm.nih.gov/umls/kss/2024AB/MRSTY.RRF"
]

for file_url in files_to_download:
    file_name = file_url.split("/")[-1]
    response = requests.get(f"{base_url}?url={file_url}&apiKey={api_key}")

    with open(file_name, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {file_name}")