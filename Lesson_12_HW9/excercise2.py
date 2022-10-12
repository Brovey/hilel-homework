def get_data_from_file(file):

    with open(file, 'r', encoding="utf-8") as my_file:

        file_content = my_file.readlines()
        temp_list = []
        output_list = []
        for items in file_content:
            temp_list.append(items.split('\t'))
            output_list.append(temp_list[0][1])
            temp_list.pop()

        return output_list


print(get_data_from_file('names.txt'))
