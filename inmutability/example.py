# mutable object
mutable_obj = ['a', 'b', 'c']
mutable_obj[1] = 'x'


#inmutable object
inmutable_obj = ('a', 'b', 'c')
inmutable_obj[1] = 'x'



# mutable
[1, 2, 3] #list
{1: 'one', 2: 'two'} #dictionary
{1, 2, 3} #set

# inmutable
"a" #string
(1, 2, 3) #tuple
frozenset([1, 2, 3]) #frozenset


t = (1, ['a', 'b', 'c'], 'word')
t[0] = 23 #error
t[2][0] = 'W' #error string aare inmutable
t[1][0] = '???' #you can modify list in tuple
