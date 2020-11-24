'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
result = {}

for key,value in dict_1.items():
    for k,v in dict_2.items():
        if k == key:
            result[k] = value+v
            break
        elif k not in dict_1.keys():
            result[k] = v
    if key not in dict_2.keys():
        result[key] = value
print(result)