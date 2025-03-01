def count_employees(dict):
    total = 0
    for department in dict.values():
        total += len(department)
    
    return total



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