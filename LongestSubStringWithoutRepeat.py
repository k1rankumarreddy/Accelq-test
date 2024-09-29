# substring
# ---------

def longSubstr(s):
    n = 0
    temp = ''
    for i in s:
        temp+=i
        if temp.count(i)>1:
            return n
        else:
            n+=1
    return n
    

string = input()
ans = 0
for i in range(len(string)):
    ans_temp = longSubstr(string[i:])
    if ans_temp > ans:
        ans = ans_temp
print(ans)
