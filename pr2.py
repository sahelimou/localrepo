word_freq = {'is': [1, 3, 4, 8, 10],
             'at': [3, 10, 15, 7, 9],
             'test': [5, 3, 7, 8, 1],
             'this': [2, 3, 5, 6, 11],
             'why': [10, 3, 9, 8, 12]}
# Check if a value exist in dictionary with multiple value
value = 10
# Get list of keys that contains the given value
list_of_keys = [key
                for key, list_of_values in word_freq.items()
                if value in list_of_values]
if list_of_keys:
    print(list_of_keys)
else:
    print('Value does not exist in the dictionary')
