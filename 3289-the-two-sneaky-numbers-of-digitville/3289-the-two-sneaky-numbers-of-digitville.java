class Solution {
    public int[] getSneakyNumbers(int[] nums) {
       int[] sneakyNumbers = new int[2];
       int[] count = new int[nums.length];
       int index = 0;
       for(int i=0; i<nums.length; i++){
        count[nums[i]]++;
        if(count[nums[i]] == 2){
           sneakyNumbers[index] = nums[i];
           index++;
        }
        if(index == 2){
            break;
        }
       } 
       return sneakyNumbers;
    }
}