class Solution {
    public boolean hasTrailingZeros(int[] nums) {
        for(int i=0; i<nums.length; i++){
            for(int j = i; j<nums.length; j++){
                int num = (nums[i] | nums[j]);
                if(i!=j && checkIfTrailingZeros(num)){
                    return true;
                }
            }
        }
        return false;
    }
    private static boolean checkIfTrailingZeros(int num){
        String n = Integer.toBinaryString(num);
        if(n.charAt(n.length() - 1 ) == '0'){
            return true;
        }
        return false;
    }
}