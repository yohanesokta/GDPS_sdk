import argparse 
from sdk import version
name_app = "GPS (Godek Public Server)"
description_app = "is git version on custom public server yohanes"
# declare

parser = argparse.ArgumentParser(description=description_app,prog=name_app) 
parser.add_argument("-v", "--verbose", action="store_true",help="melihat version aplikasi")
parser.add_argument("stage",action="store_true",help="stagging perubahan file sebelum push")
parser.add_argument('bar',nargs="?",help="BAR!",type=str)
print(parser.parse_args())

if (parser.parse_args().verbose):
    version()
