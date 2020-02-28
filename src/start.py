from pathlib import Path
import os
from scrap_poets import form_poet
from processing import join_poem

f = open("Poet_list.txt","r")
data = f.readlines()
data = [poet.rstrip() for poet in data]



# To creat folder same name as that of poet
for poet in data:
    path = Path(poet) #creating Path object
    if path.exists():
        print("Folder {0} already Exists!".format(poet))
    else:
        print("\nCreating Folder.....  ",poet,"\n")
        path.mkdir()
        form_poet(poet)

# To create cluster file of all poems of a poet
for poet in data:        
    join_poem(poet)
  