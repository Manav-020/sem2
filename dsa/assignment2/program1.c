#include<stdio.h>
#include<stdlib.h>
void read(int **a)
{
    printf("\nenter element of matrix:\n");
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            scanf("%d",(*(a+i)+j));
        }
    }
    printf("matrix is\n");
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            printf("%d\t",*(*(a+i)+j));
        }
        printf("\n");
    }
    printf("***********************\n***********************");
}
void multi(int **a,int**b)
{
    int x,y;
    int c[3][3];
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            c[i][j]=0;
            for(int k=0;k<3;k++)
            {
                x=*(*(a+i)+k);
                y=*(*(b+k)+j);
                c[i][j]=c[i][j]+(x*y);
            }
        }
    }
    printf("\nproduct of two matrix is\n");
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            printf("%d\t",c[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    int *a[3],*b[3];
    for(int i=0;i<3;i++)
    {
        a[i]=(int*)calloc(3,sizeof(int));
        b[i]=(int*)calloc(3,sizeof(int));
    }
    read(a);
    read(b);
    multi(a,b);
    
}