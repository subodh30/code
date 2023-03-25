class Solution {
    public int closetTarget(String[] words, String target, int startIndex) {
        int min = Integer.MAX_VALUE;
        int n = words.length;
        for(int i=0; i<words.length; i++){
            int x = ( i + startIndex )%n;
            if(words[x].equals(target)){
                if(i  < min){
                    min = (i);
                }
            }
        }
        
         for(int i=0; i<words.length; i++){
            int x = ( startIndex - i + n )%n;
            if(words[x].equals(target)){
                if(i  < min){
                    min = (i);
                }
            }
        }
        
        if(min == Integer.MAX_VALUE) return -1;
        return min;
    }
}