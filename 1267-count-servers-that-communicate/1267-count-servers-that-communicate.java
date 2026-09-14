class Solution {
    public int countServers(int[][] grid) {
        if(grid == null || grid.length == 0){
            return 0;
        }
        int rows = grid.length;
        int cols = grid[0].length;
        int[] rowCount = new int[rows];
        int[] colCount = new int[cols];
        for(int row = 0; row < rows; row++){
            for(int col = 0; col < cols; col++){
               if(grid[row][col] == 1)
               {
                rowCount[row]++;
                colCount[col]++;
               }
            }
        }
        int count = 0;
        for(int row = 0; row < rows; row++){
            for(int col = 0; col < cols; col++){
                if(grid[row][col] == 1){
                    if(rowCount[row] > 1 || colCount[col] > 1){
                         count++;
                    }
                }
            }
        }
        return count;
    }
}