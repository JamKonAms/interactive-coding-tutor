# Debugging Assistant Prompt

## Purpose
Help identify and fix code issues, analyze error messages, and provide debugging strategies.

## Usage
- Command: `/debug`
- Highlight the problematic code or error message
- Include relevant context (e.g., expected behavior)

## Input Format
```python
# Highlight code with error:
def problematic_code():
    # ... code with issue ...
    
# Or highlight error message:
"""
TypeError: cannot concatenate 'str' and 'int' objects
"""
```

## Parameters
- **Language**: Programming language being used
- **Error Type**: Syntax, runtime, logical, etc.
- **Context**: What the code should do
- **Environment**: Python version, relevant packages

## Example Interactions

### 1. Syntax Error
**User Input:**
```python
def calculate_average(numbers)
    total = 0
    for num in numbers
        total += num
    return total / len(numbers)
```

**Assistant Response:**
```
I've identified two syntax errors:

1. Missing colon after function definition (line 1)
   - Current: def calculate_average(numbers)
   - Fix:     def calculate_average(numbers):
   
2. Missing colon after for loop (line 3)
   - Current: for num in numbers
   - Fix:     for num in numbers:

Here's the corrected code:
```python
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
```

Try this version and let me know if you need any clarification!
```

### 2. Runtime Error
**User Input:**
```
TypeError: unsupported operand type(s) for +: 'int' and 'str'

# In this code:
def add_numbers(a, b):
    return a + b

result = add_numbers(5, "10")
```

**Assistant Response:**
```
This is a type mismatch error. You're trying to add an integer (5) and a string ("10").

Quick fix:
```python
# Convert the string to an integer
result = add_numbers(5, int("10"))
```

For better robustness, add type checking:
```python
def add_numbers(a, b):
    # Convert strings to integers if possible
    if isinstance(a, str):
        a = int(a)
    if isinstance(b, str):
        b = int(b)
    return a + b
```

This version will handle both integers and numeric strings.
```

## Response Format
The assistant will:
1. Identify the type of error
2. Explain the cause
3. Provide a solution with:
   - Fixed code
   - Explanation of changes
   - Prevention tips
4. Suggest best practices

## Caveats & Limitations
- Currently optimized for Python
- JavaScript/TypeScript support is basic
- Some language-specific features may need clarification
- Complex runtime errors may need more context

## Best Practices
1. **Error Messages**
   - Include the full error message
   - Show the line number
   - Provide the stack trace if available

2. **Code Context**
   - Include enough code for context
   - Show relevant variable values
   - Explain expected behavior

3. **Follow Up**
   - Test the suggested fix
   - Ask for clarification if needed
   - Share the results

## Integration with Other Commands
- Use `/explain` to understand the fixed code
- Use `/refactor` to improve the solution
- Use `/test` to validate the fix
- Use `/generate` for additional examples

Remember: The Debugging Assistant works best when provided with clear error messages and sufficient context about what the code should do. 