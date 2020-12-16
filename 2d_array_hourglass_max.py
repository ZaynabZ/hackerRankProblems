# this function returns the max of the sum of the elements of an array
# gathered in the shape of an hourglass
# the array treated in the function is of size 6 * 6
# It contains 16 hourglass
def hourglassSum(arr):
    return max([sum(
        [arr[i][j], arr[i][j + 1], arr[i][j + 2], arr[i + 1][j + 1], arr[i + 2][j], arr[i + 2][j + 1],
         arr[i + 2][j + 2]])
        for i in range(4) for j in range(4)])

