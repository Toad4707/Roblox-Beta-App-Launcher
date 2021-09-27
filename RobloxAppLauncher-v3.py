import subprocess
import os

versions = os.path.join(os.getenv("LOCALAPPDATA"),"Roblox/Versions/")

def GetRobloxBeta():
    for path in os.listdir(versions):
        for path2 in os.listdir(versions + "/" + path):
            if (path2 == "RobloxPlayerBeta.exe"):
                return path + "/" + path2

location = versions + GetRobloxBeta()
subprocess.run([location,"--app"])