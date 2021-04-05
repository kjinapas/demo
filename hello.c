#include<stdio.h>
int main (){
    struct Bboy{
        char name[20];
        int age;
        char aka[20];
    };
    struct Bboy Cd={"kanokpon",30,"Bboy CD"};
    
    printf("Your Aka is : %s !!!",Cd.aka);
    
}