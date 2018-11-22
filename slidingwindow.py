def maxSum(arr, n, k): 
      
    # Initialize result 
    max_sum = INT_MIN 
  
    # Consider all blocks  
    # starting with i. 
    for i in range(n - k + 1): 
        current_sum = 0
        for j in range(k): 
            current_sum = current_sum + arr[i + j]
  
        # Update result if required. 
        max_sum = max(current_sum , max_sum )
  
    return max_sum

def window(arr, k):
    n= len(arr)
    max_sum = 0
    for i in range(n-k+1):
        current_sum = sum(arr[i:i+k])
        if max_sum==0:
            max_sum= current_sum
        if i+k<n:
            max_sum = max(max_sum, current_sum - arr[i] + arr[i+k])
    return max_sum


[3,4,3,2] k=2

n = 4
for i in [0,1,2]
max_sum = 7
i==0:
    