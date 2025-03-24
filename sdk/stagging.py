import os
import zipfile
folder = "./.gps"
path = "."


def createFolder():
    os.makedirs(folder,exist_ok=True)

def compressingFiles():
    zipfile_name = "compressioncode.zip"
    with zipfile.ZipFile(folder + "/" +  zipfile_name,"w",zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(path):
            for file in files:
                if (file != zipfile_name):
                    # print(root)
                    file_path = os.path.join(root,file,)
                    zipf.write(file_path,os.path.relpath(file_path,path))
    with open("./.gpsignore") as file:
        print(file.read().split(" ")[0].split("\n"))

def stage():
    createFolder()
    # jika kamu gk punya folder gps (sans aja kalau ada gk ke replace)
    print(" - stage")
    print(" - compressing files %")
    compressingFiles()
