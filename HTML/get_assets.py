
import os
import requests

def download_file(url, path):
    '''download a file from a given url and store it in the path provided
    '''
    # retrieve the file from the url
    r = requests.get(url, stream=True)
    # save the file in the provided path
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

# provide the url and the path to store the file

def explore_files_in_folders(path):
    '''explore all the files in all folders of a given path
    '''
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            a=full_path
            file_path = a[a.find("path")+len(path):]
            url = "https://finapp.bragherstudio.com/view22/assets/" + file_path
            download_file(url,path+file_path)
            print(full_path+" - > "+url)

# provide the path to the directory to explore
explore_files_in_folders("/Users/sezzerouali/Downloads/Finapp v2.2/HTML/assets/")
