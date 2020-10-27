
f = open('insurance.csv','r')

for i in range(5):
    print(f.readline(), end="")
f.close()
