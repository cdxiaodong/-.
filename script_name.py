import os
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor

# 创建目标文件夹
def create_dirs(file_path):
    dir_path = os.path.join('source', os.path.dirname(file_path.lstrip('/')))
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return os.path.join('source', file_path.lstrip('/'))

# 下载文件
def download_file(file_path, url_template):
    url = url_template.replace('$$', file_path)
    local_path = create_dirs(file_path)
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果请求失败，抛出异常
        with open(local_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {file_path} to {local_path}")
    except requests.RequestException as e:
        print(f"Failed to download {file_path}: {e}")

# 读取文件路径并下载
def download_files_from_list(url_template, file_list_path):
    with open(file_list_path, 'r') as f:
        file_paths = [line.strip() for line in f.readlines()]

    with ThreadPoolExecutor(max_workers=5) as executor:
        for file_path in file_paths:
            executor.submit(download_file, file_path, url_template)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download files from a list of paths using a URL template.')
    parser.add_argument('url_template', type=str, help='The URL template with $$ as a placeholder for file paths.')
    parser.add_argument('file_list_path', type=str, help='The path to the file containing the list of file paths.')
    
    args = parser.parse_args()

    download_files_from_list(args.url_template, args.file_list_path)
