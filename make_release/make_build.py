#!/usr/bin/python -O
# -*- coding: UTF-8 -*-

import os
import sys
import re

keil_path = r'D:\Keil_v5\UV4'
sys.path.append(keil_path)
path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
target_path = path + "/Src/Template/USER/Template.uvproj"

def build(target_filename, mode):
    if mode != r'Release':
        mode = "Debug"
    build_output_filename = mode + "_Build_Output.txt"
    build_command = "UV4.exe -r %s -o %s -t %s" % (target_filename, build_output_filename, mode)
    print(build_command+"\n")
    os.system(build_command)

def print_file(output_file):
    for line in open(output_file):
        print(line)

def extractData(regex, content): 
    for line in open(output_file):
        matchObj = re.search(regex, line, re.M|re.I)
        if matchObj:
            print(line)


if __name__ == '__main__':
  
    cmd = sys.argv[1]

    if (cmd == "r" or cmd == "release" or cmd == "Release"):
        mode = "Release" 
    elif (cmd == "d" or cmd == "debug" or cmd == "Debug"):
        mode = "Debug" 
    else:
        print("command error")
        print("must input cmd: d/debug/Debug or r/release/Release")
        sys.exit()

    if (os.path.exists(target_path)):
        build(target_path, mode)
    else:
        print("target file do not exist")

    output_file = path + "/Src/Template/USER/" + mode + "_Build_Output.txt"

    if (os.path.exists(output_file)):
        print("read build output file...\n")
        # print_file(output_file)
        extractData('Error',output_file)
        # extractData('warning',output_file)
    else:
        print(output_file + "is not exists")
