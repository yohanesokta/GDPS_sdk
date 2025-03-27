import os
import zipfile
from datetime import datetime
from sdk.config import config
from sdk.config import filename

folder = "./.gdps"
path = "."


def createFolder():
    os.makedirs(folder,exist_ok=True)
    os.makedirs(folder+"/compress",exist_ok=True)


def compressingFiles():
    zipfile_name = f"stagging_{str(datetime.now())}.zip"
    with zipfile.ZipFile(folder + "/compress/" +  zipfile_name,"w",zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(path):
            skip_dir = False
            for dir_ignore in config.ignore():
                if (dir_ignore in root and root != "." and dir_ignore != " "):
                    skip_dir = True
                    break
            if (skip_dir or f"{folder}/compress" in root):
                continue
            for file in files:
                if (file != zipfile_name and (file not in config.ignore())):
                    file_path = os.path.join(root,file,)
                    zipf.write(file_path,os.path.relpath(file_path,path))

    config.update_stagging(zipfile_name)


def stage():
    createFolder()
    # jika kamu gl punya folder gps 
    # (sans aja kalau ada gk ke replace kok)
    print(" - stage")
    print(" - compressing files %")
    compressingFiles()
    print(" - stagging ready")

def listStagging():
    print(f"\nListing on {filename}\n<-------------------------->")
    if(config.stagging()):
        iterable = 1
        for data in config.stagging():
            print(iterable,">",data.split("_")[1].split(".")[0])
            iterable += 1
        print("")
    else:
        print("gak pernah stagging sama sekali!\n")