
/*
Name: Rahman Md Shazedur
ID: M25W7502
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>



// Student Information 
char RahmanMdShazedur_Name[] = "Rahman Md Shazedur";

char M25W7502_ID[] = "M25W7502";



struct Node_M25W7502
{
    char data_M25W7502[50];

    struct Node_M25W7502 *next_M25W7502;
};



struct Node_M25W7502 *head_M25W7502 = NULL;



// Create Node
struct Node_M25W7502* createNode_M25W7502(char value_M25W7502[])
{
    struct Node_M25W7502 *newNode_M25W7502;

    newNode_M25W7502 =
    (struct Node_M25W7502*)malloc(sizeof(struct Node_M25W7502));

    strcpy(newNode_M25W7502->data_M25W7502, value_M25W7502);

    newNode_M25W7502->next_M25W7502 = NULL;

    return newNode_M25W7502;
}



// Display List
void display_M25W7502()
{
    struct Node_M25W7502 *temp_M25W7502 = head_M25W7502;

    printf("\nLinked List:\n");

    while(temp_M25W7502 != NULL)
    {
        printf("%s -> ", temp_M25W7502->data_M25W7502);

        temp_M25W7502 = temp_M25W7502->next_M25W7502;
    }

    printf("NULL\n");
}



// Insert Node
void insert_M25W7502()
{
    char value_M25W7502[50];

    printf("Enter String: ");

    scanf("%s", value_M25W7502);

    struct Node_M25W7502 *newNode_M25W7502;

    newNode_M25W7502 =
    createNode_M25W7502(value_M25W7502);

    newNode_M25W7502->next_M25W7502 = head_M25W7502;

    head_M25W7502 = newNode_M25W7502;

    printf("Inserted Successfully\n");
}



// Delete Node
void delete_M25W7502()
{
    if(head_M25W7502 == NULL)
    {
        printf("List Empty\n");

        return;
    }

    struct Node_M25W7502 *temp_M25W7502 = head_M25W7502;

    head_M25W7502 = head_M25W7502->next_M25W7502;

    free(temp_M25W7502);

    printf("Deleted Successfully\n");
}



// Modify Node
void modify_M25W7502()
{
    int position_M25W7502, i_M25W7502;

    char value_M25W7502[50];

    struct Node_M25W7502 *temp_M25W7502 = head_M25W7502;

    printf("Enter Position: ");

    scanf("%d", &position_M25W7502);

    printf("Enter New String: ");

    scanf("%s", value_M25W7502);

    for(i_M25W7502 = 1;
        i_M25W7502 < position_M25W7502
        && temp_M25W7502 != NULL;
        i_M25W7502++)
    {
        temp_M25W7502 =
        temp_M25W7502->next_M25W7502;
    }

    if(temp_M25W7502 == NULL)
    {
        printf("Invalid Position\n");

        return;
    }

    strcpy(temp_M25W7502->data_M25W7502,
           value_M25W7502);

    printf("Modified Successfully\n");
}



// Recursive Reverse
struct Node_M25W7502*
reverse_M25W7502(struct Node_M25W7502 *current_M25W7502)
{
    if(current_M25W7502 == NULL
       || current_M25W7502->next_M25W7502 == NULL)
    {
        return current_M25W7502;
    }

    struct Node_M25W7502 *newHead_M25W7502;

    newHead_M25W7502 =
    reverse_M25W7502(current_M25W7502->next_M25W7502);

    current_M25W7502->next_M25W7502->next_M25W7502 =
    current_M25W7502;

    current_M25W7502->next_M25W7502 = NULL;

    return newHead_M25W7502;
}



int main()
{
    int choice_M25W7502, i_M25W7502;

    char value_M25W7502[50];

    printf("Student Name: %s\n", RahmanMdShazedur_Name);

    printf("Student ID: %s\n", M25W7502_ID);

    printf("\nEnter 17 Strings:\n");

    for(i_M25W7502 = 0; i_M25W7502 < 17; i_M25W7502++)
    {
        scanf("%s", value_M25W7502);

        struct Node_M25W7502 *newNode_M25W7502;

        newNode_M25W7502 =
        createNode_M25W7502(value_M25W7502);

        if(head_M25W7502 == NULL)
        {
            head_M25W7502 = newNode_M25W7502;
        }
        else
        {
            struct Node_M25W7502 *temp_M25W7502 =
            head_M25W7502;

            while(temp_M25W7502->next_M25W7502 != NULL)
            {
                temp_M25W7502 =
                temp_M25W7502->next_M25W7502;
            }

            temp_M25W7502->next_M25W7502 =
            newNode_M25W7502;
        }
    }

    do
    {
        printf("\n1.Display\n2.Insert\n3.Delete\n4.Modify\n5.Reverse\n6.Exit\n");

        printf("Choice: ");

        scanf("%d", &choice_M25W7502);

        switch(choice_M25W7502)
        {
            case 1:

                display_M25W7502();

                break;

            case 2:

                insert_M25W7502();

                break;

            case 3:

                delete_M25W7502();

                break;

            case 4:

                modify_M25W7502();

                break;

            case 5:

                head_M25W7502 =
                reverse_M25W7502(head_M25W7502);

                printf("Reversed Successfully\n");

                break;

            case 6:

                printf("Program Exit\n");

                break;

            default:

                printf("Invalid Choice\n");
        }

    } while(choice_M25W7502 != 6);

    return 0;
}