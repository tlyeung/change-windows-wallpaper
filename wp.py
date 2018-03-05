import ctypes
import random
import os
import winreg

# put script to "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
# check "D:\Home\Pictures" if there are wp?.jpg image
count = 0
for name in os.listdir('D:\Home\Pictures'):
    a,b = name.split('.')
    if 'wp' in a  and 'jpg' == b:
        count+=1

regKey = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(regKey, "WallpaperStyle", 0, winreg.REG_SZ, "0")
winreg.SetValueEx(regKey, "TileWallpaper", 0, winreg.REG_SZ, "0")

ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\Home\Pictures\wp%d.jpg" % random.randrange(count) , 3)
