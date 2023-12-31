// BugFix Linear Search - Solution Branch

#include <stdio.h>

// Fixed binarySearch function
int binarySearch(int arr[], int left, int right, int x) {
    if (right >= left) {
        int mid = left + (right - left) / 2;

        // If the element is present at the middle
        if (arr[mid] == x)
            return mid;

        // If the element is not present in the right subarray
        if (arr[mid] > x)
            return binarySearch(arr, left, mid - 1, x);

        // If the element is not present in the left subarray
        return binarySearch(arr, mid + 1, right, x);
    }

    // Element is not present in the array
    return -1;
}

// Driver program
int main() {
    int arr[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;

    // Corrected function name
    int result = binarySearch(arr, 0, n - 1, x);

    (result == -1) ? printf("Element is not present in array")
                   : printf("Element is present at index %d", result);
    return 0;
}