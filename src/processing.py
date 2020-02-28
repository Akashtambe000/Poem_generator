from pathlib import Path

def clear_poem_final(line):
    temp1 = ['!','~','`','+','-','_','#','@','$','%','^','&','*',':',';',',','.','?','|',')','(','[',']','>','<','=','\'','\"',u"\u2014",]
    temp2 = []
    data = line.split()
    for value in data:
        new_val = ""    
        for each_char in value:
            if each_char not in temp1:
                new_val = new_val+each_char
        temp2.append(new_val)        
    return " ".join(temp2) 

# def clear_poem(line):
#     temp1 = ['!','~','`','+','-','_','#','@','$','%','^','&','*',':',';',',','.','?','|',')','(','[',']','>','<','=',u"\u2014"]
#     temp2 = []
#     data = line.split()
#     for value in data:
#         if len(value)!=0 and value[-1] in temp1:
#             value = value.rstrip(value[-1])
#         if len(value)!=0 and value[0] in temp1:
#             value = value.lstrip(value[0])    
#         temp2.append(value)
#     return " ".join(temp2)    
  
def join_poem(poet):
    path = Path(poet)
    if  path.exists():
        files = [file for file in path.glob('*.txt')]
        if poet+"/_final_poem_ml.txt" in files:
            print("_final_poem_ml.txt already exits for ",poet)
        else:
            file_path = poet+"/_final_poem_ml.txt"
            f = open(file_path,"w",encoding='utf-8')
            for each_file in files:
                g = open(each_file,"r")
                data = g.readlines()
                for line in data[:-1]:
                    if line.rstrip().isdigit() == False:
                        new_line = clear_poem_final(line) 
                        f.write(new_line+"\n")
                g.close()
            f.close()
            print("_final_poem_ml.txt created succesfully for",poet)       
    else:
        print("folder ",poet," does not exists!!")
              

if __name__ == "__main__":
        join_poem("edgar-allan-poe")