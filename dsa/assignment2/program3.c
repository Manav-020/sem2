#include<stdio.h>
struct bankmgmt{
    int accnumber;
    char cusname[100];
    int avlbalance;
    char acctype[20];
};
int main()
{
    struct bankmgmt c1;
    printf("enter account number:");
    scanf("%d",&c1.accnumber);
    printf("\nenter name:");
    char c;
    scanf("%c",&c);
    fgets(c1.cusname,100,stdin);
    printf("\nenter balance:");
    scanf("%d",&c1.avlbalance);
    printf("\nenter account type:");
    scanf("%s",&c1.acctype);
    int n,i,w;
    while (i=1)
    {
        printf("\n3press 1 to withdraw\npress 2 to deposite\npress 3 to check balance\npress 4 to exit\n");
        scanf("%d",&n);
        switch(n)
        {
            case 1: printf("enter amount you want to withdraw:");
                    w=0;
                    scanf("%d",&w);
                    if(w>c1.avlbalance)
                    {
                        printf("insufficient funds");
                    }
                    else
                    {
                        printf("name:%s\t",c1.cusname);
                        printf("account number:%d\t",c1.accnumber);
                        printf("available balance:%d\t",c1.avlbalance-w);
                        printf("account type:%s\t",c1.acctype);
                    }
            case 2: printf("enter amount you want to deposite:");
                    w=0;
                    scanf("%d",&w);
                    printf("name:%s\t",c1.cusname);
                    printf("account number:%d\t",c1.accnumber);
                    printf("available balance:%d\t",c1.avlbalance+w);
                    printf("account type:%s\t",c1.acctype);
            case 3: printf("your bank details are");
                    printf("name:%s\t",c1.cusname);
                    printf("account number:%d\t",c1.accnumber);
                    printf("available balance:%d\t",c1.avlbalance);
                    printf("account type:%s\t",c1.acctype);
            case 4: break;
            default: printf("invalid operation\n");
        }
    }
    printf("end");
}
