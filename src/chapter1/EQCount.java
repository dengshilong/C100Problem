package chapter1;

/**
 * Created on 16/5/8.
 * author: robinjia
 * email: dengshilong1988@gmail.com
 */
public class EQCount {
    public static int eqCount(int[] f, int[] g) {
        int i = 0;
        int j = 0;
        int result = 0;
        while (i < f.length && j < g.length) {
            if (f[i] == g[j]) {
                i++;
                j++;
                result++;
            } else if (f[i] > g[j]) {
                j++;
            } else {
                i++;
            }
        }
        return result;
    }
    public static void main(String[] args) {
        int[] f = {1, 3, 4, 7, 9};
        int[] g = {3, 5, 7, 8, 10};
        System.out.println(eqCount(f, g));
    }
}
