class Solution {
    public int winningPlayerCount(int n, int[][] pick) {
        Map<Integer, Map<Integer, Integer>> map = new HashMap<>();
        for(int [] p : pick){
            int player = p[0];
            int color = p[1];
            if(!map.containsKey(player)){
                map.put(player, new HashMap<>());
            }
            Map<Integer, Integer> playerColors = map.get(player);
            playerColors.put(color, playerColors.getOrDefault(color, 0) + 1);

        }
        int winners = 0;
        for(int i=0; i<n; i++){
            boolean won = false;
              Map<Integer, Integer> playerColors = map.getOrDefault(i, new HashMap<>());
for(int count : playerColors.values()){
  if(count > i){
    won = true;
    break;
  }
}
if(won){
    winners++;
}

        }
        return winners;
    }
}