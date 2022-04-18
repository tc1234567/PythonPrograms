grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

mulOf5 = []

for mul in range(40, 101):
    if mul%5 == 0:
        mulOf5.append(mul)
            
for i in range(len(grades)):
    if grades[i] < 38:
        print(grades[i])
    if 38 <= grades[i] <= 40:
        print('40')
            
    if grades[i] > 40:
        for j in mulOf5:
            if j - grades[i] >= 0:
                if abs(j-grades[i]) < 3:
                    print(j)
                else:
                    print(grades[i])
                break

                    


