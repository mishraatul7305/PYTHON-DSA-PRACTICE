## PROBLEM  1  ---------------------------------------------------

def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return None

print(two_sum([2, 3, 11, 15], 5)) 

##PROBLEM 2  
#maximum Subarray 

def max_subarray(nums):
     cur = best = nums[0]
     for x in nums[1:] : 
         cur = max (x, cur + x)
         best = max (best,cur)
     return best
  
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))

## problem 3==================================
## Rotate Array ----------------------------------------

def rotate (nums,k):
    k %=len(nums) 
    nums[:] = nums [-k:] + nums[:-k]
a=[1,2,3,4,5,6,7]
rotate (a,3)
print(a) 

## problem 4 ===============================
## Quick Sort (two pointers), O(n) 

arr= [6,3,8,2,5,1,7,4]

pivot=arr [-1]
i=-1 
for j in range(len(arr) -1):
    if arr[j] < pivot:
        i+=1
        arr[i],arr[j]=arr[j],arr[i]
arr [i+1],arr[-1] = arr[-1],arr[i+1]
print (arr)
        
## problem 5 ================== 
arr =[1,2,3,4]
i=0
j-=len(arr)-1
while i < j :
    arr[i],arr[j]=arr[j],arr[i]
    i += 1
    j-=1
    print(arr)

        ##problem -6 -----------------
arr=[5,4,3,2,1]
j=0
j-=len(arr) -1 
while i < j :
    arr[i],arr[j]=arr[j],[i]
    i+=1
    j-=1
    print(arr)
        
    
    

    
    