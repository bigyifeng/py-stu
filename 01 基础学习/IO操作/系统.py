import os
import pickle

print(os.name)
pathList = os.environ.get("Path").split(";")

print(os.path.abspath("."))

testPath = os.path.join("./file/demo.txt")
try:
    os.rename(testPath, "./file/demo2.txt")
except FileNotFoundError as e:
    print(e)

