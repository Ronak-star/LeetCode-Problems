class MyQueue {
    private Stack<Integer> main;
    private Stack<Integer> helper;
    
    
    public MyQueue() {
        main = new Stack<>();
        helper = new Stack<>();
    }
    
    public void push(int x) {
        // add all elements of main to helper --> main --> helper
       
       while(main.size()>0){
        helper.push(main.pop());
       }
        // add x to main

        main.push(x);

        // add all elements to from helper to main --> helper --> main
      while(helper.size()>0){
        main.push(helper.pop());
      }
    }
    
    public int pop() {
        return main.pop();
    }
    
    public int peek() {
        return main.peek();
    }
    
    public boolean empty() {
        return main.size()==0;

    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */