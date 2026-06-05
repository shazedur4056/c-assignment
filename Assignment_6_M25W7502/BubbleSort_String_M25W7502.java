import java.util.Arrays;

public class BubbleSort_String_M25W7502 {

    // Name: Rahman Md Shazedur
    // Student ID: M25W7502

    static void bubbleSort(String fruits[]){

        int n=fruits.length;

        for(int i=0;i<n-1;i++){

            for(int j=0;j<n-i-1;j++){

                if(
                fruits[j]
                .compareTo(
                fruits[j+1]
                )>0){

                    String temp=
                    fruits[j];

                    fruits[j]=
                    fruits[j+1];

                    fruits[j+1]=
                    temp;

                }
            }
        }
    }

    public static void main(String[] args){

        String fruits[]={
        "Mango",
        "Apple",
        "Banana"
        };

        System.out.println(
        "Name: Rahman Md Shazedur");

        System.out.println(
        "Student ID: M25W7502");

        System.out.println(
        Arrays.toString(fruits));

        bubbleSort(fruits);

        System.out.println(
        Arrays.toString(fruits));
    }
}