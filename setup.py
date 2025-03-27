import argparse 
from sdk import version,stage,listStagging
name_app = "GPS (Godek Public Server)"
description_app = "Is git version on custom public server yohanes"
# declare

parser = argparse.ArgumentParser(description=description_app,prog=name_app) 
parser.add_argument("-v", "--verbose", action="store_true",help="melihat version aplikasi")
parser.add_argument("-s","--stage",action="store_true",help="stagging perubahan file sebelum push")
parser.add_argument("-l","--list",action="store_true",help="list semua stagging file")
parser.add_argument("-u","--unstage",action="store_true",help="unstagging perubahan yang telah di stagging")

args = parser.parse_args()
# print(args,"\n")

# logic

if (parser.parse_args().verbose):
    version()
elif (args.stage):
    stage()
elif (args.list):
    listStagging()
else:
    parser.print_help()
