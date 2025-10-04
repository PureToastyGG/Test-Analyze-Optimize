# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers): 
    counts = {}
    most = None
    max_count = 0

    for num in numbers: 
        counts[num] = counts.get(num, 0) + 1 
        if counts[num] > max_count:
            max_count = counts[num] 
            most = num 
    return most

"""
Time and Space Analysis for problem 1:
- Best-case: The best case scenario for this function is O(n) time complexity, we can't make this any shorter 
because we have to look at every value to know whether or not we have found the number with the most occurences.
- Worst-case: The worst case scenario is also O(n) time complexity, as we still have to look at every value in the list.
- Average-case: The average case is also O(n) time complexity, as we have to look at every value in the list.
- Space complexity:
- Why this approach? This approach uses a dictionary to count occurrences, which is effiecient for tracking the counts with 
out creating too many other variables that are taking up space.
- Could it be optimized? Maybe it could be operating by breaking the loop early if we find a number that has more than half the occurences,
or more than the remaining numbers in the list, but this would be a rare case.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    repeats = set(nums)
    return repeats

"""
Time and Space Analysis for problem 2:
- Best-case: O(1) because all it needs to do is make a set from the list, which is done in constant time.
- Worst-case: O(1) because making a set from the list is done in constant time regardless of input size.
- Average-case: O(1) because making a set from the list is done in constant time regardless of input size.
- Space complexity: O(n) because the set will store up to n unique elements from the input list.
- Why this approach? Using a set is the most efficient way to remove duplicates in Python, with nearly 
no run time and only a little bit of space complexity.
- Could it be optimized? No, this is already optimal for the task at hand.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    pairs = []
    for num in nums: 
        if target - num in nums: 
            pairs.append((num, target - num)) 
            nums.remove(num) 
        else: 
            continue
    return pairs
"""
Time and Space Analysis for problem 3:
- Best-case: Best case is O(n^2) time complexity, where n is the number of elements in the list. 
We have to look at each element once to check if its complement (target - num) exists in the list. 
and if there are no pairs than the loop will only run n times.
- Worst-case: Worst case is O(n^2) time complexity, which when there are pairs in the list, and we have to search 
for each complement in the list, which takes O(n) time for each of the n elements.
- Average-case: O(n^2) time complexity, as on average we will have to search through half the list for each element.
- Space complexity: O(k) where k is the number of pairs that are actually found.
- Why this approach? This appraoch is effective and works better than checking each individial addition to check if the sum equals the target.
- Could it be optimized? You could maybe use a set when checking if the number requried for the sum is in the list, this 
could reduce your time complexity to O(n) overall because checking for membership in a set is O(1) on average.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    fixed_capacity = 4
    lst = [None] * fixed_capacity 
    while n > fixed_capacity:
        print("Resizing from", fixed_capacity, "to", fixed_capacity * 2)
        new_lst = [None] * (fixed_capacity * 2)
        for i in range(fixed_capacity):
            new_lst[i] = lst[i]
        lst = new_lst
        fixed_capacity *= 2
    pass

"""
Time and Space Analysis for problem 4:
- When do resizes happen? The resizes everytime elements are needed to be added that exceed the size 
of the current list capacity.
- What is the worst-case for a single append? The worst case for a single append is O(n) time complexity,
because we have to copy all the elements from the old list to the new list when resizing.
- What is the amortized time per append overall? The amortized time per append is O(1) because although a single append can take O(n) time when resizing,
most appends will take O(1) time, and the cost of resizing is spread out over many appends.
- Space complexity: O(n) because we are storing n elements in the list.
- Why does doubling reduce the cost overall? Doubling reduces the cost overall because it minimizes the number of times we need to resize 
while also not being too wasteful with our space.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    total = 0 
    for i in range(len(nums)):
        total += nums[i]
        nums[i] = total
    return nums

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) time complexity, as we have to iterate through the entire list to compute the running totals.
- Worst-case: O(n) time complexity, as we have to iterate through the entire list to compute the running totals.
- Average-case: O(n) time complexity, as we have to iterate through the entire list to compute the running totals.
- Space complexity: O(1) if we modify the list in place because we are not adding any new lists to storage, just modifying 
old one and returning it.
- Why this approach? This approach doesn't add any extra space and keeps the time complexity pretty low.
- Could it be optimized? No, I think this is the most efficient way to compute running totals.
"""

print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Output: 3
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Output: [4, 5, 6, 7]
print(find_pairs([1, 2, 3, 4], 5))  # Output: [(1, 4), (2, 3)]
add_n_items(12) # Should print resizing message
print(running_total([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]