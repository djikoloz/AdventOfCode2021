print("------------")
print("Star1")
# This opens a handle to your file, in 'r' read mode
file_handle = open(r'D:\AoC\2021\day1_input.txt')
# Read in all the lines of your file into a list of lines
lines_list = file_handle.readlines()
print(len(lines_list))
Omhooglist = []
for i in range(0,len(lines_list)):
    if int(lines_list[i]) - int(lines_list[i-1]) > 0:
        # print(int(lines_list[i]))
        # print("Omhoog")
        Omhooglist.append(lines_list[i])
print("Omhooglist lengte")
print(len(Omhooglist))
