#include<stdio.h>
bool search(int *stack,int num)
{
    for(int i=1;i<=stack[0];i++)
    {
        if(stack[i]==num) return true;
    }
    return false;
}
void insert(int *stack,int num)
{
    stack[0]++;
    stack[stack[0]]=num;
}
int pop(int *stack)
{
    int num=stack[stack[0]--];
    return num;
}
void print(int *stack)
{
    for(int i=1;i<=stack[0];i++)
        printf("%c ",'A'+stack[i]);
}
int main(){
    int num,i,j,arr[20][20],stack[30];
    printf("Enter the number of nodes\t");
    scanf("%d",&num);
    printf("Enter the edge\n ");
    for(i=0;i<num;i++) printf(" %c",i+'A');puts("");
    int count=0;
    for(i=0;i<num;i++)
    {
        printf("%c ",i+'A');
        for(j=0;j<num;j++)
        {
            scanf("%d",&arr[i][j]);
            if(arr[i][j]) count++;
        }
    }
    bool flag=false;
    stack[0]=0;
    i=0;
    int pre;
    while(count--)
    {
        for(j=0;j<num;j++)
        {
            if(arr[i][j]!=0)
            {
                if(!(search(stack,i)))
                        insert(stack,i);
                if(search(stack,j))
                {
                    if(j==pre) continue;
                    printf("Cycle  ");
                    print(stack);printf("%c     %d\n",j+'A',i);
                }
                else
                {
                    pre=i;
                    i=j;
                    j=-1;
                }
            }
        }
    }
    for(i=1;i<=stack[0];i++)    printf("%d ",stack[i]);
    return 0;
}
