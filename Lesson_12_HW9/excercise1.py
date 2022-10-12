def get_data_from_file(file):

    with open(file, 'r') as my_file:
        file_content = my_file.readlines()
        output_list = []
        for items in file_content:
            output_list.append(items[1:-1])
        return output_list


print(get_data_from_file('domains.txt'))
