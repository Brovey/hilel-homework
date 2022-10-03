def group_by_surname(list_of_enrollees):  # returns 4 ints
    groups = {"A-I": "ABCDEFGHI", "J-P": "JKLMNPP", "Q-T": "QRST", "U-Z": "UXYZ"}
    groups_result = {"A-I": 0, "J-P": 0, "Q-T": 0, "U-Z": 0}
    for person in list_of_enrollees:
        name, surname = person.split()
        for key, value in groups.items():
            if surname[0] in value:
                groups_result[key] += 1

    return tuple(groups_result.values())


list_of_enrollees = ["Petr Ivanov", "Ivan Petrov", "Will Smith", "Jay Z", "Paul Anderson", "St Lem", "T Andrew"]
groups = group_by_surname(list_of_enrollees)
print(f'A-I - {groups[0]}\nJ-P - {groups[1]}\nQ-T - {groups[2]}\nU-Z - {groups[3]}')