// Name: Rahman Md Shazedur
// Student ID: M25W7502

import java.util.Scanner;

public class AverageCalculator_M25W7502 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first decimal number: ");
        double num1_M25W7502 = sc.nextDouble();

        System.out.print("Enter second decimal number: ");
        double num2_M25W7502 = sc.nextDouble();

        System.out.print("Enter third decimal number: ");
        double num3_M25W7502 = sc.nextDouble();

        int int1 = (int) num1_M25W7502;
        int int2 = (int) num2_M25W7502;
        int int3 = (int) num3_M25W7502;

        double avg_M25W7502 = (int1 + int2 + int3) / 3.0;

        int finalResult_M25W7502 = (int) Math.ceil(avg_M25W7502);

        System.out.println("Rounded Average = " + finalResult_M25W7502);

        sc.close();
    }
}