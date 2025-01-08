from cx_Freeze import setup, Executable
import sys

# Define a base corretamente dependendo se o aplicativo é para Windows ou outro sistema operacional
base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {
    "packages": ["os", "sys", "PyQt6", "requests", "uuid", "tempfile", "subprocess", "shutil", "azure.cognitiveservices.speech"],
    "include_files": [
        ("QIcon_window.png", "QIcon_window.png"),
        ("QIcon_alertOK.png", "QIcon_alertOK.png"),
        ("QIcon_alertNOK.png", "QIcon_alertNOK.png"),
        ("start_record_icon.png", "start_record_icon.png"),
        ("stop_record_icon.png", "stop_record_icon.png"),
        ("noturn_on_off_icons.png", "noturn_on_off_icons.png")
    ],
    "includes": ["atexit"]
}

executables = [
    Executable("azure_pyqt6.py", base=base, icon="QIcon_window.ico", target_name="Conversor de Texto em Áudio - Giovanne.exe")
]

setup(
    name="Conversor",
    version="2.0",
    description="Conversor de Texto em Áudio",
    options={"build_exe": build_exe_options},
    executables=executables
)