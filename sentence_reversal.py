#sentence reversal

def rev_sentence(s):

    temp_list = []
    count=1
    for _ in range(len(s)):
        temp_list.append(s[len(s)-count])
        count+=1

    return temp_list

sentence = list(map(str, input().split()))
print(rev_sentence(sentence))

