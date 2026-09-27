class Solution {
    public String reverseParentheses(String s) {
         int n = s.length();
         Stack<Integer> openParenthesesIndices = new Stack<>();
         int[] pair = new int[n];

         for(int i =0; i<n; i++){
            if(s.charAt(i) == '('){
               openParenthesesIndices.push(i);

            }
            if(s.charAt(i) == ')'){
                int j = openParenthesesIndices.pop();
                pair[i] = j;
                pair[j] = i;

            }
         }
         StringBuilder result = new StringBuilder();
         int currIndex = 0;
         int direction = 1;

         while(currIndex < n){
            if(s.charAt(currIndex) == '(' || s.charAt(currIndex) == ')'){
                currIndex = pair[currIndex];
                direction = -direction;
            }
            else{
                result.append(s.charAt(currIndex));

            }
            currIndex += direction;
         }
         return result.toString();
    }
}