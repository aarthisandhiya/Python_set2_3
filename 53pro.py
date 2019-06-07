import string
def abc(string):
    s="abcdefghijklmnopqrstuvwxyz"
    for c in s:
        if c not in string.lower():
            return False
    return True
string=input()
if (abc(string)==True):
    print("yes")
else:
    print("no")
