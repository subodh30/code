class Solution {
    public boolean isPalindrome(int x) {
        String xx = String.valueOf(x);
        int j = xx.length() -1;
        for(int i=0;i<xx.length();i++){
            if(xx.charAt(i) == xx.charAt(j)){
                j--;
                continue;
            }else{
                return false;
            }
        }
        return true;
    }
}