# TASK:
# Take a list value as an argument
# Return a string with all the items separated by a comma and space
    # With 'and' inserted before the last item
# Ex: apples, bananas, tofu, and cats

# PERSONAL TWIST:
# If the first value of the list is a string
    # Capitalize it

### MY CODE BELOW: ###

# Define function
def str_list(list_value):
    string = ''
    for i in range(len(list_value)):
        if i == 0 and type(list_value[i]) == str:
            string = list_value[i].capitalize() + ', '
        elif i == len(list_value) -1:
            string = string + 'and ' + str(list_value[i])
        else: string = string + str(list_value[i]) + ', '
    return string

# Test function with different values
list1 = ['apples', 'bananas', 'tofu', 'cats']
list2 = [1, 2, 3, 4, 5]
list3 = [0, 'pi', 3.14, 'circles']
my_string = str_list(list1)
print(my_string)
