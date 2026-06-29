def moveZeroes(nums):
        c=0
        for i in range(0,len(nums)-1):
            if nums[i]==0:
                nums.remove(0)
                c+=1
        return nums+[0]*c
print(moveZeroes([0]))