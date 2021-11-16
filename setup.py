import os
from os import system,rename
import glob
venv = glob.glob('*/bin/activate')
if venv:
    system(f"source {venv[0]}")
else:
    system("python3 -m venv venv")
    system("source venv/bin/activate")

system("pip install -r requirements.txt")
proj_name = input("enter project name: ")
os.chdir('../')
rename("drfTemplate", rf'{proj_name}')
os.chdir(rf'{proj_name}')

