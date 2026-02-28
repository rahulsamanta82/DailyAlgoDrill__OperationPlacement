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