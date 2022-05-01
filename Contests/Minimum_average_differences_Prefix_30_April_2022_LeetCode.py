'''2256. Minimum Average Difference
User Accepted:5419
User Tried:6686
Total Accepted:5544
Total Submissions:18773
Difficulty:Medium
You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.


Input: nums = [2,5,3,9,5,3]
Output: 3
Explanation:
- The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
- The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
- The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
- The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
- The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
- The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
The average difference of index 3 is the minimum average difference so return 3.'''


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        ps=[0 for i in range(len(nums))]
        ss=[0 for i in range(len(nums))]
        res=[0 for i in range(len(nums))]
        sum1=0
        sum2=0
        for i in range(0,len(nums)):
            sum1=sum1+nums[i]
            ps[i]=int((sum1)/(i+1))
            
     
        p1=1
        ss[len(nums)-1]=0
        for i in range(len(nums)-1, 0,-1):
           
                sum2=sum2+nums[i]
               
                ss[i-1]=int((sum2)/(p1))
                p1=p1+1

        
        for k in range(0, len(nums)):
            res[k]=abs(ps[k]-ss[k])
        
        minimum=res[0]
        result=0
        for k in range(0,len(res)):
            if(minimum>res[k]):
                minimum=res[k]
                result=k
        return result
