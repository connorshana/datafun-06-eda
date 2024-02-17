# Create project folder in Github repository with a README.md:  DATAFUN-06-EDA
# Clone the repository down in VScode ```
# Open project folder in VS Code
# Add a .gitignore with ```.vscode/ ``` and ```.venv/```
# Create and activate a local virtual environment in .venv.

```py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install pandas pyarrow
py -m pip freeze > requirements.txt```

# Install dependencies into your .venv and () and freeze into requirements.txt.

```python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pandas pyarrow
python3 -m pip freeze > requirements.txt```

# Git add and commit with a useful message
# As working git add/commit/push to GitHub

import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started") # add this at the beginning of the main method
logging.info("Program ended")  # add this at the end of the main method
