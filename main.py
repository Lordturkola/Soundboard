from webapp.app import WebApp
from mediaEventManager import MediaEventManager
import shutil, sys, os

current = os.path.abspath(os.curdir)
env = os.path.join(current, "environment", "soundboard")

ffmpeg_env = os.path.join(current, "environment", "ffmpeg", "bin", "*")
dst = os.path.join(env, "Lib", "site-packages", "yt_dlp")
reqs_path = os.path.join(current, "environment", "requirements.txt")
winVenvPath = os.path.join(env, "Scripts", "Activate.bat")
linuxVenvPath = os.path.join(env, "bin", "activate")
shell_command = {
    "src_win32": f"{winVenvPath}",
    "cp_win32": f"copy {ffmpeg_env} {dst}",
    "cp_linux": f"cp {ffmpeg_env} {dst}",
    "src_linux": f"source {linuxVenvPath}",
    "venv": "python -m venv soundboard",
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
    if not os.path.exists(env):
        print("creating new venv")
        os.system(shell_command["venv"])
    else:
        print("venv already exists")

    print("installing reqs")
    os.system(shell_command["pip"])
    if sys.platform == "win32" or sys.platform == "cygwin":
        print(f"sourcing {sys.platform} {shell_command['src_win32']}")
        os.system(shell_command["src_win32"])
        print("copying ffmpeg dependency to correct folder")
        os.system(shell_command["cp_win32"])
    else:
        print(f"sourcing {sys.platform} {shell_command['src_linux']}")
        os.system(shell_command["src_linux"])
        os.system(shell_command["cp_win32"])

    # MediaEventManager.start_media_manager()
    # WebApp.start_server(True)
