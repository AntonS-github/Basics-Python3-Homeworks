import sys
with open('bakery.csv', 'r', encoding = 'utf-8') as tab:
    text_list = tab.readlines()
    show_list = []
    num_of_row_start = int(sys.argv[1]) #сюда добавить сис аргв 1
    num_of_row_end =  int(sys.argv[2])  #сюда добавить сис аргв 2
    for i, line in enumerate(text_list, start = 1):
        show_list.append(f'{i}: {line}')
    if num_of_row_start == None and num_of_row_end == None:
        print(*show_list)
    elif num_of_row_end == None:
        print(*show_list[num_of_row_start:])
    else:
        print(*show_list[num_of_row_start:num_of_row_end])