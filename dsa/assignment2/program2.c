#include <stdio.h> 
#include <stdlib.h> 
typedef struct { 
int *a; 
int *b; 
} str; 
int main() { 
str *s = (str *)malloc(sizeof(str)); 
    int n; 
    printf("Enter the size of the array: "); 
    scanf("%d", &n);  
    s->a = (int *)malloc(n * sizeof(int)); 
    s->b = (int *)malloc(n * sizeof(int)); 
    printf("Enter the elements of the array: \n"); 
    for (int i = 0; i < n; i++) { 
        scanf("%d", (s->a + i)); 
    }
    for (int i = 0; i < n; i++)  
    { 
        if (i % 2 == 0 || i>=n-1) 
        { 
            *(s->b + i) = *(s->a + i); 
        } 
        else 
        { 
            *(s->b + i) = *(s->a + i - 1) * *(s->a + i + 1); 
        }    
    } 
    printf("Modified array: \n"); 
    for (int i = 0; i < n; i++)  
    { 
        printf("%d ", *(s->b + i)); 
    }
    free(s->a); 
    free(s->b); 
    free(s); 
     
    return 0; 
}