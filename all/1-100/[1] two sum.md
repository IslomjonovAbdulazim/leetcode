## Brute Force (Naive) Approach

### Idea
- Check all possible pairs in the array.
- For every element at index `i`, check every element at index `j` (`j > i`) to see if they sum to the target.
- **Time Complexity**: \( O(n^2) \)  
- **Space Complexity**: \( O(1) \)