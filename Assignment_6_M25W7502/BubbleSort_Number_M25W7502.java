import java.util.Arrays;

public class BubbleSort_Number_M25W7502 {

    // Name: Rahman Md Shazedur
    // Student ID: M25W7502

    static void bubbleSort(int numbers[]) {

        int n=numbers.length;

        for(int i=0;i<n-1;i++){

            for(int j=0;j<n-i-1;j++){

                if(numbers[j]>numbers[j+1]){

                    int temp=numbers[j];

                    numbers[j]=numbers[j+1];

                    numbers[j+1]=temp;

                }
            }
        }
    }

    public static void main(String[] args){

        int numbers[]={7,3,9,1};

        System.out.println(
        "Name: Rahman Md Shazedur");

        System.out.println(
        "Student ID: M25W7502");

        System.out.println(
        Arrays.toString(numbers));

        bubbleSort(numbers);

        System.out.println(
        Arrays.toString(numbers));

    }
}