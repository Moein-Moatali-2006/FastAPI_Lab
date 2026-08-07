# Multi-Threaded Download Manager

A simple and lightweight **multi-threaded download manager** built with Python.

This project was developed by **Moein Moatali** as a practical project for learning and applying Python concepts such as HTTP requests, file handling, logging, threading, synchronization, and thread pools.

## Features

* Download files from URLs listed in a text file
* Download multiple files concurrently
* Limit concurrent downloads using `ThreadPoolExecutor`
* Save downloaded files into a dedicated directory
* Handle HTTP errors with `httpx`
* Log download errors into an `Error.log` file
* Automatically create the download directory
* Use `Path` from `pathlib` for file handling

## Technologies

* Python 3
* HTTPX
* `concurrent.futures.ThreadPoolExecutor`
* `threading`
* `logging`
* `pathlib`

## Project Structure

```text
Download_Manager/
│
├── main.py
├── links.txt
├── Error.log
├── downloads/
│   ├── file_0.dat
│   ├── file_1.dat
│   └── ...
└── README.md
```

## How It Works

The application reads download URLs from `links.txt`.

Example:

```text
https://example.com/file1.zip
https://example.com/file2.zip
https://example.com/file3.zip
```

Each URL is submitted as a task to a `ThreadPoolExecutor`.

The number of simultaneous downloads is controlled by:

```python
ThreadPoolExecutor(max_workers=5)
```

This means that at most **5 download tasks** can run concurrently.

When one download finishes, the thread can process another waiting task.

## Installation

Install the required dependency:

```bash
pip install httpx
```

## Usage

Add your file URLs to `links.txt`, one URL per line:

```text
https://example.com/file1.zip
https://example.com/file2.zip
https://example.com/file3.zip
```

Then run:

```bash
python main.py
```

Downloaded files will be stored in:

```text
downloads/
```

For example:

```text
downloads/
├── file_0.dat
├── file_1.dat
└── file_2.dat
```

## Error Logging

Download errors are recorded in `Error.log`.

The project uses Python's built-in `logging` module:

```python
logging.basicConfig(
    level=logging.ERROR,
    filename="Error.log",
    encoding="utf-8"
)
```

This allows failed requests and HTTP errors to be recorded in a log file.

## Concurrency

The project uses `ThreadPoolExecutor` to manage multiple download tasks concurrently.

Example:

```python
with ThreadPoolExecutor(max_workers=5) as executor:
    for i, url in enumerate(urls):
        save_file_path = DOWNLOAD_DIR / f"file_{i}.dat"

        executor.submit(
            download_file,
            url,
            save_file_path,
            30
        )
```

Using a thread pool prevents the application from creating an unlimited number of threads when many URLs are provided.

## Learning Goals

This project was created to practice:

* Working with HTTP requests
* Downloading files with Python
* Reading and processing text files
* Using `pathlib`
* Exception handling
* Logging errors
* Working with threads
* Understanding synchronization with `Lock`
* Understanding `ThreadPoolExecutor`
* Managing concurrent tasks

## Future Improvements

Possible improvements for future versions include:

* Progress bars for downloads
* Download speed calculation
* File size detection
* Automatic filename extraction from URLs
* Resume interrupted downloads
* Retry failed downloads
* Configurable number of workers
* Download status tracking
* Command-line arguments
* Asynchronous downloading with `asyncio` and `httpx.AsyncClient`
* Graphical User Interface

## Author

**Moein Moatali**

Software Engineering Student & Programmer

Email: **[MoeinMoatali@gmail.com](mailto:MoeinMoatali@gmail.com)**

+98 9030813097

---

Made with Python by **Moein Moatali**.
