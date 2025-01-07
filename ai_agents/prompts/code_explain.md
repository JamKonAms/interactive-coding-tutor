# Code Explanation Prompt

## Purpose
Provide clear, in-depth explanations of code functionality, concepts, and patterns.

## Usage
- Command: `/explain`
- Highlight the code you want explained
- Optionally specify focus areas (e.g., "focus: memory usage")

## Input Format
```python
# Highlight code to explain:
def your_code():
    # ... code to understand ...

# Optionally add focus areas:
# Focus: Time complexity
# Focus: Design patterns
# Focus: Memory management
```

## Parameters
- **Language**: Programming language being explained
- **Focus**: Specific aspects to emphasize
- **Detail Level**: Basic/intermediate/advanced
- **Context**: How the code is used

## Example Interactions

### 1. Basic Function Explanation
**User Input:**
```python
@dataclass
class Point:
    x: float
    y: float
    
    def distance_to(self, other: 'Point') -> float:
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
```

**Assistant Response:**
```
Let's break this code down:

1. Class Definition:
   - Uses Python's `@dataclass` decorator
   - Automatically creates __init__, __repr__, etc.
   - Represents a 2D point with x,y coordinates

2. Type Annotations:
   - `x: float`: x-coordinate as decimal number
   - `y: float`: y-coordinate as decimal number
   - `other: 'Point'`: Another Point instance
   - `-> float`: Returns a decimal number

3. Method `distance_to`:
   - Calculates Euclidean distance between two points
   - Uses the formula: √((x₂-x₁)² + (y₂-y₁)²)
   - Returns distance as a float

Usage example:
```python
p1 = Point(0, 0)  # Origin
p2 = Point(3, 4)  # Point (3,4)
distance = p1.distance_to(p2)  # Returns 5.0
```
```

### 2. Algorithm Explanation
**User Input:**
```python
# Focus: Time complexity
def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
```

**Assistant Response:**
```
Binary Search Algorithm Explanation:

1. Purpose:
   - Efficiently finds an element in a sorted array
   - Returns index of target or -1 if not found

2. Algorithm Steps:
   a. Initialize pointers:
      - left: start of search range
      - right: end of search range
   
   b. While search range exists:
      - Calculate middle point
      - If target found, return its index
      - If target larger, search right half
      - If target smaller, search left half

3. Time Complexity: O(log n)
   - Each iteration halves the search space
   - For array size n, takes log₂(n) steps
   - Much faster than linear search O(n)

4. Requirements:
   - Array must be sorted
   - Elements must be comparable

Example walkthrough:
```python
arr = [1, 3, 5, 7, 9]
target = 7

# Step 1: mid = 2, arr[2] = 5 < 7
# Step 2: mid = 3, arr[3] = 7 (found!)
```
```

## Response Format
The assistant will:
1. Break down the code structure
2. Explain key concepts
3. Provide usage examples
4. Highlight important details
5. Answer follow-up questions

## Caveats & Limitations
- Explanations focus on Python concepts
- May need additional context for complex patterns
- Some language features may need references
- Advanced topics may require prerequisites

## Best Practices
1. **Code Selection**
   - Include complete, runnable snippets
   - Show relevant imports
   - Provide context if needed

2. **Questions**
   - Be specific about unclear parts
   - Mention your experience level
   - Ask for examples if needed

3. **Learning Path**
   - Start with basics
   - Build on fundamentals
   - Practice with examples

## Integration with Other Commands
- Use `/debug` for error explanations
- Use `/refactor` to improve code
- Use `/test` to verify understanding
- Use `/generate` for practice examples

Remember: The Code Explanation Assistant helps you understand not just what code does, but why and how it works. 