#anagram checker

def anagram(s1,s2):
    s1 = list(s1)
    s2 = list(s2)
    flag = ''
    if len(s1)==len(s2):
        for i in s1:
            for j in s2:
                if i == j:
                    flag = True

    if flag == True:
        return True
    else:
        return False

s1 = input().replace(' ', '').lower()
s2 = input().replace(' ', '').lower()
print(anagram(s1,s2))