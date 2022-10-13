
def get_data_from_file(file):
    with open(file, 'r', encoding="utf-8") as my_file:
        file_content = my_file.readlines()
        temp_list1 = [item.split(' ')[0:3] for item in file_content if len(item) > 10]
        list_values_original = []
        list_for_values_modified = []
        output_list = []
        dict_months = {
            "January": "1", "February": "2", "March": "3", "April": "4", "May": "5",
            "June": "6", "July": "7", "August": "8", "September": "9", "October": "10",
            "November": "11", "December": "12"
                      }
        for i in temp_list1:
            list_values_original.append(" ".join(i))
            i[0] = i[0][:-2]
            for keys in dict_months.keys():
                if i[1] == keys:
                    i[1] = dict_months[keys]
            list_for_values_modified.append("/".join(i))

        output_list_temp = list(zip(list_values_original, list_for_values_modified))
        for i in output_list_temp:
            output_list.append({"date_original": i[0], "date_modified": i[1]})
        return output_list


print(get_data_from_file('authors.txt'))
