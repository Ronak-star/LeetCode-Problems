class Solution {
    public int tribonacci(int n) {
          if(n==0){
            return 0;
        }
        else if(n==1 || n == 2 ){
            return 1;
        }

        int Firstterm = 0;
        int Secondterm = 1;
        int Thirdterm = 1;

        for( int i=1; i<=n; i++){
            int Forthterm = Firstterm + Secondterm + Thirdterm;

            Firstterm = Secondterm;
            Secondterm = Thirdterm;
            Thirdterm = Forthterm;
        }
        return Firstterm;
    }
}