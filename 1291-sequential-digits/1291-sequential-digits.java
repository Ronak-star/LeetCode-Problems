import java.util.ArrayList;
import java.util.List;

class Solution { 
    public List<Integer> sequentialDigits(int low, int high) { 
        String digits = "123456789"; // 1. Fixed missing '5'
        List<Integer> result = new ArrayList<>(); 
        
        int lowLength = String.valueOf(low).length(); 
        int highLength = String.valueOf(high).length(); 
        
        for(int left = lowLength; left <= highLength; left++){ 
            for(int right = 0; right <= digits.length() - left; right++) { // 2. Added opening brace
                String seqString = digits.substring(right, right + left); 
                int num = Integer.parseInt(seqString); 
                if(num >= low && num <= high){ // 3. Fixed missing variable 'num'
                    result.add(num); 
                } 
            } // 4. Added closing brace
        } 
        return result; 
    } 
}
