l = ['mix', 'xyz', 'apple', 'xanadu', 'aavark']
sub_l = []
for x in l:
    if x[0] == "x":
        sub_l.append(x)
        l.remove(x)
l.sort()
sub_l.sort()
sub_l.extend(l)
print(sub_l)

list2 = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]

def last_ele(e):
    return e[-1]

list2.sort(key=last_ele)
print(list2)