from cx_Freeze import setup, Executable
import sys

# Define a base corretamente dependendo se o aplicativo é para Windows ou outro sistema operacional
base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {
    "packages": ["os", "sys", "PyQt6", "requests", "uuid", "tempfile", "subprocess", "shutil", "azure.cognitiveservices.speech"],
    "include_files": [
        ("img_source/QIcon_window.png", "img_source/QIcon_window.png"),
        ("img_source/QIcon_alertOK.png", "img_source/QIcon_alertOK.png"),
        ("img_source/QIcon_alertNOK.png", "img_source/QIcon_alertNOK.png"),
        ("img_source/start_record_icon.png", "img_source/start_record_icon.png"),
        ("img_source/stop_record_icon.png", "img_source/stop_record_icon.png"),
        ("img_source/noturn_on_off_icons.png", "img_source/noturn_on_off_icons.png")
    ],
    "includes": ["atexit"]
}

executables = [
    Executable("main.py", base=base, icon="img_source/QIcon_window.ico", target_name="Conversor de Texto em Áudio - Giovanne.exe")
]

setup(
    name="Conversor",
    version="2.0",
    description="Conversor de Texto em Áudio",
    options={"build_exe": build_exe_options},
    executables=executables
)
