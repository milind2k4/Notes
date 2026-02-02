
### Brute Force
Start searching from the left as well as right, when we find the first occurrence on both sides, then stop.

This gives `O(2n)` time complexity.

### Linear Time Complexity

Start searching from the left, but keep a flag.

```cpp
first = last = -1;
flag = 0;

for (i -> n){
	if (arr[i] == x && flag == 0){
		first = i;
	}
	if (arr[i] == x){
		last = i;
	}
}
```

### Modified Binary Search 

We make two functions,

```c
int first(){
	// rest is normal binary search 
	int first = -1;
	while (left <= right){
		if (a[mid] == x){
			first = mid;
			high = mid - 1;
		}
		.
		.
		.
	}
	return first;
}

int last(){
	int last = -1;
	// rest is normal binary search 
	while (left <= right){
		if (a[mid] == x){
			last = mid;
			low = mid + 1;
		}
		.
		.
		.
	}
	return last;
}
```