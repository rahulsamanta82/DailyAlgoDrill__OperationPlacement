// Day: 27-02-2026
// 3666. Minimum Operations to Equalize Binary String
// You are given a binary string s, and an integer k.
// In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.
// Return the minimum number of operations required to make all characters in the string equal to '1'. If it is not possible, return -1.

// Example 1:
// Input: s = "110", k = 1
// Output: 1
// Explanation:
// There is one '0' in s.
// Since k = 1, we can flip it directly in one operation.

// Example 2:
// Input: s = "0101", k = 3
// Output: 2
// Explanation:
// One optimal set of operations choosing k = 3 indices in each operation is:
// Operation 1: Flip indices [0, 1, 3]. s changes from "0101" to "1000".
// Operation 2: Flip indices [1, 2, 3]. s changes from "1000" to "1111".
// Thus, the minimum number of operations is 2.

// Example 3:
// Input: s = "101", k = 2
// Output: -1
// Explanation:
// Since k = 2 and s has only one '0', it is impossible to flip exactly k indices to make all '1'. Hence, the answer is -1.

 

class Minimum_Operations {

    public int minOperations(String s, int k) {
        int n = s.length();

        int one = 0, zero = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '0') zero++;
            else one++;
        }

        if (zero == 0) return 0;
        if (zero == k) return 1;
        if (k == 1) return zero;
        if (k >= n) return -1;

        for (int ans = 2; ans <= n; ans++) {
            int change = ans * k;

            if (change < zero) continue;
            if ((change - zero) % 2 == 1) continue;

            if (change == zero) return ans;

            if ((ans & 1) == 1 && (zero + (ans - 1) * n >= change)) return ans;
            else if ((ans & 1) == 0 && (zero + (ans - 2) * n + one * 2 >= change)) return ans;
        }
        return -1;
    }

    // 🔹 Add this
    public static void main(String[] args) {
        Minimum_Operations obj = new Minimum_Operations();

        String s = "101";
        int k = 2;

        int result = obj.minOperations(s, k);
        System.out.println("Minimum Operations: " + result);
    }
}
