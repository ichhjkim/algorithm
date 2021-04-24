package LeetCode.Top100Liked;

public class ClimbingStairs {
    public static int climbStairs(int n) {

        int num_1 = 1;
        int num_2 = 2;

        if (n==1) return num_1;
        if (n==2) return num_2;

        int result = 0;
        for (int i=3;i<n+1;i++) {
            result = num_1+num_2;
            num_1 = num_2;
            num_2 = result;
        }
        return result;
    }

    public static void main(String[] args) {

    }

}
