__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import zipfile
import re

base_path = os.getcwd()

zip_path = os.path.join(base_path, 'files', 'data.zip')
cache_dir_path = os.path.join(base_path, 'files', 'cache')


def clean_cache():

    if os.path.isdir(cache_dir_path):
        for f in os.listdir(cache_dir_path):
            file_path = os.path.join(cache_dir_path, f)
            if os.path.isdir(file_path):
                os.rmdir(file_path)
            else:
                os.remove(file_path)
    else:
        os.mkdir(cache_dir_path)


def cache_zip(zip_path, cache_dir_path):

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)


def cached_files():

    file_names = os.listdir(cache_dir_path)
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
