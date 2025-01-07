# Content Generation Prompt

## Purpose
Generate lesson content, code examples, practice exercises, and documentation tailored to learning goals and skill levels.

## Usage
- Command: `/generate`
- Specify content type and parameters
- Optionally include theme or context

## Input Format
```
/generate [content_type] [parameters]

Examples:
/generate exercise loops intermediate
/generate example recursion beginner
/generate lesson_plan data_structures advanced
```

## Parameters
- **Content Type**: Exercise, example, lesson, etc.
- **Topic**: Programming concept to cover
- **Skill Level**: Beginner/intermediate/advanced
- **Theme**: Optional learning theme

## Example Interactions

### 1. Generate Practice Exercise
**User Input:**
```
/generate exercise
Topic: List comprehension
Level: Intermediate
Theme: Space exploration
```

**Assistant Response:**
```
# Space Mission Data Processing Exercise

## Background
You're a data analyst for the Galactic Space Agency. You have a list of recent space missions containing launch dates, destinations, and mission durations.

## Task
Using list comprehensions, create filtered lists of missions based on various criteria.

```python
missions = [
    ("Mars Explorer", 2030, 300),
    ("Luna Base", 2028, 150),
    ("Saturn Ring Study", 2035, 800),
    ("Venus Survey", 2029, 200)
]

# 1. Create a list of mission names for missions longer than 200 days
long_missions = # Your code here

# 2. Create a list of (name, year) tuples for missions before 2030
early_missions = # Your code here

# 3. Create a list of mission durations in years (divide days by 365)
mission_years = # Your code here
```

## Expected Output
```python
long_missions == ["Mars Explorer", "Saturn Ring Study"]
early_missions == [("Luna Base", 2028), ("Venus Survey", 2029)]
mission_years == [0.82, 0.41, 2.19, 0.55]
```

## Hints
1. Remember list comprehension syntax: [expression for item in list if condition]
2. You can unpack tuples in list comprehensions
3. Use float division (/) for years calculation
```

### 2. Generate Code Example
**User Input:**
```
/generate example
Topic: Decorators
Level: Beginner
```

**Assistant Response:**
```
# Understanding Python Decorators

Here's a simple example showing how decorators can time function execution:

```python
import time
from functools import wraps

def timer_decorator(func):
    """A decorator that prints how long a function takes to run."""
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Record start time
        start_time = time.time()
        
        # Run the function
        result = func(*args, **kwargs)
        
        # Calculate duration
        duration = time.time() - start_time
        
        # Print the timing
        print(f"{func.__name__} took {duration:.2f} seconds")
        
        return result
    
    return wrapper

# Example usage:
@timer_decorator
def calculate_sum(n):
    """Calculate sum of numbers from 1 to n."""
    return sum(range(1, n + 1))

# Try it out:
result = calculate_sum(1000000)
print(f"Sum: {result}")
```

## Key Points:
1. Decorators are functions that modify other functions
2. They use the `@` syntax for easy application
3. `@wraps` preserves the original function's metadata
4. The wrapper function can add behavior before/after

## Try It:
1. Run this code and observe the timing output
2. Modify the decorator to also show memory usage
3. Create a decorator that counts function calls
```

## Response Format
The assistant will:
1. Generate requested content
2. Provide clear instructions/explanations
3. Include examples and expected outputs
4. Add helpful hints or tips
5. Suggest follow-up exercises

## Caveats & Limitations
- Content focuses on Python programming
- Examples are educational, not production code
- May need adaptation for specific contexts
- Generated content follows standard curriculum

## Best Practices
1. **Content Requests**
   - Specify clear learning objectives
   - Indicate target skill level
   - Mention preferred theme if any

2. **Exercise Design**
   - Start with context/background
   - Provide clear requirements
   - Include test cases
   - Offer progressive hints

3. **Code Examples**
   - Show practical use cases
   - Include comments
   - Demonstrate best practices
   - Build on fundamentals

## Integration with Other Commands
- Use `/explain` to understand examples
- Use `/debug` to fix exercise attempts
- Use `/refactor` to improve solutions
- Use `/test` to validate exercises

Remember: The Content Generation Assistant creates educational materials that align with your learning goals and preferences.