# Samuel Tremblay, 4/15/2025
# LeetCode 1534. Count Good Triplets

def good_triplets(arr, a, b, c):
    # Find all combinations of 3 elements
    arr.reverse()
    all_triplets = enumerate_combinations(arr, 3)

    # Check conditions for good triplets for each combination
    counter = 0
    for triplet in all_triplets:
        if checkTriplet(triplet, a, b, c):
            counter = counter + 1

    # Return the number of valid good triplets
    return counter

def enumerate_combinations(array, n):
    result = backtrack_enumeration(array)
    triplets = [combination for combination in result if len(combination) == n]
    return triplets
    
def backtrack_enumeration(array):
    # base case
    if len(array) == 0:
        return [[]]
    
    # recursive call
    result = []
    for combination in backtrack_enumeration(array[1:]):
        result += [combination, combination + [array[0]]]
    return result

def checkTriplet(triplet, a, b, c):
    condition_a = abs(triplet[0] - triplet[1]) <= a
    condition_b = abs(triplet[1] - triplet[2]) <= b
    condition_c = abs(triplet[0] - triplet[2]) <= c
    return condition_a and condition_b and condition_c


input_array = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3

print(f"There are {good_triplets(input_array, a, b, c)} good triplets within the input array for a = {a}, b = {b}, c = {c}")