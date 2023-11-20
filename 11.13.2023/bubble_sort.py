def bubble_sort(things: list) -> list:
    '''
    Function: bubble_sort -- sorting the elements of a list by swapping
                             two consecutive elements that are out of order
    Parameters:
       things -- the elements to be sorted
    Returns a new list with all of the elements in sorted order
    '''
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(things)-1):
            if things[i] > things[i+1]:
                tmp = things[i]
                things[i] = things[i+1]
                things[i+1] = tmp
                swapped = True
                # things[i], things[i+1] = things[i+1], things[i]
    return things


def main():
    things = [1, 2, 3, 4, 5, 6]
    sorted = bubble_sort(things)
    print(f'{things} - {sorted}')

    things = ['a', 'b', 'c', 'e', 'd']
    sorted = bubble_sort(things)
    print(f'{things} - {sorted}')

    things = [9, 8, 7, 6, 5]
    sorted = bubble_sort(things)
    print(f'{things} - {sorted}')

    things = ['d', 'a', 'c', 'b', 'e']
    sorted = bubble_sort(things)
    print(f'{things} - {sorted}')

if __name__ == '__main__':
    main()