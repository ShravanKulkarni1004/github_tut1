a = [1,2,3]

b = [4,5,6]

# c = [5,7,9]

def addlist(l1, l2):
    l3 = []
    j = 0
    for i in l1:
        l3.append(i + l2[j])
        j += 1

    return l3

print(addlist(a,b))
