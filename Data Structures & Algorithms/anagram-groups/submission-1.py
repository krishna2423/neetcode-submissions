class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        result = []
        char_to_index = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
        for str in strs:
            # make a dict with the character counts
            arr = [0 for x in range(26)]
            for c in str: 
                arr[char_to_index[c]] += 1
            if tuple(arr) in map: 
                map[tuple(arr)].append(str)
            else:
                map[tuple(arr)] = [str]
        
        for k in map:
            result.append(map[k])
        return result

    
