1680. Concatenation of Consecutive Binary Numbers
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 
Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
 

Constraints:

1 <= n <= 105





import java.util.Scanner;

public class Concatenation_of_Consecutive {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input
        int n = sc.nextInt();

        // Object creation
        Concatenation_of_Consecutive obj = new Concatenation_of_Consecutive();

        // Output
        System.out.println(obj.concatenatedBinary(n));

        sc.close();
    }

    public int concatenatedBinary(int n) {
        final int MOD = 1_000_000_007;
        long ans = 0;

        for (int i = 1; i <= n; ++i) {
            ans = ((ans << numberOfBits(i)) % MOD + i) % MOD;
        }

        return (int) ans;
    }

    private int numberOfBits(int n) {
        return 32 - Integer.numberOfLeadingZeros(n); // Better than log()
    }
}