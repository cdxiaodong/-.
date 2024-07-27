### README

# Arbitrary File Read Exploit Downloader

This script is designed to exploit arbitrary file read vulnerabilities by downloading files from a list of paths using a URL template. It supports multithreading to download multiple files simultaneously and saves them in a structured directory based on their original paths.

## Features
- Multithreaded file downloading.
- Dynamic URL template with placeholders.
- Creates directory structure based on file paths.
- Command-line interface with argument parsing.

## Requirements
- Python 3.6+
- `requests` library

## Installation
1. Clone the repository or download the script:
    ```bash
    git clone https://github.com/yourusername/arbitrary-file-read-exploit-downloader.git
    cd arbitrary-file-read-exploit-downloader
    ```
2. Install the required Python libraries:
    ```bash
    pip install requests
    ```

## Usage
1. Create a file containing the list of file paths you want to download (e.g., `file.txt`):
    ```
    /etc/passwd
    /etc/hosts
    /var/log/syslog
    ```
2. Run the script with the URL template and the path to the file list as arguments:
    ```bash
    python script_name.py "http://example.com/?file=$$" file.txt
    ```
   Replace `script_name.py` with the actual name of your script file.

3. You can also get help information by running:
    ```bash
    python script_name.py -h
    ```

### Example
```bash
python script_name.py "http://example.com/?file=$$" file.txt
```

### Output
The downloaded files will be saved in a directory named `source`, maintaining the structure of their original paths. For example, downloading `/etc/passwd` will save the file to `source/etc/passwd`.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

### LICENSE

MIT License

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
