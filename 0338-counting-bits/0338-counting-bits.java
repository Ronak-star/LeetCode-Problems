class Solution {
    public int[] countBits(int n) {
        int ans[] = new int [n + 1];
        ans[0] = 0;
        for(int i=1; i<=n; i++){
            int one_count  = countOnes(i);
            ans [i] = one_count;
        }
        return ans;
    }
    
    private int countOnes (int num){
        int count = 0;
        while (num > 0) {
            count += (num & 1); // Add 1 if the last bit is set
            num >>= 1;          // Right shift to check the next bit
        }
        return count;
    }
}