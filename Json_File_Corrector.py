import json
from tqdm import tqdm 
idx = 0

new = open("test_data.json", "w")

with open('dblpv13.json',"r") as fp:
     for line in tqdm(fp):
        # if idx > 10000: #For Debugging if needed
        #     break
        try:
            #This is somewhat arbitrary but the goal is to avoid lines with negligible information. I've found 3 is a sufficient enough parser
            if len(line) < 3: 
                continue
            strip_line = line.strip(',')
            new.write(strip_line)
#             idx += 1 #For Debugging if needed
        except:
            print('fail')
#             idx += 1 #For Debugging if needed
            pass
