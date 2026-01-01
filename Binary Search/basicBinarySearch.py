def binary_search(arr, target):
    """
    Binary Search Algorithm
    
    Searches for a target value in a SORTED array using the divide-and-conquer approach.
    Time Complexity: O(log n) - much faster than linear search O(n)
    Space Complexity: O(1) - only uses a constant amount of extra space
    
    Args:
        arr: A sorted list of comparable elements
        target: The value we're searching for
    
    Returns:
        The index of target if found, -1 otherwise
    """
    
    # Initialize two pointers: left at start, right at end
    left = 0
    right = len(arr) - 1
    
    # Continue searching while the search space is valid
    while left <= right:
        # Find the middle index (prevents integer overflow in some languages)
        mid = left + (right - left) // 2
        
        # Check if we found the target
        if arr[mid] == target:
            return mid  # Target found! Return its index
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1  # Move left pointer to mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1  # Move right pointer to mid - 1
    
    # Target not found in the array
    return -1


# Example usage and visualization
if __name__ == "__main__":
    # Example 1: Target exists in array
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 11
    
    result = binary_search(sorted_array, target)
    print(f"Searching for {target} in {sorted_array}")
    print(f"Result: Index {result} (Value: {sorted_array[result]})" if result != -1 else "Not found")
    print()
    
    # Example 2: Target doesn't exist
    target = 8
    result = binary_search(sorted_array, target)
    print(f"Searching for {target} in {sorted_array}")
    print(f"Result: {result} (Not found)")
    print()
    
    # Visual walkthrough for target = 11
    print("=== Step-by-step walkthrough for searching 11 ===")
    print("Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]")
    print("Indices: 0  1  2  3  4   5   6   7   8   9")
    print()
    print("Step 1: left=0, right=9, mid=4 → arr[4]=9 < 11")
    print("        Move left to 5 (eliminate left half)")
    print()
    print("Step 2: left=5, right=9, mid=7 → arr[7]=15 > 11")
    print("        Move right to 6 (eliminate right half)")
    print()
    print("Step 3: left=5, right=6, mid=5 → arr[5]=11 == 11")
    print("        Found! Return index 5")
    print()
    print("Total comparisons: 3 (vs 6 with linear search)")