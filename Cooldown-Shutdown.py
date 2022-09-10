import time
import os
seconds = 10
for i in range(seconds):
    x = (seconds - i)
    print(x)
    time.sleep(1)
    os.system("shutdown /s /t 1")