def from_list_to_strings(list):
    itens = ''
    for i in list[0:-2]:
        itens += str(i) + ', '
    itens += str(list[-2]) + ' and ' + str(list[-1])
    return itens


spam = ['apples', 'bananas', 'tofu', 'cats', 1, 3.14]

print(from_list_to_strings(spam))
