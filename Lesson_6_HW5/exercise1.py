
def fizz_buzz(first_digit, last_digit):
    """Takes two arguments as first and last digit, generate list ,check every item for being multiple
     of 3 or 5 also for  3 and 5 replacing with according word  then return  output_list"""
    number_list = []
    output_list = []
    for i in range(first_digit, last_digit):
        number_list.append(i)

    for i in number_list:
        if i % 3 == 0 and i % 5 == 0:
            output_list.append("FizzBuzz")
        elif i % 3 == 0:
            output_list.append("Fizz")
        elif i % 5 == 0:
            output_list.append("Buzz")
        else:
            output_list.append(i)
    return output_list


def main():
    print("Числа FizzBuzz:", *fizz_buzz(1, 10), sep='\n')


main()

