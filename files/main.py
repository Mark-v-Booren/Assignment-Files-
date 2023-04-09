__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import zipfile
import re

zip_path = 'c:\\Winc\\files\\data.zip'
cache_dir_path = 'c:\\Winc\\files\\cache'


def clean_cache():

    if not os.path.exists(cache_dir_path):
        os.makedirs(cache_dir_path)
    for f in os.listdir(cache_dir_path):
        os.remove(os.path.join(cache_dir_path, f))
    return ''


def cache_zip(zip_path, cache_dir_path):

    if not os.path.exists(cache_dir_path):
        os.makedirs(cache_dir_path)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)
    return ''


def cached_files():
    cache_dir_path = os.path.abspath(os.path.join(
        'C:\\', 'Winc', 'files', 'cache'))
    file_names = os.listdir(cache_dir_path)
    file_names = [f for f in file_names if os.path.isfile(
        os.path.join(cache_dir_path, f))]
    file_paths = [os.path.join(cache_dir_path, f) for f in file_names]
    return file_paths


def find_password(cached_files):
    search_password = re.compile(r'password:\s*(\w+)')
    for file_path in cached_files:
        with open(file_path, 'r') as f:
            contents = f.read()
            match = search_password.search(contents)
            if match:
                return match.group(1)


print(clean_cache())
print(cache_zip(zip_path, cache_dir_path))
print(cached_files())
print(find_password(cached_files()))
