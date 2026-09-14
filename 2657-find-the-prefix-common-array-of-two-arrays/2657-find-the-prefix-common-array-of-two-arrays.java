class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int[] res = new int [A.length];
        Set<Integer> aSet = new HashSet<>();
        Set<Integer> bSet = new HashSet<>();
        int count = 0;
        for(int i = 0; i<res.length; i++){
            aSet.add(A[i]);
            bSet.add(B[i]);
            if(A[i] == B[i]){
                count++;
            }
            else{
                if(aSet.contains(B[i])){
                    count++;
                }
                if(bSet.contains(A[i])){
                    count++;
                }
            }
            res[i] = count;
        }
        return res;
    }
}