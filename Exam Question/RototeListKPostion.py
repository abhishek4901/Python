# Input list
nums = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter the position to rotate: "))

# Left rotate  
k = k % len(nums)  # in case k > length 
rotated = nums[k:] + nums[:k]
 
print("Rotated list:", rotated)
 
