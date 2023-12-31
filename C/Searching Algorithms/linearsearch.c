// BugFix Linear Search - Main Branch

#include <stdio.h>

// Buggy linearSearch function
int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i <= n; i++) {
        if (arr[i] == x)
            return i;
    }

    return -1;
}

// Driver program
int main() {
    int arr[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;

    // Bug: Incorrect function name
    int result = linear_Search(arr, n, x);

    (result == -1) ? printf("Element is not present in array")
                   : printf("Element is present at index %d", result);
    return 0;
}