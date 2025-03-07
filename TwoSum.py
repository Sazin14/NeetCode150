from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashdict = defaultdict(list)
        for i in range(len(nums)):
            hashdict[nums[i]].append(i)         



        List = []
        for i in range(len(nums)):
            x = target - nums[i]

            if x == nums[i]:
                if len(hashdict[x])>1:
                    x = hashdict[x][1]
                    y = nums[x] + nums[i]
                    if y == target:
                        List = [i, x]
                        break
            if x!=nums[i]:
              if len(hashdict[x]) > 0:
                x = hashdict[x][0] 
                y = nums[x] + nums[i]
                if y == target:
                    List = [i, x]
                    break
            

        return List

obj = Solution()
List = obj.twoSum([2, 7, 11, 15], 9)
print(List)