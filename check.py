import os

corn = r'C:\Users\papa6\Downloads'
zero = 1
for i in os.listdir(corn):

    if os.path.isdir(corn+"\\"+i):
        if os.path.splitext(i)[0] == "prj":
            break
        elif os.path.splitext(i)[0] == 'img':
            print(f"{os.path.splitext(i)}, zero")
            zero -= 1
            continue

        print(f"{os.path.splitext(i)}, {zero}")
        zero += 1
