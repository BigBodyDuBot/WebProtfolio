public class Task2a {

    public static boolean firstCondition() {
        System.out.println("firstCondition evaluated");
        return false;
    }

    public static boolean secondCondition() {
        System.out.println("secondCondition evaluated");
        return true;
    }

    public static void main(String[] args) {

        if (firstCondition() && secondCondition()) {
            System.out.println("Both conditions are true");
        } else {
            System.out.println("Condition is false");
        }

        System.out.println("End");
    }
}