import json
from tqdm import tqdm # google this
# journals = []
idx = 0

new = open("test_data.json", "w")

with open('dblpv13.json',"r") as fp:
     for line in tqdm(fp):
        # if idx > 10000: 
        #     break
        try:
            if len(line) < 3:
                continue
            strip_line = line.strip(',')
#             hello = json.loads(strip_line)
#             print(str(hello))
            # journals.append(json.loads(strip_line))
            new.write(strip_line)
            idx += 1
        except:
            print('fail')
#             try:
#                 strip_line = line.strip(',')
#                 # journals.append(json.loads(strip_line))
# #                 new.write(strip_line + "\n")
#                 idx += 1
#             except:
            idx += 1
            pass