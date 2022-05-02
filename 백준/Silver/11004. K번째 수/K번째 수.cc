#include <stdio.h>
#include <algorithm>

using namespace std;

int main(void) {
    int n, k;
    scanf("%d %d", &n, &k);
    int* arr = new int[n];
    
    for (int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    
    sort(arr, arr + n);
    printf("%d", arr[k-1]);
    
    return 0;
}