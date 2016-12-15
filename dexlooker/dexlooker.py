#!/usr/bin/python
#coding=utf-8
import sys
import os
sys.path.append(sys.path[0])
import DexUtil as dexutil

apk_path = sys.argv[1]
os.chdir(sys.path[0])
dexutil.run(apk_path)
