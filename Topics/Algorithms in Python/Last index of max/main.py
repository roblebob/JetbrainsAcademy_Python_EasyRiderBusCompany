def last_indexof_max(numbers):
    # write the modified algorithm here
    if not numbers:
        return -1

    index = 0
    for i, num in enumerate(numbers):
        if num >= numbers[index]:
            index = i

    return index
