# 🚀 Slash Commands in Cursor

This guide explains how to use AI-powered slash commands to enhance your learning experience.

## 🎯 Available Commands

| Command | Purpose | When to Use | Example |
|---------|---------|-------------|----------|
| `/learn` | Get learning guidance | Need direction or have questions | "What topic should I focus on next?" |
| `/generate` | Create content or examples | Want practice material | "Create an exercise about Python loops" |
| `/debug` | Fix code issues | Code isn't working | Highlight error message and use command |
| `/refactor` | Improve code quality | Code works but needs improvement | Highlight function and use command |
| `/explain` | Understand code | Need to grasp concepts | Highlight code snippet and use command |
| `/test` | Create test cases | Want to validate code | Highlight function and use command |

## 💡 Using Commands in Cursor

### Basic Usage
1. Type `/` in any editor or chat window
2. Select a command from the dropdown
3. Follow the command-specific instructions

### Code-Specific Commands
1. Highlight the relevant code
2. Type the appropriate command
3. Review and apply suggestions

## 🎯 Command-Specific Guidelines

### 1. Learning Assistant (`/learn`)
- **Best for:**
  - Getting personalized guidance
  - Understanding learning paths
  - General programming questions
- **Example:**
  ```
  /learn What should I learn after mastering loops?
  ```

### 2. Content Generation (`/generate`)
- **Best for:**
  - Creating practice exercises
  - Getting code examples
  - Expanding lesson content
- **Example:**
  ```python
  # Type /generate with this comment:
  # Create a beginner-friendly example of list comprehension
  ```

### 3. Debugging Assistant (`/debug`)
- **Best for:**
  - Error messages
  - Runtime issues
  - Syntax problems
- **Example:**
  ```python
  # Highlight problematic code:
  def calculate_average(numbers)
      return sum(numbers) / len(numbers)
  # Type /debug
  ```

### 4. Code Refactoring (`/refactor`)
- **Best for:**
  - Improving readability
  - Optimizing performance
  - Applying best practices
- **Example:**
  ```python
  # Highlight code to improve:
  def f(x,y):
      z=x+y
      return z
  # Type /refactor
  ```

### 5. Code Explanation (`/explain`)
- **Best for:**
  - Understanding code logic
  - Learning new concepts
  - Clarifying syntax
- **Example:**
  ```python
  # Highlight code to understand:
  [x for x in range(10) if x % 2 == 0]
  # Type /explain
  ```

### 6. Test Generation (`/test`)
- **Best for:**
  - Creating unit tests
  - Finding edge cases
  - Validating functions
- **Example:**
  ```python
  # Highlight function to test:
  def factorial(n):
      return 1 if n <= 1 else n * factorial(n-1)
  # Type /test
  ```

## 🔄 Common Command Chains

### Fixing and Improving Code
1. Use `/debug` to fix errors
2. Use `/refactor` to improve the working code
3. Use `/test` to validate changes

### Learning New Concepts
1. Use `/learn` to identify topic
2. Use `/generate` to see examples
3. Use `/explain` to understand details

## ⚠️ Important Notes

1. **Code Selection**
   - Highlight complete code blocks
   - Include necessary context
   - Remove irrelevant code

2. **Command Choice**
   - Use `/debug` only for errors
   - Use `/explain` for understanding
   - Use `/refactor` for improvements

3. **Best Practices**
   - Review suggestions before applying
   - Test changes thoroughly
   - Keep code selections focused

## 🔍 Troubleshooting

If commands aren't working:
1. Verify Cursor is up to date
2. Check your code selection
3. Try reloading Cursor
4. Ensure proper context is provided

## 🎓 Learning Tips

1. **Start Simple**
   - Begin with `/explain` to understand code
   - Use `/generate` for practice
   - Progress to `/refactor` as you learn

2. **Debug Effectively**
   - Highlight specific error messages
   - Include relevant code context
   - Follow suggested fixes step by step

3. **Improve Gradually**
   - Start with working code
   - Use `/refactor` for small improvements
   - Add tests as you go

Remember: These commands are tools to enhance your learning. They work best when used thoughtfully and in combination with your own understanding. 