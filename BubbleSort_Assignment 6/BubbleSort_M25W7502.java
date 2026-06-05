import java.util.Arrays;

public class BubbleSort_M25W7502 {

    // Name: Rahman Md Shazedur
    // Student ID: M25W7502

    static void bubbleSort(int arr[]) {

        int n = arr.length;

        for(int i=0;i<n-1;i++){

            for(int j=0;j<n-i-1;j++){

                if(arr[j]>arr[j+1]){

                    int temp=arr[j];

                    arr[j]=arr[j+1];

                    arr[j+1]=temp;
                }
            }
        }
    }

    static void bubbleSortString(String arr[]){

        int n=arr.length;

        for(int i=0;i<n-1;i++){

            for(int j=0;j<n-i-1;j++){

                if(arr[j].compareTo(arr[j+1])>0){

                    String temp=arr[j];

                    arr[j]=arr[j+1];

                    arr[j+1]=temp;
                }
            }
        }
    }

    public static void main(String[] args){

        int numbers[]={7,3,9,1};

        System.out.println("Before Numeric Sort:");
        System.out.println(Arrays.toString(numbers));

        bubbleSort(numbers);

        System.out.println("After Numeric Sort:");
        System.out.println(Arrays.toString(numbers));

        String fruits[]={
                "Mango",
                "Apple",
                "Banana"
        };

        System.out.println("\nBefore Alphabet Sort:");
        System.out.println(Arrays.toString(fruits));

        bubbleSortString(fruits);

        System.out.println("After Alphabet Sort:");
        System.out.println(Arrays.toString(fruits));
    }
}