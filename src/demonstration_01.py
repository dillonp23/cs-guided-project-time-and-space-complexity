"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""

def two_sum(nums, target): #O(n) overall
     visitedNums = dict() #O(1)

     for (currIndex, firstNum) in enumerate(nums): #O(n)
        secondNum = target - firstNum #O(1)

        if secondNum in visitedNums: #O(1)
            return [visitedNums[secondNum], currIndex] #O(1)
        
        else:
            visitedNums[firstNum] = currIndex #O(1)

        # try: 
        #     prevIndex = visitedNums[secondNum] #O(1)
        #     return [prevIndex, currIndex]

        # except:
        #     visitedNums[firstNum] = currIndex #O(1)

print(two_sum([1,3,4,7,8,9], 9))


### BAD SOLUTION  ###:

# loop over and add use a pointer for current index plus the next index, if not the sum, then move current to next index
    # since only one soln., we can drop the previously visited indices
    # if nums.count  2:
    #     return []

# def two_sum(nums, target):
    # if len(nums) < 2:
    #     return list()

    # currIndex = 0
    # nextIndex = 1

    #  while currIndex < nextIndex and nextIndex < len(nums):
    #      sum = nums[currIndex] + nums[nextIndex]
            
    #      if sum == target:
    #          return [currIndex, nextIndex]

    #      elif nextIndex == len(nums) - 1:
    #          currIndex += 1
    #          nextIndex = currIndex + 1

    #      else:
    #          nextIndex += 1

    #  return list()