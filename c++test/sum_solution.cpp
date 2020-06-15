#include <iostream>
using namespace std;
int main(){
    int a  = 4;
    cout<<sizeof(a)<<endl;
    int b[1][2];
    cout<<sizeof(b)<<endl;
    int c[3][4];
    cout<<sizeof(c)<<endl;
    // 计算1+2+...+n 不使用if for 等关键字的情况下
    int n = 10;
    char d[n][n+1];
    cout<<(sizeof(d)>>1)<<endl;

    // 也可以用int 
    int e[n][n+1];
    cout<<sizeof(e)<<endl;
    cout<<(sizeof(e)>>3)<<endl;
}