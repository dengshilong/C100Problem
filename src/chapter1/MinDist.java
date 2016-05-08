package chapter1;

/**
 * Created on 16/5/8.
 * author: robinjia
 * email: dengshilong1988@gmail.com
 */
public class MinDist {
    public static int minDist(int[] x, int[] y) {
        int result = Integer.MAX_VALUE;
        int i = 0;
        int j = 0;
        while (i < x.length && j < y.length) {
            if (x[i] >= y[j]) {
                result = Math.min(result, x[i] - y[j]);
                j++;
            } else {
                result = Math.min(result, y[j] - x[i]);
                i++;
            }
        }
        return result;
    }
    public static void main(String[] args) {
        int[] x = {1, 3, 5, 7, 9};
        int[] y = {2, 6, 8};
        System.out.println(minDist(x, y));
    }
}
