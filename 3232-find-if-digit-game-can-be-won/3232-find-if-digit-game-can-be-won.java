class Solution {
    public boolean canAliceWin(int[] nums) {
        int singleDigitSum = 0, doubleDigitSum = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i]<10){
                singleDigitSum += nums[i];
            }
            else{
                doubleDigitSum += nums[i];
            }
        }
        return (singleDigitSum != doubleDigitSum ? true : false);
    }
}