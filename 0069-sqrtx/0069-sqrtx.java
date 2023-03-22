class Solution {
    public int mySqrt(int x) {
      if(x==0 || x==1){
          return x;
      }
      int st = 0;
        int en = x;
        while(st< en){
            int mid = st + ( en - st)/2;
            int ans = x/mid;
            if (mid == ans) return mid;
            if(mid < ans){
                st = mid+1;
            }else{
                en = mid;
            }
        }
        return st-1;
    }
    
}