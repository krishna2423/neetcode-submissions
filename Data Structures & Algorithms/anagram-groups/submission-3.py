class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = [[] for i in range(len(strs))]
        indices = {}
        set_sorted_words = set()
        current_index = 0
        
        for s in strs: 
            copy = s
            copy = "".join(sorted(s))
            if copy in set_sorted_words:
                result[indices[copy]].append(s)
            else:
                set_sorted_words.add(copy)
                indices[copy] = current_index
                current_index += 1
                result[indices[copy]].append(s)
        
        return [x for x in result if x]





    
