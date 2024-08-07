import sys, os

current = os.path.abspath(os.curdir)
env = os.path.join(current, "environment", "soundboard")

ffmpeg_env = os.path.join(current, "ffmpeg", "bin", "*")
dstWin = os.path.join(env, "Lib", "site-packages", "yt_dlp", "ffmpeg")
python_ver_num = sys.version.split()[0].split(".")
python_ver = f"python{python_ver_num[0]}.{python_ver_num[1]}"
dstLinux = os.path.join(env, "lib", python_ver, "site-packages", "yt_dlp", "ffmpeg")
reqs_path = os.path.join(current, "environment", "requirements.txt")
winVenvPath = os.path.join(env, "Scripts", "Activate.bat")
linuxVenvPath = os.path.join(env, "bin", "activate")
shell_command = {
    "src_win32": f"CALL {winVenvPath}",
    "cp_win32": f"copy {ffmpeg_env} {dstWin}",
    "cp_linux": f"cp {ffmpeg_env} {dstLinux}",
    "mkdir_win": f"mkdir {dstWin}",
    "mkdir_linux": f"mkdir {dstLinux}",
    "src_linux": f"source {linuxVenvPath}",
    "venv": f"python3 -m venv {env}",
    "pip": f"pip install -r {reqs_path}",
}
if __name__ == "__main__":
    print(current)
    print(f"src:{ffmpeg_env}")
    print(f"dst:{dstLinux}")
    print(f"dst:{dstWin}")
    print(env)
    print(winVenvPath)
    print(linuxVenvPath)
    print(reqs_path)
    print(f"OS system: {sys.platform}")
    print("installing dependencies")
    
    os.system(shell_command["pip"])
    print("additional dependencies")
    if sys.platform == "win32" or sys.platform == "cygwin":
        if not os.path.exists(dstWin):
            print("copying ffmpeg bin to venv (third party dependency)")
            os.system(shell_command["mkdir_win"])
            os.system(shell_command["cp_win32"])
        else:
            print("already exists")

    else:
        if not os.path.exists(dstLinux):
            print("copying ffmpeg bin to venv (third party dependency)")
            os.system(shell_command["mkdir_linux"])
            os.system(shell_command["cp_linux"])
        else:
            print("already exists")

    from webapp.app import WebApp
    from mediaEventManager import MediaEventManager
    from threading import Thread

    t1 = Thread(target=WebApp.start_server, args=())
    t1.start()
    t2 = Thread(target=MediaEventManager.start_media_manager, args=())
    t2.start()
    
    t1.join()
    t2.join()

