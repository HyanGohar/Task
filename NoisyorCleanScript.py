import pathlib
import json
from playsound import playsound
from pathlib import Path

playlist={}
path_=input("Insert the folder path ")

for path in pathlib.Path(path_).iterdir():
    if path.is_file():     
        playsound(str(path))
        print(Path(path).name)  
        userinput=input("Insert 'n' for the noisy sound and 'c' for the clean one\n")
            
        while (userinput!="n" and userinput!="c"):
            if (userinput=="r"):
                playsound(str(path))                
            userinput=input("Try again: Insert 'n' for the noisy sound and 'c' for the clean one! For replay input 'r'\n")
            
        if userinput=="n":
            playlist[Path(path).name]=userinput
            
        else:
            playlist[Path(path).name]=userinput           
      
with open("Playlist.txt","w+") as file:
    json.dump(playlist,file,indent=3)
