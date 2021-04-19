""" Generator for virtual files"""

import mkdocs_gen_files

with open("README.md") as file:
    readme = file.read()

with mkdocs_gen_files.open("index.md", "w") as f:
    print(readme, file=f)
    