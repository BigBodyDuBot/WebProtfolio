public class Task1b {
    public static void main(String[] args) {

        int x = -10;
        int y = 5;

        // Using braces to change association
        if (x > 0) {
            if (y > 0) {
                System.out.println("Both are positive");
            }
        } else {
            System.out.println("x is not positive");
        }

        System.out.println("End");
    }
}