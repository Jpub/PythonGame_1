file = open("test2.txt", 'r')
rl = file.readlines()
file.close()
for i in rl:
    print(i.rstrip("\n"))
