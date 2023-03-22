class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        char[] a = s.toCharArray();
        for(char c: a){
            if(c == '('){
                st.push(')');
            }
             else if(c == '['){
                st.push(']');
            }
             else if(c == '{'){
                st.push('}');
            }
            else{
                if(st.size() == 0) return false;
                if(st.pop() != c) return false;
            }
        }
        if(st.size() == 0) return true;
        return false;
    }
}