class Solution {
    public int romanToInt(String s) {
        Map<String, Integer> hash = new HashMap();
        hash.put("I", 1);
        hash.put("V", 5);
        hash.put("X", 10);
        hash.put("L", 50);
        hash.put("C", 100);
        hash.put("D", 500);
        hash.put("M", 1000);
        hash.put("IV", 4);
        hash.put("IX", 9);
        hash.put("XL", 40);
        hash.put("XC", 90);
        hash.put("CD", 400);
        hash.put("CM", 900);
int ans = 0;
        for(int i=0; i<s.length()-1; i++){
            String dd = ""+s.charAt(i) + s.charAt(i+1);
            if(hash.get(dd) != null){
                ans+=hash.get(dd);
                i++;
            }else{
                ans+=hash.get(""+s.charAt(i));
            }
        }
        if(s.length() >= 2){
        String dd = ""+s.charAt(s.length()-2) + s.charAt(s.length()-1);
            if(hash.get(dd) == null){
                ans+=hash.get(""+s.charAt(s.length()-1));
            }
    }else{
            ans = hash.get(""+s.charAt(0));
        }
        return ans;
    }
}