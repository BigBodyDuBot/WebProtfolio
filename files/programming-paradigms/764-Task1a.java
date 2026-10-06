public class Task1a {
    public static void main(String[] args) {

        int x = 10;
        int y = -5;

        // No braces (shows how else is matched)
        if (x > 0)
            if (y > 0)
                System.out.println("Both are positive");
            else
                System.out.println("y is not positive");

        System.out.println("End");
    }
}