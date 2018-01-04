import sys
from cx_Freeze import setup, Executable

build_exe_options = { "packages": ["os"], "excludes": ["tkinter","scipy"], "include_files": ["gc_settings.txt"] }

setup(
    name = "V3 Graphing Calculator",
    version = "3.6",
    description = "Graphing calculator and statistical utility.",
    options = {"build_exe": build_exe_options},
    executables = [Executable("graphing_calculator.py", base = "Win32GUI")])
