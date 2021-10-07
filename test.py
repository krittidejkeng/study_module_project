from pathlib import Path

sep = ' '
path = 'runs/detect/exp.jpg'
path = Path(path)
suffix = path.suffix
print("Path is",path)
print("suffix is",suffix)
path = path.with_suffix('')


print("{path}{sep} is",f"{path}{sep}*")