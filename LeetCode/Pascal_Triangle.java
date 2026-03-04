// 118. Pascal's Triangle
// Given an integer numRows, return the first numRows of Pascal's triangle.

// In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

// Example 1:

// Input: numRows = 5
// Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
// Example 2:

// Input: numRows = 1
// Output: [[1]]
 

// Constraints:

// 1 <= numRows <= 30
 

import java.util.*;
class Pascal_Triangle {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of rows: ");
        int n = sc.nextInt();

        // Loop for each row
        for (int i = 0; i < n; i++) {

            // Print spaces to make triangle shape
            for (int space = 0; space < n - i; space++) {
                System.out.print(" ");
            }

            int number = 1;  // First value in every row

            // Print numbers in row
            for (int j = 0; j <= i; j++) {

                System.out.print(number + " ");

                // Pascal triangle formula
                number = number * (i - j) / (j + 1);
            }

            // Move to next line
            System.out.println();
        }
    }
}

