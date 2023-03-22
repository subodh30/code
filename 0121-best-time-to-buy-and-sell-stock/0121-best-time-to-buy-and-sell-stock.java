import java.lang.*;
class Solution {
    public int maxProfit(int[] prices) {
        int min = Integer.MAX_VALUE;
        int sell = -1;
        int ans = 0;
        if(prices.length <= 1) return 0;
        for(int i=0;i<prices.length;i++){
            if(min > prices[i]){
                min = prices[i];
            }
            sell = prices[i] - min;
            ans = ans < sell ? sell : ans;
        }
        return ans;
        }
    
}