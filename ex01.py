def merge_dictionaries(dict1, dict2):
    dict3= dict1

    for key, value in dict2.items():
        dict3[key]= value
    
    return dict3


dict1 = { 
    "a": 1,
    "b": 2,
    "c": 3
}

dict2 = {
    "b": 10,
    "d": 4
}

dict3 = merge_dictionaries(dict1, dict2)
print (dict3)