'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    arr.sort()

    index = 0
    if arr[-1] == 0:
        return arr

    while arr[index] <= 0:
        index += 1

    arr1 = arr[:index]
    arr2 = arr[index:]
    return arr2 + arr1
    
   



  
    

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")