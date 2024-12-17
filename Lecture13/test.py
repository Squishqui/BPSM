#!/usr/bin/python3

tester = open("sliding_windows.py")
count = 0

for eachline in tester.readlines():
    count +=1
    line_length=len(eachline.rstrip("/n"))
    print("we are processing line "+str(count)+" of the file")
    print("there are "+str(line_length)+" characters on the line")

tester.close()
