def merge_dictioaries(dict1, dict2):
    dict3= dict1

    for key, value in dict2.items():
        dict3[key]= value
    
    return dict3
