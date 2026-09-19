class Solution {
    public int[] applyOperations(int[] nums) {
        int[] res = new int[nums.length];
        for(int i=0; i<nums.length - 1; i++){
            if(nums[i] == nums[i+1]){
                nums[i] = nums[i] * 2;
                nums[i + 1] = 0;

            }
        }
        int index = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] != 0){
                res[index++] = nums[i];
            }
        }
        for(int i = index; i<res.length; i++){
            res[i] = 0;
        }
        return res;
    }
}