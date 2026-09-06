class Solution {
    public int sumOfEncryptedInt(int[] nums) {
       int sum = 0;
       for(int num : nums){
        sum += encrypt(num);

       }
       return sum; 
    }
    private static int encrypt(int num){
        String str = String.valueOf(num);
        int len = str.length();
        int max = Integer.MIN_VALUE;
        for(int i=0; i<str.length(); i++){
            String ch = String.valueOf(str.charAt(i));
            if(Integer.parseInt(ch) > max){
                max = Integer.parseInt(ch);
            }
        }
        StringBuilder sb  = new StringBuilder();
        for(int i=0; i<len; i++){
            sb.append(String.valueOf(max));
        }
        return Integer.parseInt(sb.toString());
    }
}