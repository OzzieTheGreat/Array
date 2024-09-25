def selection_sort(list, size):
    for i in range(size):
        min_element = i
        for j in range(i + 1, size):
            if list[j] < list[min_element]:
                min_element = j
        (list[i], list[min_element]) = (list[min_element], list[i])
list = [2,5,3,1,4,7,6]
size = len(list)
selection_sort(list, size)
print('The list in ascending order by selection sort:')
print(list)
def average_numbers(list):
    sum_of_lst = 0
    for i in range(len(list)):
        sum_of_lst += list[i]
    average = sum_of_lst/len(list)
    return average
average = average_numbers(list)
print("Average value of even elements in list:", round(average, 2))
