import java.util.Scanner;

public class LeapYearCalculation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String studentID = "m25w7502";

        System.out.print("Enter a year: ");
        int year = sc.nextInt();

        // Nested conditional with logical expressions
        if (year % 4 == 0) {
            if (year % 100 == 0) {
                if (year % 400 == 0) {
                    System.out.println("ID: " + studentID);
                    System.out.println(year + " is a Leap Year");
                } else {
                    System.out.println("ID: " + studentID);
                    System.out.println(year + " is NOT a Leap Year");
                }
            } else {
                System.out.println("ID: " + studentID);
                System.out.println(year + " is a Leap Year");
            }
        } else {
            System.out.println("ID: " + studentID);
            System.out.println(year + " is NOT a Leap Year");
        }

        sc.close();
    }
}