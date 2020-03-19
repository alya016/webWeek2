#include <iostream>
#include <cmath>
#include <stdio.h>

using namespace std;
int main() {
int a,b,c,d,r,r2,r3;

cin >> a >> b >> c >> d;

r=min(a,b);
r2=min(r,c);
r3=min(r2,d);

cout << r3;
return 0;
}
