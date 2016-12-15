#!/usr/bin/python
# coding=utf-8
import zipfile
import os
import os.path
import shutil

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEX2JAR_DIR = ROOT_DIR + "/dex2jar"
JD_GUI_DIR = ROOT_DIR + "/JD-GUI.app"


def run(apk_path):
    print("starting...")
    unzip_dir = unzip_apk(apk_path)
    copy_dir = DEX2JAR_DIR + "/dex/"
    mk_and_clean_dir(copy_dir)
    copy_dex_to_dir(unzip_dir, copy_dir)
    del_all_jar(DEX2JAR_DIR)
    dex2jar(DEX2JAR_DIR)
    open_all_jar(DEX2JAR_DIR)


# 解压apk
def unzip_apk(path):
    print("start unzip apk...")
    unzip_dir = os.path.splitext(path)[0]
    mk_and_clean_dir(unzip_dir)
    zipfile.ZipFile(path, "r").extractall(unzip_dir)
    print("unzip finish")
    return unzip_dir


# 复制dex文件到指定目录下
def copy_dex_to_dir(source_dir, target_dir):
    print("start copy dex...")
    list = os.listdir(source_dir)
    for line in list:
        filepath = os.path.join(source_dir, line)
        if not os.path.isdir(filepath) and filepath.find('.dex') > 0:
            shutil.copy(filepath, target_dir)
        elif os.path.isdir(filepath):
            copy_dex_to_dir(filepath,target_dir)

    print("copy finish")


def mk_and_clean_dir(dir):
    print("clean " + dir + "...")
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)
    print("clean finish")


def dex2jar(dex2jar_dir):
    print("start dex to jar...")
    os.chdir(dex2jar_dir)

    dex_dir = dex2jar_dir + "/dex/"
    list = os.listdir(dex_dir)
    i = 0
    for line in list:
        filepath = os.path.join(dex_dir, line)
        if not os.path.isdir(filepath) and filepath.find('.dex') > 0:
            filename = os.path.basename(filepath)
            os.system("./d2j-dex2jar.sh ./dex/" + filename)
    os.chdir(ROOT_DIR)
    print("dex2jar finish")


# 利用JD_GUI 打开jar
def open_all_jar(dir):
    print("start open jar...")
    list = os.listdir(dir)
    for line in list:
        filepath = os.path.join(dir, line)
        if not os.path.isdir(filepath) and filepath.find('.jar') > 0:
            os.system("open -a " + JD_GUI_DIR + " " + filepath)


def del_all_jar(dir):
    print("start delete jar...")
    list = os.listdir(dir)
    for line in list:
        filepath = os.path.join(dir, line)
        if not os.path.isdir(filepath) and filepath.find('.jar') > 0:
            os.remove(filepath)
    print("delete finish")
