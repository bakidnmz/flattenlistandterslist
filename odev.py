
def flattenlist(l,newl):
    for i in l:
        if type(i)==list:
            flattenlist(i,newl)
        else:
            newl.append(i)

    return newl

list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flttnlist = flattenlist(list1,[])

print(flttnlist)


