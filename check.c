#include<stdio.h>
int main(){
    int row;
    int i,j;
    int chess=1;
    int columm;
    scanf("%d",&row);
    scanf("%d",&columm);
    for (i=0;i<row;i++){
        for(j=1;j<=columm;j++){
            if(chess%2!=0){
                printf("  ");
                chess++;
            }else{
                printf("X ");
                chess++;
            }

        }printf("\n");
    }
    
}