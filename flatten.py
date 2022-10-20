def flatten(x):
    
    for i in x:
        if isinstance(i,list): ## is isinstance() function returns True if the specified object is of the specified type, otherwise False.
            flatten(i)
        else:
            spare_list.append(i)
            
x = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
spare_list = [] 
flatten(x)
print(spare_list)