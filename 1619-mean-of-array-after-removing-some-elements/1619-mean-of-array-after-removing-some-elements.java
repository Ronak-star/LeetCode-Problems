class Solution {
    public double trimMean(int[] arr) {
        int len = arr.length;
        Arrays.sort(arr);
        double limit = 0.05 * len;
        int start = (int) limit;
        int end = len - (int) limit;
        double sum = 0, new_length = 0;
        for(int i= start; i<end; i++){
            sum = sum + arr[i];
            new_length++;

        }
        double avg = sum / new_length;
        return avg;
    }
}