def selection_sorting(lst: list[int]) -> list[int]:
    """
    sorts the list with integers using selection sort algorithm
    >>> selection_sorting([2, 8, 5, 3, 9, 4, 1])
    [1, 2, 3, 4, 5, 8, 9]
    """

    for i in range(len(lst)):
        min_ind = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_ind]:
                min_ind = j
        lst[i], lst[min_ind] = lst[min_ind], lst[i]

    return lst