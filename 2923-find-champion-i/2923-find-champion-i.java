class Solution {
    public int findChampion(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        for(int i=0; i<row; i++){
            int count = 0;
            for(int j=0; j<col; j++){
                if(grid[i][j] == 1){
                    count++;
                }
                if(count == grid.length - 1){
                    return i;
                }

            }
        }
        return -1;
    }
}