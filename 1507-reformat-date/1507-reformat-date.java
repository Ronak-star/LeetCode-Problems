class Solution {
    public String reformatDate(String date) {
        String year = date.substring(date.length() - 4 );
        String result = year + "-";
        Map<String, String> map = new HashMap<String, String>();
        map.put("Jan", "01");
        map.put("Feb", "02");
        map.put("Mar", "03");
        map.put("Apr", "04");
        map.put("May", "05");
        map.put("Jun", "06");
        map.put("Jul", "07");
        map.put("Aug", "08");
        map.put("Sep", "09");
        map.put("Oct", "10");
        map.put("Nov", "11");
        map.put("Dec", "12");

        String month = date.substring(date.length() - 8, date.length() - 5);
        List<String> list = new ArrayList<String>(map.keySet());
        for(String str: list){
            if(str.equals(month)){
                result +=  map.get(str) + "-";
            }
        }
        String words[] = date.split(" ");
        String day_th = words[0];
        String day = "";
        for(int i=0; i<day_th.length(); i++){
            if(Character.isDigit(day_th.charAt(i))){
                day +=Character.toString(day_th.charAt(i));

            }
        }


 if(day.length() == 1) {
    result += "0" + day;
 }
 else if(day.length() == 2){
    result += day;
 }  
 return result;
 }
}