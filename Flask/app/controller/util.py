import psutil
import json
import platform
import re
import os
import socket


def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['kernel']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['phcpu']=psutil.cpu_count(logical=False)
        info['vrcpu']=psutil.cpu_count()
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        print("info")
        return json.dumps(info)
    except Exception as e:
        print(e)
        return {"MSG":False}

def getSystemUsageInfo():
    try:
        info={}
        info['CPU']=psutil.cpu_percent()
        info['RAM']=psutil.virtual_memory().percent
        info['DISK']=psutil.disk_usage('/').percent
        TEMP = psutil.sensors_temperatures()
        TEMP = TEMP.get("coretemp")
        if(TEMP):
            TEMP = TEMP[0].current
        else:
            TEMP = -1
        info['TEMP']= TEMP
        info['temp']=str(psutil.sensors_temperatures())
        print(info)
        return json.dumps(info)
    except Exception as e:
        print(e)
        return {"MSG":False}



