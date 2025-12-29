import java.util.Scanner;

class MatrixDiagonalSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] matrix = new int[3][3];

        // Input matrix
        System.out.println("Enter elements of 3x3 matrix:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        int primarySum = 0, secondarySum = 0;

        for (int i = 0; i < 3; i++) {
            primarySum += matrix[i][i];          // primary diagonal
            secondarySum += matrix[i][2 - i];    // secondary diagonal
        }

        int totalSum = primarySum + secondarySum - matrix[1][1]; // avoid double-count

        System.out.println("Sum of primary diagonal = " + primarySum);
        System.out.println("Sum of secondary diagonal = " + secondarySum);
        System.out.println("Total sum of both diagonals = " + totalSum);
    }
}