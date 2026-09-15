class Solution {
    public int countPartitions(int[] nums) {
        int count = 0;
        int total  = 0;
        for(int i=0; i<nums.length; i++){
            total += nums[i];
        }
        int leftSum = 0;
        for(int i=0; i<nums.length - 1; i++){
            leftSum += nums[i];
            if((leftSum - (total - leftSum)) % 2 == 0){
                count++;
            }
        }
        return count;
    }
}