import os
import requests
from tqdm import tqdm

# Read the API key from the file
with open("/usr/secrets/umls_key.txt", "r") as file:
    api_key = file.read().strip()

base_url = "https://uts-ws.nlm.nih.gov/download"
files_to_download = [
    # "https://download.nlm.nih.gov/umls/kss/2024AB/umls-2024AB-mrconso.zip"
    # ,
    "https://download.nlm.nih.gov/umls/kss/2024AB/umls-2024AB-metathesaurus-full.zip"
]

for file_url in files_to_download:
    file_name = file_url.split("/")[-1]
    full_url = f"{base_url}?url={file_url}&apiKey={api_key}"
    
    if os.path.exists(f'/usr/downloads/{file_name}'):
        overwrite = input(f"{file_name} already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() != 'y':
            print(f"Skipping download for {file_name}")
            continue
    
    try:
        print(f"Starting download for {file_name}...")
        response = requests.get(full_url, stream=True)
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx and 5xx)

        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte

        with open(f'/usr/downloads/{file_name}', "wb") as file, tqdm(
            total=total_size, unit='iB', unit_scale=True
        ) as bar:
            for data in response.iter_content(block_size):
                file.write(data)
                bar.update(len(data))
        print(f"Successfully downloaded {file_name}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Failed to download {file_name}")
    except Exception as err:
        print(f"Other error occurred: {err} - Failed to download {file_name}")