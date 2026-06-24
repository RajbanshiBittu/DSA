# Brute Force 
nums = [2,7,11,15]
target = 9

def twoSum(arr, tar):
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr)):
            if arr[i] + arr[j] == tar:
                return [i, j]
    return -1
print(twoSum(nums, target))

#   Optimal Solution - Two Pointer

def optimalTwoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
print(optimalTwoSum(nums, target))
    