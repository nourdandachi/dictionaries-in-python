def count_employees(dict):
    total = 0
    for department in dict.values():
        total += len(department)
    
    return total


def dict_flip(dict):
    flipped_dict= {}

    for name, age in dict.items():
        if age in flipped_dict:
            flipped_dict[age].append(name)
        else:
            flipped_dict[age] = [name]

    return flipped_dict




company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}

print (company_employees)
company_employees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}


print(company_employees)
total_employees = count_employees(company_employees)
print("Total number of employees:",total_employees)

print(" ")

dict1= {"Alice": 10, "Bob": 20, "Charlie": 10, "David": 30}
expected_output = dict_flip(dict1)
print(expected_output)

