# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

def odd_filter(random_list):
    for i in random_list:
        if i % 2 == 0:
            random_list.remove(i)
    return random_list


print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]
