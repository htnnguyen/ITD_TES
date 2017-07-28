import psutil
import os
os.chdir("D:\\PNNL\\Testbed\\Version 0\\76F\\Bad Insultation");

os.system("runIEEE13_B");

import time
time.sleep(60*60)
for proc in psutil.process_iter():
    if proc.name() == "fncs_broker.exe":
        proc.terminate()
    if proc.name() == "gridlabd.exe":
        proc.terminate()

os.chdir("D:\\PNNL\\Testbed\\Version 0\\76F\\Normal Insultation");
os.system("runIEEE13_N");
time.sleep(60*60)
for proc in psutil.process_iter():
    if proc.name() == "fncs_broker.exe":
        proc.terminate()
    if proc.name() == "gridlabd.exe":
        proc.terminate()

os.chdir("D:\\PNNL\\Testbed\\Version 0\\76F\\Very Good Insultation");
os.system("runIEEE13_VG");
time.sleep(60*60)
for proc in psutil.process_iter():
    if proc.name() == "fncs_broker.exe":
        proc.terminate()
    if proc.name() == "gridlabd.exe":
        proc.terminate()

os.chdir("D:\\PNNL\\Testbed\\Version 0\\72F\\Very Good Insultation");
os.system("runIEEE13_VG");
time.sleep(60*60)
for proc in psutil.process_iter():
    if proc.name() == "fncs_broker.exe":
        proc.terminate()
    if proc.name() == "gridlabd.exe":
        proc.terminate()


os.chdir("D:\\PNNL\\Testbed\\Version 0\\72F\\Normal Insultation");
os.system("runIEEE13_N");
time.sleep(60*60)
for proc in psutil.process_iter():
    if proc.name() == "fncs_broker.exe":
        proc.terminate()
    if proc.name() == "gridlabd.exe":
        proc.terminate()

os.chdir("D:\\PNNL\\Testbed\\Version 0\\72F\\Bad Insultation");
os.system("runIEEE13_B");
time.sleep(60*60)
for proc in psutil.process_iter():
    if proc.name() == "fncs_broker.exe":
        proc.terminate()
    if proc.name() == "gridlabd.exe":
        proc.terminate()

