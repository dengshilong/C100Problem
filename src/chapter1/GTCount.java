package chapter1;

/**
 * Created on 16/5/8.
 * author: robinjia
 * email: dengshilong1988@gmail.com
 */
public class GTCount {
    public static int gtCount(int[] f, int[] g) {
        int i = 0;
        int j = 0;
        int result = 0;
        while (i < f.length && j < g.length) {
            if (f[i] > g[j]) {
                result += f.length - i;
                j++;
            } else {
                i++;
            }
        }
        return result;
    }
    public static void main(String[] args) {
        int[] f = {1, 3, 5, 7, 9};
        int[] g = {2, 3, 4, 7, 8};
        System.out.println(gtCount(f, g));
    }
}

