#include<stdio.h>

int main(){
    int n,sum =0;
    printf("请输入n:");
    scanf("%d",&sum);
    for(int i=1;i<=n;i++)
        sum += i;
    printf("%d",sum);

    return 0;

}
