#include <stdio.h>
int main(){
    int num = 1234;
     int rever = 0;
    //  int temp = rever;
    while(num!=0){
        int rem = num%10;
        rever = rever * 10 + rem;
        num = num /10;
    };
    printf("%d",rever);
}