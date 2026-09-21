class Solution {
    public int[] resultArray(int[] nums) {
        int [] result = new int[nums.length];
        result[0] = nums[0];
        result[nums.length - 1] = nums[1];
        int index1 = 0, index2 = nums.length - 1;
        for(int i=2; i<nums.length; i++){
            if(result[index1] > result[index2]){
                index1++;
                result[index1] = nums[i];
            }
            else{
                index2--;
                result[index2] = nums[i];

            }
        }
        for(int l = index2, r = nums.length - 1; l<r; l++, r--){
            int temp = result[l];
            result[l] = result[r];
            result[r] = temp;
        }
        return result;
    }
}