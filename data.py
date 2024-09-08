Data Fetcher & Processor
Informasi
Data Fetcher & Processor adalah skrip Python yang dirancang untuk mengambil data dari API, memproses data tersebut menjadi format terstruktur menggunakan pandas, dan menyimpan hasilnya ke dalam file JSON. Skrip ini berguna untuk mengautomasi proses pengambilan data dan menyimpannya dalam format yang mudah diproses lebih lanjut.

Fitur Utama:
Mengambil data dari endpoint API menggunakan requests.
Memproses data mentah menjadi DataFrame pandas.
Menyimpan DataFrame ke dalam file JSON yang terstruktur dengan baik.
Cara Penggunaan
Instalasi Dependencies

Pastikan Anda memiliki Python terinstal di sistem Anda. Skrip ini memerlukan beberapa paket Python yang dapat diinstal menggunakan pip. Install dependencies berikut dengan menjalankan perintah:

bash
Salin kode
pip install requests pandas
Konfigurasi

Sesuaikan skrip dengan URL API Anda dan nama file output yang diinginkan. Edit variabel API_URL dan OUTPUT_FILE di skrip utama:

python
Salin kode
API_URL = "https://api.example.com/data"  # Ganti dengan URL API Anda
OUTPUT_FILE = "data_output.json"
Menjalankan Skrip

Setelah konfigurasi selesai, jalankan skrip dengan perintah berikut:

bash
Salin kode
python script_name.py
Gantilah script_name.py dengan nama file skrip Anda.

Memeriksa Output

Setelah skrip selesai dijalankan, file output data_output.json akan berisi data yang telah diproses dalam format JSON.

Contoh Skrip
Berikut adalah skrip lengkap untuk pengambilan dan pemrosesan data:

python
Salin kode
import requests
import pandas as pd
import json
from typing import List, Dict

def fetch_data(api_url: str) -> Dict:
    """Fetch data from an API endpoint."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return {}

def process_data(data: Dict) -> pd.DataFrame:
    """Process raw data into a structured DataFrame."""
    if not data:
        return pd.DataFrame()

    # Assuming the data is a list of records
    records = data.get('results', [])
    return pd.DataFrame(records)

def save_to_json(df: pd.DataFrame, file_path: str) -> None:
    """Save DataFrame to a JSON file."""
    df.to_json(file_path, orient='records', lines=True)
    print(f"Data saved to {file_path}")

def main(api_url: str, output_file: str) -> None:
    """Main function to fetch, process, and save data."""
    data = fetch_data(api_url)
    df = process_data(data)
    if not df.empty:
        save_to_json(df, output_file)
    else:
        print("No data to save.")

if __name__ == "__main__":
    API_URL = "https://api.example.com/data"  # Ganti dengan URL API Anda
    OUTPUT_FILE = "data_output.json"
    main(API_URL, OUTPUT_FILE)
Lisensi
Skrip ini dilisensikan di bawah MIT License. Silakan lihat file LICENSE untuk detail lebih lanjut.
