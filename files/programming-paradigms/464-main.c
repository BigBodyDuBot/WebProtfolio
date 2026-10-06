#include <stdio.h>

int main() {

    // The variable i is declared inside the for loop
    for (int i = 0; i < 3; i++) {
        printf("Inside loop i = %d\n", i);
    }

    // Now we try to use i outside the loop
    // This line should cause a compiler error
    printf("Outside loop i = %d\n", i);

    return 0;
}