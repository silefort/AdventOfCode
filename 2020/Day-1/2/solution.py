file1 = open('input', 'r') 
List1 = file1.readlines() 
file2 = open('input', 'r') 
List2 = file2.readlines() 
file3 = open('input', 'r') 
List3 = file3.readlines() 

for x in List1:
    for y in List2:
        for z in List3:
            if int(x)+int(y)+int(z) == 2020:
                print(int(x)*int(y)*int(z))
