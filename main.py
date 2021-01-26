fname = input("Enter filename with extension: ")

with open(fname, 'r') as f:
    cont = f.read()
    print(cont)

zero = True
while zero:
    fin = input("Find a word which u want to replace: ")
    count = 0
    count = cont.count(fin)
    if count == 0:
        print(f"Sorry! There are no words of {fin}")
    else:
        print(f"There are {count} occurences of {fin}")
        zero = False
    

rep = input(f"Replace {fin} with: ")

cont1 = cont.replace(fin, rep)

with open(fname, 'w') as f:
    f.write(cont1)

print(f"Replaced {fin} with {rep} {count} times")

print("## New contents of file ##: ")
print(cont1)