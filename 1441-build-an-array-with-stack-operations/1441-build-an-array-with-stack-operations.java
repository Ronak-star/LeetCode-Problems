class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> opsList = new ArrayList<>();
        int input = 1;
        for(int num : target){
            while(input < num){
                opsList.add("Push");
                opsList.add("Pop");
                input++;
            }
            opsList.add("Push");
            input++;
        }
        return opsList;
    }
}