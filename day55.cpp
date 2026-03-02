#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function   
   int add;
   add = *a + *b;
   
   int diff;
   diff = *a - *b;
   
   if (diff < 0){
    diff = -diff;
   }
   
   *a = add;
   *b = diff;
   
   
    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}