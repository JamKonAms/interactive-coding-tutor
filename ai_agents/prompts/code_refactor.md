# Code Refactoring Prompt

## Purpose
Improve code quality, readability, and performance while maintaining functionality.

## Usage
- Command: `/refactor`
- Highlight the code you want to improve
- Optionally specify refactoring goals

## Input Format
```python
# Highlight code to refactor:
def your_code():
    # ... code to improve ...

# Optionally add comment with specific goals:
# Goal: Improve performance
# Goal: Add type hints
# Goal: Follow PEP 8
```

## Parameters
- **Language**: Programming language being used
- **Goals**: Specific improvement targets
- **Context**: How the code is used
- **Style Guide**: Preferred coding standards

## Example Interactions

### 1. Basic Refactoring
**User Input:**
```python
def calc(lst):
    x = 0
    for i in lst:
        x = x + i
    return x/len(lst)
```

**Assistant Response:**
```
Here's the refactored version with improvements:

```python
def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers to average
        
    Returns:
        The arithmetic mean of the numbers
        
    Raises:
        ZeroDivisionError: If the list is empty
    """
    if not numbers:
        raise ZeroDivisionError("Cannot calculate average of empty list")
    
    return sum(numbers) / len(numbers)
```

Improvements made:
1. Descriptive function and parameter names
2. Type hints for better clarity
3. Docstring with complete documentation
4. Input validation
5. Used built-in sum() for efficiency
6. Follows PEP 8 style guide
```

### 2. Performance Optimization
**User Input:**
```python
# Goal: Improve performance
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates
```

**Assistant Response:**
```
Here's an optimized version using a set for O(n) performance:

```python
def find_duplicates(items: list) -> list:
    """Find duplicate items in a list efficiently.
    
    Uses a set for O(n) time complexity instead of O(n²).
    
    Args:
        items: List to check for duplicates
        
    Returns:
        List of items that appear more than once
    """
    seen = set()
    duplicates = set()
    
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            
    return list(duplicates)
```

Improvements made:
1. Used sets for O(n) time complexity
2. Removed nested loops
3. Added type hints and documentation
4. More memory efficient
5. Clearer variable names
```

## Response Format
The assistant will:
1. Provide refactored code
2. List improvements made
3. Explain key changes
4. Suggest additional enhancements
5. Note any trade-offs

## Caveats & Limitations
- Primarily focused on Python best practices
- May suggest trade-offs between readability and performance
- Some refactorings may need broader codebase context
- Complex optimizations may require profiling data

## Best Practices
1. **Code Selection**
   - Include complete functions/classes
   - Show usage context if relevant
   - Indicate specific goals

2. **Refactoring Goals**
   - Readability
   - Performance
   - Maintainability
   - Error handling
   - Documentation

3. **Style Guidelines**
   - Follow language conventions
   - Use consistent naming
   - Add appropriate comments
   - Include type hints

## Integration with Other Commands
- Use `/explain` to understand the changes
- Use `/debug` if refactoring introduces issues
- Use `/test` to validate refactored code
- Use `/generate` for alternative approaches

Remember: The Code Refactoring Assistant improves working code. For broken code, use `/debug` first. 