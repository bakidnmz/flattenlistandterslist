def terslist(l):
    l.reverse()
    for i in l:
        if type(i)==list:
            terslist(i)
    return l

list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

terssli = terslist(list1)

print(terssli)

list2 = [[1, 2], [3, 4], [5, 6, 7]]

terssli2 = terslist(list2)

print(terssli2)
