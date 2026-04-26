class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0 
        
        if k > len(arr):
            return res
        
        # calculate the average of the first k elements
        avg = 0 
        for i in range(k):
            avg = avg + (arr[i] / k)
        
        if avg >= threshold:
            res += 1
        
        L = 0
        for R in range(k, len(arr)):
            print("average: " + str(avg))
            print("res: " + str(res))
            print("right: " + str(R))
            print("left: " + str(L))
            
            avg -= arr[L] / k
            avg += arr[R] / k
            L += 1

            if avg >= threshold:
                res += 1
        return res
            