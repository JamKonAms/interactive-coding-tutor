# 📚 Lesson Design Guide

## Overview
This guide establishes standards and best practices for creating lessons in our interactive coding curriculum. The curriculum is designed to work seamlessly with Cursor IDE and its AI-powered features.

## 🏷️ Content Classification

### Skill Level Tags
Each lesson must be tagged with one of these skill levels:
- 🌱 **Beginner** - No prior experience needed
- 🌿 **Intermediate** - Basic programming knowledge required
- 🌳 **Advanced** - Solid programming background expected

Example metadata:
```yaml
skill_level: "beginner"
prerequisites:
  - "Basic computer skills"
  - "Terminal familiarity"
```

### Theme Integration
Lessons should support these themes:
- 🚀 Space Exploration
- 🗡️ Fantasy Quest
- 🤖 Robotics Lab
- 🌿 Nature Discovery
- 🌊 Ocean Adventure

Example theme-specific content:
```yaml
themes:
  space:
    terminology:
      file: "mission_log"
      directory: "space_station"
  fantasy:
    terminology:
      file: "scroll"
      directory: "realm"
```

## 🎮 Getting Started with Cursor

### Opening the Project
- Launch Cursor IDE
- Select File > Open Folder and navigate to the project directory
- The project structure will appear in the file explorer

### Using Slash Commands
- Type `/` in any editor or chat window to see available commands
- Highlight code and use `/explain` to get detailed explanations
- Use `/debug` when encountering issues
- Try `/refactor` for code improvement suggestions
- Use `/generate` for content scaffolding
- Access `/test` for test generation

### AI Learning Assistant
The AI Learning Assistant helps personalize your learning experience by:
- Guiding lesson selection based on your skill level
- Adapting examples to your chosen theme
- Providing contextual help via slash commands
- Offering real-time feedback on exercises

## 🎯 Lesson Structure

### Required Files and Directories
```
lesson{n}/
├── instructions.md       # Main lesson content
├── metadata.yaml        # Lesson metadata and personalization
└── code/
    ├── examples/        # Example code files
    ├── exercises/       # Practice exercises
    └── solutions/       # Exercise solutions
```

### Metadata Format (metadata.yaml)
```yaml
title: "Lesson Title"
description: "Brief lesson description"
prerequisites:
  - "Prerequisite 1"
  - "Prerequisite 2"
estimated_time: "X-Y hours"
personalization:
  skill_levels:
    - beginner:
        content_adjustments:
          - "More detailed explanations"
          - "Step-by-step guidance"
    - intermediate:
        content_adjustments:
          - "Faster pace"
          - "More complex examples"
    - advanced:
        content_adjustments:
          - "Advanced concepts"
          - "Implementation challenges"
  themes:
    - space:
        examples:
          - "Spacecraft data"
          - "Mission control"
    - fantasy:
        examples:
          - "Quest systems"
          - "Character stats"
```

## 📝 Slash Command Integration

### Command Placement
Include slash command references at these key points:
1. **Code Blocks**
   ```python
   # Try /explain on this code:
   def example_function():
       pass
   ```

2. **Exercise Instructions**
   ```markdown
   ## Practice Exercise
   1. Write a function that...
   2. Use /generate to scaffold the solution
   3. Improve it with /refactor
   ```

3. **Debugging Sections**
   ```markdown
   ## Troubleshooting
   If you encounter errors:
   1. Highlight the error message
   2. Use /debug for analysis
   3. Apply suggested fixes
   ```

### Skill-Level Specific Commands
- **Beginner**
  - Emphasize `/explain` for understanding
  - Use `/debug` with detailed guidance
  - Suggest `/generate` for examples

- **Intermediate**
  - Focus on `/refactor` for improvement
  - Use `/test` for validation
  - Combine multiple commands

- **Advanced**
  - Advanced `/refactor` scenarios
  - Complex `/test` cases
  - Performance optimization

## 📝 Instructions.md Format

