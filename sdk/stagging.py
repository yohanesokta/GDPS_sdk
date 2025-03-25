import os
import zipfile
from datetime import datetime
from sdk.config import config

folder = "./.gps"
path = "."


def createFolder():
    os.makedirs(folder,exist_ok=True)

def compressingFiles():
    
    zipfile_name = f"stagging_{str(datetime.now())}.zip" 
    with zipfile.ZipFile(folder + "/" +  zipfile_name,"w",zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(path):
            skip_dir = False
            for dir_ignore in config.ignore():
                if (dir_ignore in root and root != "." and dir_ignore != " "):
                    skip_dir = True
                    break
            if (skip_dir):
                continue
            for file in files:
                if (file != zipfile_name and (file not in config.ignore())):
                    file_path = os.path.join(root,file,)
                    zipf.write(file_path,os.path.relpath(file_path,path))


def stage():
    createFolder()
    # jika kamu gk punya folder gps (sans aja kalau ada gk ke replace)
    print(" - stage")
    print(" - compressing files %")
    compressingFiles()
