file = open("test.txt", 'w')
for i in range(10):
    file.write("line " + str(i) + "\n")
file.close()
