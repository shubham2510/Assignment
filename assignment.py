import io
import json
import os
import threading 
from threading import*
import time

filename = 'json.json'
if os.path.isfile(filename):
    with open(filename) as f:
        data = json.load(f)
        print(data)
else:
    with open(filename, 'w+') as f:
        f.write('"shubzz": [23,0]')            
        f.close

with open(filename) as f:
        data = json.load(f)

def write_json(data, filename=filename): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

def create(key,value,timeout=0):
    with open(filename) as f:
        data = json.load(f)
        if key in f:
            print("key already exists") #error message1
        else:
            if(key.isalpha()):
                if len(data)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                    if timeout==0:
                        l=[value,timeout]
                    else:
                        l=[value,time.time()+timeout]
                    if len(key)<=32: #constraints for input key_name capped at 32chars
                        data[key]=l
                        print(json.dumps(data))
                        write_json(data)
                else:
                    print("Memory limit exceed ")#error message2
            else:
                print("key_name must contain only alphabets and no special characters or numbers")


def read(key):
    
    if key not in data:
        print("key does not exist in database.") #error message4
    else:
        b=data[key]
        if b[1]!=0:
            if time.time()< b[1]: #comparing the present time with expiry timeprint
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                print(stri)
            else:
                print("Time has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            print(stri)


read("sastra")

def delete(key):
    if key not in data:
        print("key does not exist in database.") #error message4
    else:
        b=data[key]
        if b[1]!=0:
            if time.time()< b[1]: #comparing the current time with expiry time
                del data[key]
                print(json.dumps(data))
                write_json(data)
                print("key is successfully deleted")
            else:
                print("Time has expired") #error message5
        else:
            del data[key]
            print(json.dumps(data))
            write_json(data)
            print("key is successfully deleted")


