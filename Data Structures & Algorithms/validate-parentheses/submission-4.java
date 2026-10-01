class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 != 0) return false;

        char[] stack = new char[s.length()];
        int top = 0;

        for (char c : s.toCharArray()) {
            switch (c) {
                case '(' -> stack[top++] = ')';
                case '{' -> stack[top++] = '}';
                case '[' -> stack[top++] = ']';
                default -> {
                    if (top == 0 || stack[--top] != c) {
                        return false;
                    }
                }
            }
        }

        return top == 0;
    }
}