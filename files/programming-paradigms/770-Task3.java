public class Task3 {
    public static void main(String[] args) {
        int n = 4;

        int[][] x = {
            {0, 0, 0, 0},
            {1, 0, 0, 0},
            {0, 2, 0, 0},
            {3, 4, 5, 6}
        };

        boolean found = false;

        for (int i = 0; i < n; i++) {
            boolean allZero = true;

            for (int j = 0; j < n; j++) {
                if (x[i][j] != 0) {
                    allZero = false;
                    break;
                }
            }

            if (allZero) {
                System.out.println("First all-zero row is: " + i);
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("No all-zero row found.");
        }
    }
}