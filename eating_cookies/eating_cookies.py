'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # if n is 1...
    if n < 2:
        # there is 1 way to eat it -- 1
        return 1
    # if n is 2...
    if n == 2:
        # there are 2 ways -- 1 1 or 2
        return 2
    # if n is 3...
    if n == 3:
        # there are 4 ways - 1 1 1, 1 2, 2 1, or 3
        return 4
    # if n is bigger than all 3 of those...
    else:
        # call the function 3 more times
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
