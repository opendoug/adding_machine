more_prompt = 'Yes'
while (more_prompt == 'Yes'):

    # get first number
    print('Choose first number!')
    is_int = 'No'
    while is_int == 'No':
        first_input = input()
        try:
            first_num = int(first_input)
        except:
            print('Enter an integer, please!')
        else:
            is_int = 'Yes'
  
    # get second number
    print('Choose second number!')
    is_int = 'No'
    while is_int == 'No':
        second_input = input()
        try:
            second_num = int(second_input)
        except:
            print('Enter an integer, please!')
        else:
            is_int = 'Yes'

    # print the sum
    print(int(first_num) + int(second_num))
    print('Want to add some more numbers? Yes or No?')
    more_prompt = input()