class Solution {
    public int finalPositionOfSnake(int n, List<String> commands) {
        int pos = 0;
        for(String command : commands){
             if(command.equals("RIGHT")){
                pos += 1;
             }
               if(command.equals("LEFT")){
                pos -= 1;
             }
               if(command.equals("UP")){
                pos -= n;
             }
               if(command.equals("DOWN")){
                pos += n;
             }
        }
        return pos;
    }
}