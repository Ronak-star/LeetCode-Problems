class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        int maxDistance = 0;
        int minSoFar = arrays.get(0).get(0);
        int maxSoFar = arrays.get(0).get(arrays.get(0).size() - 1);
        for(int i = 1; i<arrays.size(); i++){
            int currMin = arrays.get(i).get(0);
            int currMax = arrays.get(i).get(arrays.get(i).size() - 1);


            maxDistance = Math.max(maxDistance, maxSoFar - currMin);
            maxDistance = Math.max(maxDistance, currMax - minSoFar);

            minSoFar = Math.min(minSoFar, currMin);
            maxSoFar = Math.max(maxSoFar, currMax);
        }
        return maxDistance;
    }
}