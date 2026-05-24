class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for n in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n,0) + 1

        for n , c in count.items():
            freq[c].append(n) 

        output = []
        for i in range(len(freq) - 1, 0 , -1):
            for a in freq[i]:
                output.append(a)
                if len(output) == k:
                    return output
