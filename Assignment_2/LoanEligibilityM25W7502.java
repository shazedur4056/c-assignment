// Name: Rahman Md Shazedur
// Student ID: M25W7502

import java.util.Scanner;

// Class declaration (Student ID included)
public class LoanEligibilityM25W7502 {

    // Main method (program starts here)
    public static void main(String[] args) {

        // Scanner object for input
        Scanner input = new Scanner(System.in);

        // Variable declaration (with Student ID)
        double incomeM25W7502;
        int creditScoreM25W7502;
        int ageM25W7502;

        // Taking input from user
        System.out.print("Enter your annual income (Yen): ");
        incomeM25W7502 = input.nextDouble();

        System.out.print("Enter your credit score: ");
        creditScoreM25W7502 = input.nextInt();

        System.out.print("Enter your age: ");
        ageM25W7502 = input.nextInt();

        // Loan eligibility logic using nested if-else
        if (incomeM25W7502 >= 50000 && creditScoreM25W7502 >= 700 
                && ageM25W7502 >= 21 && ageM25W7502 <= 68) {

            System.out.println("Eligible for Loan");

        } 
        else if (incomeM25W7502 >= 40000 && incomeM25W7502 <= 59999) {

            if (creditScoreM25W7502 > 900) {
                System.out.println("Eligible for Loan");
            } 
            else {
                System.out.println("Not Eligible for Loan");
            }

        } 
        else {
            System.out.println("Not Eligible for Loan");
        }

        // Closing scanner
        input.close();
    }
}