print("------------")
print("Star4")
# This opens a handle to your file, in 'r' read mode
file_handle = open(r'D:\AoC\2021\day2_input.txt')
# Read in all the lines of your file into a list of lines
lines_list = file_handle.readlines()
print(len(lines_list))
X = 0 # Horizontal
Y = 0 # Vertical Depth
Z = 0 # Aim

for i in range(0,len(lines_list)):
    value = int(lines_list[i].split(" ")[1])
    direction = lines_list[i].split(" ")[0]
    print("## ",lines_list[i])
    # Horizontal movement + Depth
    if direction == "forward":
       print("Voren = X +",value)
       print("Depth = ",Z,"*",value)
       X += value
       Y += Z * value
       print("Depth:",Y)
       print("Forward:", X)
    # Aim movement (tuple)
    elif direction in ["down","up"]:
       if direction == "down":
           print("Aim = ",Z,"+",value)
           Z += value
           print("Aim:", Z)
       elif direction == "up":
           print("Aim = ",Z,"-",value)
           Z -= value
           print("Aim:", Z)
print("#Forward: ", X)
print("#Depth: ", Y)
print("#Aim:", Z)
sum = X * Y
print("Multiply Total", sum)