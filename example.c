#include<stdio.h>
int main(){

    int a[100], b[100], c[100];

    for(int i=0;i<100;i++){
        c[i] = a[i] + b[i];
    }

    return 0;
}