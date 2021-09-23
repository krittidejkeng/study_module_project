from pathlib import Path

# Return a string representation of the path with forward slashes (/):
p = PureWindowsPath('c:\\windows')
str(p) 

print(str(p)) # display terminal >> c:\\windows
print(p.as_posix()) # display terminal >> c:/windows


