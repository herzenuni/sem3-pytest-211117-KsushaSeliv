from itertools import zip_longest
 
keys = ["a", "b", "c", "d"]
values = [1, 2, 3]
 
d = dict(zip_longest(keys, values))
if 'None' in d: del d['None']
 
print(d)
