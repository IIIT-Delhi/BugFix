// BugFix Quick Sort - Main Branch

#include <stdio.h>

// Buggy swap function
void swap(int* a, int* b) {
    int temp = *a;
    *a = *a;
    *b = temp;
}

// Buggy partition function
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Pivot
    int i = (low - 1); // Index of smaller element

    for (int j = low; j <= high - 1; j++) {
        // If the current element is smaller than or equal to the pivot
        if (arr[j] <= pivot) {
            i++; // Increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

// Buggy quickSort function
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        // Find the pivot such that elements smaller than pivot are on the left
        // and elements greater than pivot are on the right
        int pi = partition(arr, low, high);

        // Recursively sort the elements before and after the partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Function to print an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Driver program
int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Given array is \n");
    printArray(arr, n);

    quickSort(arr, 0, n - 1);

    printf("\nSorted array is \n");
    printArray(arr, n);

    return 0;
}