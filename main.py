import sys, os
from webapp.app import WebApp
from mediaEventManager import MediaEventManager
from threading import Thread

current = os.path.abspath(os.curdir)
env = os.path.join(current, "environment", "soundboard")

ffmpeg_env = os.path.join(current, "ffmpeg", "bin", "*")
dst = os.path.join(env, "Lib", "site-packages", "yt_dlp")
reqs_path = os.path.join(current, "environment", "requirements.txt")
winVenvPath = os.path.join(env, "Scripts", "Activate.bat")
linuxVenvPath = os.path.join(env, "bin", "activate")
shell_command = {
    "src_win32": f"CALL {winVenvPath}",
    "cp_win32": f"copy {ffmpeg_env} {dst}",
    "cp_linux": f"cp {ffmpeg_env} {dst}",
    "src_linux": f"source {linuxVenvPath}",
    "venv": f"python3 -m venv {env}",
    "pip": f"pip install -r {reqs_path}",
}
if __name__ == "__main__":
    print(current)
    print(f"src:{ffmpeg_env}")
    print(f"dst:{dst}")
    print(env)
    print(winVenvPath)
    print(linuxVenvPath)
    print(reqs_path)
    print(os.system)
    # if os.system == "win32" or os.system == "cygwin":
    #      os.system(shell_command["cp_win32"])
    # else:
    # os.system(shell_command["cp_linux"])

    #
    t2 = Thread(target=WebApp.start_server, args=())
    t2.start()
    t1 = Thread(target=MediaEventManager.start_media_manager, args=())
    t1.start()
    t1.join()
    t2.join()
