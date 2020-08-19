'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    counter = 0
    for num in arr:
        if arr[num] == 0:
            counter += 1
            arr.pop(num)
    while counter > 0:
        arr.append(0)
        counter -= 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")