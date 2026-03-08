// 1980. Find Unique Binary String
// Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

// Example 1:

// Input: nums = ["01","10"]
// Output: "11"
// Explanation: "11" does not appear in nums. "00" would also be correct.
// Example 2:

// Input: nums = ["00","01"]
// Output: "11"
// Explanation: "11" does not appear in nums. "10" would also be correct.
// Example 3:

// Input: nums = ["111","011","001"]
// Output: "101"
// Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 

// Constraints:

// n == nums.length
// 1 <= n <= 16
// nums[i].length == n
// nums[i] is either '0' or '1'.
// All the strings of nums are unique.



import java.util.*;

public class find_unique {

    static class Solution {
        public String findDifferentBinaryString(String[] nums) {
            StringBuilder s = new StringBuilder();

            for(int i = 0; i < nums.length; i++) {
                if(i < nums[i].length()) {
                    char curr = nums[i].charAt(i);
                    s.append(curr == '0' ? '1' : '0');
                } else {
                    s.append('1');
                }
            }

            return s.toString();
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        String[] nums = new String[n];

        for(int i = 0; i < n; i++) {
            nums[i] = sc.next();
        }

        Solution obj = new Solution();
        System.out.println(obj.findDifferentBinaryString(nums));

        sc.close();
    }
}