class Solution(object):
    def groupAnagrams(self, strs):
        sortedMap = {}

        for s in strs:
            _sortedstr = "".join(sorted(s))

            if _sortedstr in sortedMap:
                sortedMap[_sortedstr].append(s)
            else:
                sortedMap[_sortedstr] = [s]

        return list(sortedMap.values())
          
        