### Required Sections
```markdown
# 🚀 [Lesson Title]
> Skill Level: [🌱 Beginner | 🌿 Intermediate | 🌳 Advanced]
> Theme: [Space 🚀 | Fantasy 🗡️ | Robotics 🤖 | Nature 🌿 | Ocean 🌊]

## Overview
Brief introduction (2-3 sentences)

## 🎯 Learning Objectives
- Objective 1
- Objective 2
- ...

## 📋 Prerequisites
- Required knowledge
- Required tools
- Required setup

## 💡 Cursor Integration
- Open this lesson in Cursor IDE
- Use `/explain` on any code block for detailed explanations
- Highlight challenging sections and use `/debug` for help
- Try `/generate` to scaffold exercise solutions
- Use `/refactor` to improve your code
- Access `/test` to generate test cases

### Skill-Level Specific Tips
{% if skill_level == "beginner" %}
- Start with `/explain` to understand concepts
- Use `/generate` for example code
- Try `/debug` when stuck
{% elif skill_level == "intermediate" %}
- Use `/refactor` to improve solutions
- Try `/test` to validate code
- Combine commands for efficiency
{% else %}
- Explore advanced `/refactor` patterns
- Create comprehensive test suites
- Focus on optimization
{% endif %}

## 📚 Content Sections
1. Topic Introduction
2. Concept Explanation
3. Code Examples
4. Practice Exercises
5. Checkpoints

## 🔍 Checkpoints
Self-assessment questions or tasks

## 📚 Additional Resources
- Official documentation
- Helpful tutorials
- Related lessons
```

## 🎨 Personalization

### 1. Skill Level Adjustments
- **Beginner**
  - Include detailed explanations
  - Provide step-by-step guidance
  - Add more code comments
  - Include troubleshooting tips

- **Intermediate**
  - Focus on best practices
  - Add optimization challenges
  - Include design patterns
  - Provide real-world scenarios

- **Advanced**
  - Cover advanced concepts
  - Include performance considerations
  - Add system design challenges
  - Discuss trade-offs

### 2. Theme Integration
- Use theme-appropriate examples
- Maintain consistent narrative
- Include themed challenges
- Reference themed resources

### 3. Special Focus Areas
- Debugging exercises (use `/debug` command)
- Performance optimization (use `/refactor` command)
- Security considerations
- Testing practices (use `/test` command)

## 🔍 Quality Standards

### 1. Content Quality
- Clear explanations
- Working code examples
- Comprehensive exercises
- Proper prerequisites

### 2. Technical Accuracy
- Tested code
- Current best practices
- Proper error handling
- Security considerations

### 3. Style Consistency
- Follow markdown format
- Use consistent emojis
- Maintain voice/tone
- Follow code style guides

## 🛠️ Code Examples

### 1. Structure
```python
# Example code structure
def example_function():
    """
    Function description
    
    Args:
        param1: Description
        param2: Description
    
    Returns:
        Description of return value
    """
    # Implementation
    pass
```

### 2. Comments
- Add docstrings
- Explain complex logic
- Note edge cases
- Include usage examples

### 3. Error Handling
- Include try/except blocks
- Handle edge cases
- Add input validation
- Provide error messages

## ✅ Exercise Guidelines

### 1. Structure
```python
# exercise.py
"""
Exercise Title

Task:
1. Step one description
2. Step two description
...

Expected Output:
[Description or example of expected output]

Tips:
- Helpful tip 1
- Helpful tip 2
"""

def exercise_function():
    # TODO: Implement the solution
    pass

# Test cases
def test_exercise():
    assert exercise_function() == expected_output
```

### 2. Solution Files
```python
# solution.py
"""
Exercise Solution

Explanation:
[Detailed explanation of the solution approach]
"""

def exercise_function():
    # Implementation with comments
    pass
```

## 🔄 Review Process

### 1. Content Review
- Check accuracy
- Verify completeness
- Test all code
- Validate exercises

### 2. Style Review
- Check formatting
- Verify consistency
- Review structure
- Test links

### 3. Integration
- Update references
- Check dependencies
- Verify navigation
- Test personalization

## 📚 Maintenance

### 1. Regular Updates
- Review content
- Update examples
- Check links
- Update dependencies

### 2. Version Control
- Track changes
- Document updates
- Maintain history
- Review feedback

### 3. Quality Checks
- Run tests
- Verify formatting
- Check consistency
- Review personalization