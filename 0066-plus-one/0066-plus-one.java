import java.util.*;
class Solution {
    public int[] plusOne(int[] digits) {
        for(int i=digits.length -1; i> -1; i--){
            if(digits[i] != 9){
                digits[i] +=1;
                return digits;
            }else{
                digits[i] = 0;
            }
        }
        int[] ret = new int[digits.length + 1];
        Arrays.fill(ret,0);
        ret[0] = 1;
        return ret;
    }
}