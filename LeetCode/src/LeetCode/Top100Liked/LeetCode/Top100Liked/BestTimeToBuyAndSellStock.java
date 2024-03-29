package LeetCode.Top100Liked;

import java.util.Arrays;

public class BestTimeToBuyAndSellStock {
    public static int maxProfit(int[] prices) {
        // μ΅μκ°μ΄ λ³??? ?? ?΄ μ€μ?¨, ?Έ?  ? ?Ό ?Έκ²? ?¬?μ§?
        //
        int minP = prices[0];
        int max = 0;
        for (int i=1;i<prices.length;i++) {
            if (minP <= prices[i]){
                max = Math.max(max, prices[i]-minP);
            } else {
                minP = prices[i];
            }
        }

        return max;
    }

    public static void main(String[] args) {
        maxProfit(new int[]{7,1,5,3,6,4});
    }
}
