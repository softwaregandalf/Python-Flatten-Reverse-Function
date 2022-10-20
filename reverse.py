def revlist(l):
    l.reverse() ## The reverse() method reverses the sort order of the elements
    for i in l:
        i.reverse()
    return l
  
l=[[1,2],[3,4],[5,6,7]] 
print(revlist(l))