import pyrootutils
import sys
import os

# fix bug
sys.path.append("src/data")

# set up path
path = pyrootutils.find_root(search_from=__file__, indicator=".project-root")
outputs_path = path / "deploy" / "outputs"
print(outputs_path)