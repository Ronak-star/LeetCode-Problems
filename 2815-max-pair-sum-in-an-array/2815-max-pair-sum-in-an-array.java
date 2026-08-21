class Solution {
    public int maxSum(int[] nums) {
        int max = -1;
        for(int i=0; i<nums.length; i++){
            for(int j= i+1; j<nums.length; j++){
                if(maxDigitInNum(nums[i] ) == maxDigitInNum(nums[j])){
                    max = Math.max(max, (nums[i] + nums[j]));
                }
            }
        }
        return max;
    }
    private int maxDigitInNum(int num){
        int maxDigit = 0;
        while(num != 0){
            if((num % 10) > maxDigit){
                maxDigit  = num %10;
            }
            num = num/10;
        }
        return maxDigit;
    }
}