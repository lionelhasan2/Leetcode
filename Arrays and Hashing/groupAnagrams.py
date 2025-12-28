class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            sorted_string = ''.join(sorted(s))
            if map.get(sorted_string) is None:
                map[sorted_string] = [s]
            else:
                map[sorted_string].append(s)
        groupList = []
        for key in map:
            groupList.append(map[key])
        
        return groupList
