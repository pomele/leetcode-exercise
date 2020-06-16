class Solution:
    def smallerNumbersThanCurrent(self, nums):
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                for (key, index) in dict.items():
                    if nums[i] < key:
                        dict[key] += 1
            # else:
            #     dict[nums[i]] = 0
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = dict[nums[i]]
        print(res)




if __name__ == '__main__':
    nums = [6, 5, 4, 8, 5]
    print(nums)
    solution = Solution()
    solution.smallerNumbersThanCurrent(nums)
