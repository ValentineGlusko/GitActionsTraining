from app.models import User, Employee
# order = {
#     "order_id": 1001,
#     "customer": "Alex",
#     "product": "Laptop",
#     "price": 1200,
#     "quantity": 2,
#     "status": "pending"
# }
# random_user = User(name=order.get("customer"))
# total = order.get("price") * order.get("quantity")
# order['status'] = 'completed'
# order['total'] = total
# del order["quantity"]
# for i in order.items():
#     print(i)


def get_it_names(input_dict: dict[int:str], only_names: bool = False):
    clone = {}
    for i in input_dict:
        if "IT" in input_dict[i].values():
            clone[i] = input_dict[i]
    if only_names:
        list_of_names = []
        for line in clone.values():
            list_of_names.append(line["name"])
        return list_of_names

    return clone


def increase_salary(input_dict: dict[int:str], depart: str, percent: int):
    for l in input_dict.values:
        current_salary = input_dict['salary']
        input_dict["salary"] = current_salary + (current_salary * 1.1)
    return input_dict


def max_sal(input_dict: dict[int:str], depart: str, percent: int):
    max_value = 0
    for l in input_dict.values():
        salary_val = l['salary']
        max_value = max(max_value, salary_val)

    return max_value


employees = {
    101: {"name": "Anna", "department": "IT", "salary": 3200},
    102: {"name": "Mark", "department": "HR", "salary": 2200},
    103: {"name": "John", "department": "IT", "salary": 4000},
    104: {"name": "Kate", "department": "Finance", "salary": 3500},
    105: {"name": "Max", "department": "IT", "salary": 2800}
}
 
# add
employees[106] = {'name': "value", "name": 33}
print(employees.items())