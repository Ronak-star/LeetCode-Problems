class Solution {
    public int balancedStringSplit(String s) {
        if(s == null || s.length() == 0){
            return 0;
        }
        int left = 0, right = 0, count = 0;
        for(int i=0; i<s.length(); i++){
            char ch = s.charAt(i);
            if(ch == 'L'){
                left++;
            }
            else{
                right++;
            }
            if(left == right){
                count++;
            }
        }
        return count;
    }
}