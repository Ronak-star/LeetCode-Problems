class Solution {
    public int fib(int n) {
        if(n==0){
            return 0;
        }
        else if(n==1){
            return 1;
        }

        int Firstterm = 0;
        int Secondterm = 1;

        for( int i=1; i<=n; i++){
            int Thirdterm = Firstterm + Secondterm;

            Firstterm = Secondterm;
            Secondterm = Thirdterm;
        }
        return Firstterm;
    }
}