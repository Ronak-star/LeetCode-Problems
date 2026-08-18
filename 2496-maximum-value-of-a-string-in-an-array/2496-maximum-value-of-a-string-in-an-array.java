class Solution {
    public int maximumValue(String[] strs) {
     int max = 0;
     int value = 0;
     for(int i=0; i<strs.length; i++){
        if(strTypeCheck(strs[i]) == 1){
            value = Integer.parseInt(strs[i]);
        }
        if(strTypeCheck(strs[i]) == -1 || strTypeCheck(strs[i]) == 2){
            value = strs[i].length();
        }
        max = Math.max(max,value);
     }   
     return max;
    }
    private static int strTypeCheck(String str){
        int count = 0;
        for(int i=0; i<str.length(); i++){
            if(Character.isDigit(str.charAt(i))){
                count++;
            }
        }
        if(count == str.length()){
            return  1;
        }
        if(count == 0){
            return -1;
        }
        return 2;
    }
}