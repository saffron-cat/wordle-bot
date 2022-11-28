# Wordle Project

# holds list of 5 letter possible answers
filter_list = []
try:
    with open('/Users/gray/PycharmProjects/pythonProject/Wordle_bot/5LA.txt', 'r') as answer_file:
        for line in answer_file:
            filter_list.append(line.strip())
except FileNotFoundError:
    print('Unable to locate answer list.')

print('\nMIT researchers have found the statistically optimal first guess is "SALET", which is a 15th century helm.')
print('Possible Answers Left: ' + str(len(filter_list)))

# input user interface
# TODO make a function to change input word for multiple runs
input_word = input("\nInput Word: ").lower()
if 5 > len(input_word) > 5:
    print('Wrong amount of letters. Please reset and try again.')
else:
    print('\nColor Guide: g = green, y = yellow, b = black')
    print('Example: ggyyb\n')

feedback = input('Feedback: ').lower()


def filter_list_print():
    print('Possible Answers Left: ' + str(len(filter_list)))
    print(filter_list)


filt_list = tuple(filter_list)


def filter_func(new_list):
    for item in new_list:
        for i in range(5):  # TODO make input_word a variable or something to pass in
            if feedback[i] == "b" and input_word[i] in item:
                filter_list.remove(item)
                break
            elif feedback[i] == "g" and input_word[i] != item[i]:
                filter_list.remove(item)
                break
            elif feedback[i] == "y" and input_word[i] not in item:
                filter_list.remove(item)
                break
            elif feedback[i] == "y" and input_word[i] == item[i]:
                filter_list.remove(item)
                break
    return filter_list


def print_ui(list1):
    print('\nRemaining Possibilities:' + str(len(run_1)))
    print('List:')
    for word in list1:
        print(word, end=', ')


# TODO make this more pythonic
run_1 = filter_func(filt_list)
run_2 = filter_func(run_1)
print_ui(run_1)
print_ui(run_2)
