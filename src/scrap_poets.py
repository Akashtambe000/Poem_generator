from scrap_poems import form_poems
from generate_poem import copy_poems
from pathlib import Path

def form_poet(poet):    
    url = "https://www.poemhunter.com/"+poet+"/poems/"
    poem_list = []
    form_poems(url,poem_list)
    poem_no = 1
    for poem in poem_list:
        poem_file = poem[0][6:-1] + ".txt"
        path_name = poet+"/"+poem_file
        path = Path(path_name)
        if path.exists():
            print("{0}. {1} already exists".format(poem_no,path_name))
        else:
            print("{0}. creating file {1}....".format(poem_no,path_name))
            try:
                data = copy_poems("https://www.poemhunter.com" + poem[0])
                f = open(path_name,"w")
                for line in data:
                    f.write(line+"\n")
                f.close()
            except:
                print("Error occured while creating ",path_name)    
        poem_no += 1    

if __name__ == "__main__" :   
    form_poet("pablo-neruda")            