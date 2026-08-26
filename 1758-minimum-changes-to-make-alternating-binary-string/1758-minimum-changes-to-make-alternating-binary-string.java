class Solution {
    public int minOperations(String s) {
        int startsWith0 = 0;
        int startsWith1 = 0;
        for(int i=0; i<s.length(); i++){
            if(i%2 == 0){
                if(s.charAt(i) == '0'){
                    startsWith1++;
                }
                else{
                    startsWith0++;
                }
            }
            else{
                if(s.charAt(i) == '1'){
                    startsWith1++;
                }
                else{
                    startsWith0++;
                }
            }
        }
        return Math.min(startsWith0, startsWith1);
    }
}