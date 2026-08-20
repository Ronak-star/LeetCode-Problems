class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        int maxDistance = 0;
        while(mainTank >= 5 && additionalTank > 0){
            maxDistance += 50;
            mainTank = (mainTank - 5) + 1;
            additionalTank--;
        }
        maxDistance += mainTank * 10;
        return maxDistance;
    }
}