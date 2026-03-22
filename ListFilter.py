list1 = [
            {'name': 'Rohan', 'location': 'l1'},
            {'name': 'Jivan', 'location': 'l2'},
            {'name': 'Amit', 'location': 'l1'},
            {'name': 'Atul', 'location': 'l2'},
            {'name': 'Kuldeep', 'location': 'l3'},
        ]

user_list = {}
temp_list = []
for i in list1:
    if i['location'] in user_list:
        temp_list = []
        temp_list.append(user_list[i['location']])
        temp_list.append(i)
        user_list[i['location']] = temp_list
    else:
        user_list[i['location']] = i

print(user_list)