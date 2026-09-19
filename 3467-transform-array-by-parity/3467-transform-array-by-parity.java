class Solution {
    public int[] transformArray(int[] nums) {
       int[] res = new int[nums.length];
       int evenCount = 0;
       for(int i=0; i<nums.length; i++){
        if(nums[i] % 2 == 0){
            evenCount++;
        }
       } 
       int index = 0;
       while(evenCount != 0){
        res[index] = 0;
        index++;
        evenCount--;
       }
       for(int i = index; i<res.length; i++){
        res[i] = 1;
       }
       return res;
    }
}