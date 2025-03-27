import argparse 
from sdk import version,stage,listStagging
name_app = "GPS (Godek Public Server)"
description_app = "Is git version on custom public server yohanes"
# declare

parser = argparse.ArgumentParser(description=description_app,prog=name_app) 
parser.add_argument("-s","--stage",action="store_true",help="stagging perubahan file sebelum push")
parser.add_argument("-l","--list",action="store_true",help="list semua stagging file")
parser.add_argument("-u","--unstage",action="store_true",help="unstagging perubahan yang telah di stagging")
parser.add_argument("-v", "--version", action="store_true",help="melihat version aplikasi")
# parser.add_argument("-p","--push",action="store_true",help="")
parser.add_argument("push",nargs="+")

args = parser.parse_args()
print(args)
# print(args,"\n")

if (parser.parse_args().version):
    # Version
    version()
elif (args.stage):
    # Stagging ( -s )
    stage()
elif (args.list):
    # Listing ( -l )
    listStagging()
elif (args.push):
    print(args)

    # Unstage ( -u )
else:
    parser.print_help()
    # print(args)
