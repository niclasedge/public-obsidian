parent: [[Python]]
tags: 
aliases: 
Reference: [[Filesystem]]

---

### work with Folders Up
```python
import pathlib
#p = pathlib.Path('/Output/KW/SD_Report_2020_KW1.png')

p=pathlib.Path.cwd() #/Users/niclasedge/projects/dw-5-script-workflow/notebooks 

# Add Folder/Filename to a path
p=pathlib.Path.cwd() / "script" / "test" #/Users/niclasedge/projects/dw-5-script-workflow/notebooks/script/test

p.parents[0] #/Users/niclasedge/projects/dw-5-script-workflow

p.parents[1] #/Users/niclasedge/projects
```

### Show filename / suffix / stem
```python
from pathlib import Path

filename = Path("source_data/text_files/raw_data.txt")

print(filename.name)
# prints "raw_data.txt"

print(filename.suffix)
# prints "txt"

print(filename.stem)
# prints "raw_data"

if not filename.exists():
    print("Oops, file doesn't exist!")
else:
    print("Yay, the file exists!")
```

### Read Files:
```python
from pathlib import Path

data_folder = Path("source_data/text_files/")

file_to_open = data_folder / "raw_data.txt"

f = open(file_to_open)

print(f.read())
```

### Convert Unix path to windows
```python

from pathlib import Path, PureWindowsPath

filename = Path("source_data/text_files/raw_data.txt")

# Convert path to Windows format
path_on_windows = PureWindowsPath(filename)

print(path_on_windows)
# prints "source_data\text_files\raw_data.txt"
```