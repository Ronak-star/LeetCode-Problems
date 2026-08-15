class Solution {
    public boolean checkZeroOnes(String s) {
        int zeroCount = 0, oneCount = 0;
        int maxZero = 0, maxOne = 0;
        for(int i=0; i<s.length(); i++){
            char ch = s.charAt(i);
            if(ch == '0'){
                zeroCount++;
                oneCount = 0;
            }
            else{
                oneCount++;
                zeroCount = 0;
            }
            maxZero = Math.max(maxZero, zeroCount);
            maxOne = Math.max(maxOne, oneCount);
        }
        if(maxOne > maxZero){
            return true;
        }
        return false;
    }
}