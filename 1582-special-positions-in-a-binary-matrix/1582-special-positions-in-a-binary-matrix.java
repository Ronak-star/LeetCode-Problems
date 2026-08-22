class Solution {
    public int numSpecial(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int count = 0;
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                if(mat[i][j] == 0){
                    continue;

                }
                boolean flag = false;
                for(int r = 0; r<rows; r++){
                    if(r != i && mat[r][j] == 1){
                        flag = true;
                        break;
                    }
                }
                for(int c = 0; c<cols; c++){
                    if(  c != j && mat[i][c] == 1){
                        flag = true;
                        break;
                    }
                }
                if(!flag){
                    count++;
                }
            }

        }
        return count;
    }
}