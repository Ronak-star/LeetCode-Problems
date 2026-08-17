class Solution {
    public int countEven(int num) {
        int count = 0;
        for(int i=1; i<=num; i++){
            if(sumOfDigits(i) % 2 == 0){
                count++;
            }
        }
        return count;
    }
    private int sumOfDigits(int n){
        int sum = 0;
        while(n != 0){
            int digit = n%10;
            sum += digit;
            n = n/10;
        }
        return sum;
    }
}