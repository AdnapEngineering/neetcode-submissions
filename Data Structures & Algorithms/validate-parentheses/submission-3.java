class Solution {
    public boolean isValid(String s) {
        if(s.length() % 2 != 0) return false; //false if string odd
        Deque<Character> stack = new ArrayDeque<>(); //LIFO 
        //iterate c in s and check if opening push closing onto stack and if close pop the element and confirm match else return false. 
        for ( char c: s.toCharArray()){
            switch(c) {
                case '(' -> stack.push(')');
                case '{' -> stack.push('}');
                case '[' -> stack.push(']');
                default -> {
                    if(stack.isEmpty() || stack.pop() != c) return false;
                }
            }
        }

        return stack.isEmpty();
    }
}
