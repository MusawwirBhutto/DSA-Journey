class Solution(object):
    def groupAnagrams(self, strs):
        hashmaps = {}

        for s in strs:

            _sorted = "".join(sorted(s))

            if _sorted in hashmaps:
                hashmaps[_sorted].append(s)
            else:
                hashmaps[_sorted] = [s]

        return list(hashmaps.values())            