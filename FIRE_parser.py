import re
import os.path 

def load_data (data_folder):
         
         data_file = os.path.join(data_folder, "FIRE_chrY.txt") 
         
         d = {"fire":{}}
                   
         with open(data_file, "r+") as f:
             for line in f:
                 y = re.split("[\t \n]", line)
                 if y[0] == "Y":
                    d["fire"]["chr"] = y[0]
                    d["fire"]["pos"] = y[1]
                    d["fire"]["ref"] = y[2]
                    d["fire"]["alt"] = y[3]
                    d["fire"]["score"] = y[4]
                    yield d
                 
if "__name__" == "__main__":
    g = load_data(data_folder)
