## Debug record
### ModuleNotFoundError
```
from src.function import *
```
Error:  ModuleNotFoundError: No module named 'src'

add parent folder to sys path
```
import sys
sys.path.append(r'd:\classes\quantitve_problems\quantitve_problems_solving')
```

### Save problem
using
```
os.getcwd()
```
to check the current working directory, and saveing path is relative path based on it