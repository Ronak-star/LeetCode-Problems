class Solution {
    public String clearDigits(String s) {
       StringBuilder sb = new StringBuilder();
       for(int i=0; i<s.length(); i++){
        if(Character.isDigit(s.charAt(i))){
            sb.deleteCharAt(sb.length() -1);
        }
        else{
            sb.append(s.charAt(i));
        }
       } 
       return sb.toString();
    }
}