import time
import os
seconds = 10
for i in range(seconds):
    x = (seconds - i)
    print(x)
    time.sleep(1)
    print("Never Gonna Give You Up")
    os.system("shutdown /s /t 1")
