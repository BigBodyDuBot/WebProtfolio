#include <iostream>
using namespace std;

int main() {

    for (int i = 0; i < 3; i++) {
        cout << "Inside loop i = " << i << endl;
    }

    // Try to use i after the loop
    cout << "Outside loop i = " << i << endl;

    return 0;
}