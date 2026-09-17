class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int increasing = 1, decreasing = 1;
        int longest = 1;
        for(int i=1; i<nums.length; i++){
            if(nums[i-1] < nums[i]){
                increasing++;
                decreasing = 1;
            }
            else if(nums[i-1] > nums[i] ){
                 decreasing++;
                 increasing = 1;
            }
            else{
                increasing = 1;
                decreasing = 1;

            }
            longest = Math.max(longest, Math.max(increasing, decreasing));
        }
        return longest;
    }
}