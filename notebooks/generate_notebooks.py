import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
import json

# Load the config_notebook.json file
with open('config_notebook.json', 'r') as f:
    config = json.load(f)

nb = new_notebook()

for cell in config:
    if cell['type'] == 'code':
        nb.cells.append(new_code_cell(cell['content']))
    elif cell['type'] == 'markdown':
        nb.cells.append(new_markdown_cell(cell['content']))

# Save the notebook
with open('output.ipynb', 'w') as f:
    nbformat.write(nb, f)
