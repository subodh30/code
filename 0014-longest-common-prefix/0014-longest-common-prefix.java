class Solution {
    public String longestCommonPrefix(String[] strs) {
        String smStr = "";
        int min = Integer.MAX_VALUE;
        for(int i=0;i<strs.length;i++){
            if(strs[i].length() < min){
                min = strs[i].length();
                smStr = strs[i];
            }
        }
        String ans = "";
        for(int i=0; i<smStr.length();i++){
            boolean pre = true;
            for(int j=0;j<strs.length;j++){
                if(smStr.charAt(i) != (strs[j].charAt(i))){
                    pre = false;
                    break;
                }
            }
            if(pre){
                ans+=""+smStr.charAt(i);
            }else{
                break;
            }
        }
        return ans;
    }
}