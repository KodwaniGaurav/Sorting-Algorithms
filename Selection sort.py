'''
Created on Friday Feb 23 20:51 2018
Last modified on Friday Feb 26 2:30 2018
@author: Gaurav Kodwani
'''
def selection_sort():
    user_input = raw_input('****************Please enter numbers separated by a single space only****************\n')
    numbers = []
    try:
        numbers = [int(i) for i in user_input.split(' ')]
    except:
        print('Please enter valid input.')


    print(numbers)

    for i in range (len(numbers)):
        smallest_number = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[smallest_number]:
                smallest_number = j
        numbers[i], numbers[smallest_number] = numbers[smallest_number], numbers[i]

    print(numbers)

if __name__ == '__main__':
    selection_sort()