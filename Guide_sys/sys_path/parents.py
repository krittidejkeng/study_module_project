from pathlib import Path
p = PureWindowsPath('c:/Users/Acer/Desktop/study/Guide_sys/sys_path/parent.py')
"""
An immutable sequence providing access to the logical ancestors of the path:
p.parents[0]
Display terminal>> PureWindowsPath('c:/Users/Acer/Desktop/study/Guide_sys/sys_path')
p.parents[1]
Display terminal>> PureWindowsPath('c:/Users/Acer/Desktop/study/Guide_sys')
p.parents[2]
Display terminal>> PureWindowsPath('c:/Users/Acer/Desktop/study')
"""