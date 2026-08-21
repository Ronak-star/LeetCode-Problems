class Solution {
    public int accountBalanceAfterPurchase(int purchaseAmount) {
        int rem = purchaseAmount % 10;
        int balance = 10 - rem;
        if(rem < 5){
            purchaseAmount = purchaseAmount - rem;

        }
        else{
            purchaseAmount = purchaseAmount + balance;
        }
        return 100 - purchaseAmount;
    }
}