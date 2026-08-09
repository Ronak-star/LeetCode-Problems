class Solution {
    public boolean validMountainArray(int[] arr) {
        int len = arr.length;
        if(len < 3){
            return false;
        }
        int i = 0, j = len - 1;
        while(i+1 < len &&  arr[i]  < arr[i+1]){
            i++;
        }
        while(j>0 && arr[j-1] > arr[j]){
          j--;
        }
        if(i > 0 && j< len - 1){
              if(i == j){
            return true;
        }
        }
      return false;
    }
}