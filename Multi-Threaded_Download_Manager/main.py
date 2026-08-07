import httpx
import logging
from pathlib import Path
from threading import Lock, current_thread
from concurrent.futures import ThreadPoolExecutor


# Config
DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

logging.basicConfig(level=logging.ERROR, filename="Error.log", encoding="utf-8")

with open("links.txt", "r", encoding="utf-8") as file:
    urls = [line.strip() for line in file]

lock = Lock()

# Function for downloading file
def download_file(url: str, save_path: Path, timeout: int) -> bool:
    try:
        response = httpx.get(url, timeout=timeout)
        response.raise_for_status()

        path = Path(save_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(response.content)
        return True
    except httpx.HTTPError as e :
        with lock:
            logging.error(f"{e} - {current_thread().name}")
        return False


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor: 
        for i, url in enumerate(urls):
            save_file_path = DOWNLOAD_DIR / f"file_{i}.dat"
            executor.submit(download_file, url, save_file_path, 30)
            
        
        

   