print("------------")
print("Star3")
# This opens a handle to your file, in 'r' read mode
file_handle = open(r'D:\AoC\2021\day2_input.txt')
# Read in all the lines of your file into a list of lines
lines_list = file_handle.readlines()
print(len(lines_list))
X = 0 # Horizontal
Y = 0 # Vertical Depth

for i in range(0,len(lines_list)):
    value = int(lines_list[i].split(" ")[1])
    direction = lines_list[i].split(" ")[0]
    # Horizontal movement
    if direction == "forward":
       #print("Voren = X +",value)
       X += value
    # Vertical movement (tuple)
    elif direction in ["down","up"]:
       if direction == "down":
           #print("Beneej = Y +",value)
           Y += value
       elif direction == "up":
           #print("Op = Y -",value)
           Y -= value
print("Forward ", X)
print("Depth ", Y)
sum = X * Y
print("Multiply Total", sum)