def insertion_sort(lst: list[int]) -> list[int]:
    """
    returns the given list where the elements are sorted in
    ascending order, using the insertion sort algorithm
    >>> insertion_sort([8, 5, 7, 3, 2])
    [2, 3, 5, 7, 8]
    """
    
    for i in range(1, len(lst)):
        val_to_sort = lst[i]
        while lst[i-1] > val_to_sort and i > 0:
            lst[i-1], lst[i] = lst[i], lst[i-1]
            i = i-1

    return lst


