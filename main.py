import sys 

file = sys.argv[1]

with open(file, "r") as file:
    file = file.read()

list = []
for i in range(len(file)):
    if file[i] == '\n':
        
        continue
    
    list[i].append(file[i])

print(list)



