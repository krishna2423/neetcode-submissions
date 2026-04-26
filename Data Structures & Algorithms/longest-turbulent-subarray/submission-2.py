class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        longest = 1
        curr = 1
        curr_num = arr[0]
        switch = None # 1 when last comparison was '>' and 0 when it was '<' and None when starting and '=='

        for i in range(1, len(arr)):
            if arr[i] > curr_num:
                if switch is None or switch == 0:
                    switch = 1
                    curr += 1
                else:
                    curr = 2
                    switch = 1

            elif arr[i] < curr_num:
                if switch is None or switch == 1:
                    switch = 0
                    curr += 1
                else:
                    curr = 2
                    switch = 0
            
            else:
                curr = 1
                switch = None
            
            curr_num = arr[i]
            longest = max(longest, curr)
        
        return longest