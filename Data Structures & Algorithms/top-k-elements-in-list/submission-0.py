class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashMap with counter
        # values with highest counter 
        # return that number
        if nums == None:
            return []

        count = Counter(nums)

        common = count.most_common(k)

        arr = []

        for val, _ in common:
            arr.append(val)

        return arr

        




        