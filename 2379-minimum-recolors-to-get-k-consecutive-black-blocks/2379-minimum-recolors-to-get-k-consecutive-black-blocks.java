class Solution {
    public int minimumRecolors(String blocks, int k) {
       int left = 0;
       int whiteCount = 0, numRecolors = blocks.length() + 1;
       for(int right = 0; right < blocks.length(); right++){
        if(blocks.charAt(right) == 'W'){
            whiteCount++;
        }
        if(right - left + 1 == k){
            numRecolors = Math.min(numRecolors, whiteCount);
            if(blocks.charAt(left) == 'W'){
                whiteCount--;
            }
            left++;
        }
       } 
       return numRecolors;
    }
}