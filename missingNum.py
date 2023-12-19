def missingNumbers(nums):
    total = sum(range(1, len(nums) + 3)) 
    for num in nums:
        total -= num
    averageMissingValue = total // 2
    foundFirstHalf = 0
    foundSecondHalf = 0 
    for num in nums: 
        if num <= averageMissingValue: 
            foundFirstHalf += num
        else: 
            foundSecondHalf += num

    expectedFirstHalf = sum(range(1, averageMissingValue + 1))
    expectedSecondHalf = sum(range(averageMissingValue + 1, len(nums) + 3))  

    return [expectedFirstHalf - foundFirstHalf, expectedSecondHalf - foundSecondHalf]v
