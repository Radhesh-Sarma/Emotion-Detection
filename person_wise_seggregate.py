
import os
basepath = 'OpenFace__personwise_raw'
from shutil import move
from utils import *
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
ss = set([])

for i in os.listdir(basepath):
    person_id = str(i[0] + i[1] + i[2] + i[3])
    print(str(BASE_DIR) + '/' + basepath + '/' + i)
    move(str(BASE_DIR) + '/' + basepath + '/' + i,str(BASE_DIR) + '/' + basepath + '/' + person_id + '/')
