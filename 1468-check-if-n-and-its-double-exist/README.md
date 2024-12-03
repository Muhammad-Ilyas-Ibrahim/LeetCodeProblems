<h2><a href="https://leetcode.com/problems/check-if-n-and-its-double-exist">Check If N and Its Double Exist</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an array <code>arr</code> of integers, check if there exist two indices <code>i</code> and <code>j</code> such that :</p>

<ul>
	<li><code>i != j</code></li>
	<li><code>0 &lt;= i, j &lt; arr.length</code></li>
	<li><code>arr[i] == 2 * arr[j]</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [10,2,5,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,1,7,11]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no i and j that satisfy the conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 500</code></li>
	<li><code>-10<sup>3</sup> &lt;= arr[i] &lt;= 10<sup>3</sup></code></li>
</ul>


--- 

# **Algorithm Explanation and Dry Run**  

## Steps :
1. **Initialize an empty list** to keep track of visited numbers.
2. **Loop through each number** in the input array.
3. **Check Conditions**:
   - **a. First condition**: `(num * 2 in visited)`
     - Check if the double of the current number exists in the visited list.
     - Example: If the current number is `5`, check if `10` exists in the visited list.
   - **b. Second condition**: `(num % 2 == 0 and num // 2 in visited)`
     - Check if the current number is divisible by `2`, and if half of the current number exists in the visited list.
     - Example: If the current number is `10`, check if `5` exists in the visited list.
4. **If either condition is satisfied**, return `True`.
5. **Append the current number** to the visited list after checking the conditions.
6. **If the loop finishes without finding a valid pair**, return `False`.

---

## Dry Run Example

### Test Case:  
Input: `arr = [10, 2, 5, 3]`  

---

### Step-by-Step Execution:

**Initialization:**  
`visited = []` (empty at the start)

---

**Iteration 1**:  
- Current number: `10`  
- Condition 1: `10 * 2 = 20`, check if `20` is in `visited`. → **False**.  
- Condition 2: `10 % 2 == 0` and `10 // 2 = 5`, check if `5` is in `visited`. → **False**.  
- Action: Append `10` to `visited`.  
  **Visited = [10]**

---

**Iteration 2**:  
- Current number: `2`  
- Condition 1: `2 * 2 = 4`, check if `4` is in `visited`. → **False**.  
- Condition 2: `2 % 2 == 0` and `2 // 2 = 1`, check if `1` is in `visited`. → **False**.  
- Action: Append `2` to `visited`.  
  **Visited = [10, 2]**

---

**Iteration 3**:  
- Current number: `5`  
- Condition 1: `5 * 2 = 10`, check if `10` is in `visited`. → **True**!  
- **Result**: The function returns `True` because `10` is the double of `5`.

---

### Explanation of the Result:
The function stops at **Iteration 3** because it finds a pair (`5` and `10`) that satisfies the condition:  
`10` is in `visited`, and it is double the current number `5`.

---

## Summary:
- The function efficiently checks the conditions using the `visited` list and exits as soon as a valid pair is found.  
- **Output for `arr = [10, 2, 5, 3]`:** `True`.

