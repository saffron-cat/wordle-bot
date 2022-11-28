# Wordle Project

# holds list of 5 letter possible answers
filt_list = []
try:
    with open('/Users/gray/PycharmProjects/pythonProject/Wordle_bot/Wordle Bot/5LA.txt', 'r') as answer_file:
        for line in answer_file:
            filt_list.append(line.strip())
except FileNotFoundError:
    print('Unable to locate answer list.')

print('\nMIT researchers have found the statistically optimal first guess is "SALET", which is a 15th century helm.')
print('Possible Answers Left: ' + str(len(filt_list)))


# input user interface


def input_func():
    input_word = input("\nInput Word: ").lower()
    print('\nColor Guide: g = green, y = yellow, b = black')
    print('Example: ggyyb\n')
    return input_word


def feedback_func():
    feedback = input('Feedback: ').lower()
    return feedback


def imput_wor_func():
    input_wor = input_func()
    return input_wor


def feedback_wor_func():
    feedback_wor = feedback_func()
    return feedback_wor


filter_list = tuple(filt_list)


# TODO fix removal logic to prevent hyper-filtration
def filter_func(new_list, input_wor, feedback):
    for item in new_list:
        for i in range(len(item)):
            if feedback[i] == "b" and input_wor[i] in item:
                try:
                    filt_list.remove(item)
                except ValueError:
                    pass
            elif feedback[i] == "g" and input_wor[i] != item[i]:
                try:
                    filt_list.remove(item)
                except ValueError:
                    pass
            elif feedback[i] == "y" and input_wor[i] not in item:
                try:
                    filt_list.remove(item)
                except ValueError:
                    pass
            elif feedback[i] == "y" and input_wor[i] == item[i]:
                try:
                    filt_list.remove(item)
                except ValueError:
                    pass
    return filt_list


def print_ui(list1):
    print('\nRemaining Possibilities:' + str(len(run_1)))
    print('List:')
    for word in list1:
        print(word, end=', ')


for num in range(6):
    run_1 = filter_func(filter_list, imput_wor_func(), feedback_wor_func())
    print_ui(run_1)
