// program to find number of inversion pairs
#include<stdio.h>
int main()
{
    printf("enter number of elements you want to enter:");
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    int inv=0;
    for(int i=0;i<n;i++)
    {
        for(int j=i;j<n;j++)
        {
            if(arr[i]>arr[j])
            {
                if(i<j)
                {
                    inv++;
                }
            }
        }
    }
    printf("\nnumber of inversion pair possible for given array is %d",inv);
}