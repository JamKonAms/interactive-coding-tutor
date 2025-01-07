# 🚀 Your Personal Learning Journey: {{ theme }}

Welcome, {{ student_name }}! Based on your {{ skill_level }} experience level and interest in {{ interests }}, we've customized this learning path for you.

## 🎯 Your Learning Goals
{% for goal in learning_goals %}
- {{ goal }}
{% endfor %}

## 📚 Customized Lesson Path

### 🌟 Foundation Track
{% if skill_level == "beginner" %}
1. **Lesson 0: Terminal Fundamentals**
   - Basic terminal navigation
   - File operations
   - Command line proficiency
   _Estimated time: 2-3 hours_

2. **Lesson 1: Python Foundations**
   - Variables and data types
   - Control flow
   - Functions and modules
   _Estimated time: 4-5 hours_
{% else %}
1. **Lesson 0: Quick Terminal Review**
   - Advanced terminal operations
   - Shell scripting basics
   - Productivity tips
   _Estimated time: 1-2 hours_

2. **Lesson 1: Python Refresher**
   - Advanced Python concepts
   - Best practices
   - Code organization
   _Estimated time: 2-3 hours_
{% endif %}

### 🔧 Development Tools
{% if skill_level == "beginner" %}
3. **Lesson 2: Version Control Basics**
   - Git fundamentals
   - Basic workflows
   - Collaboration basics
   _Estimated time: 3-4 hours_
{% else %}
3. **Lesson 2: Advanced Version Control**
   - Git workflows
   - Branch strategies
   - Team collaboration
   _Estimated time: 2-3 hours_
{% endif %}

### 💻 Core Programming
{% if "web" in interests %}
4. **Lesson 3: Web Development**
   - HTML/CSS basics
   - JavaScript fundamentals
   - React introduction
   _Estimated time: 5-6 hours_
{% endif %}

{% if "ai" in interests %}
4. **Lesson 3: AI & Machine Learning**
   - Python for ML
   - Basic algorithms
   - Model training
   _Estimated time: 6-7 hours_
{% endif %}

{% if "data" in interests %}
4. **Lesson 3: Data Science**
   - Data manipulation
   - Analysis techniques
   - Visualization
   _Estimated time: 5-6 hours_
{% endif %}

### 🏗️ Project Track
{% if skill_level == "beginner" %}
5. **Lesson 4: Building Your First Project**
   - Project planning
   - Implementation
   - Testing basics
   _Estimated time: 8-10 hours_
{% else %}
5. **Lesson 4: Advanced Project Development**
   - Architecture design
   - Testing strategies
   - Deployment
   _Estimated time: 10-12 hours_
{% endif %}

## 🎮 Interactive Learning Tools

Throughout your journey, you can use these Cursor commands for assistance:
- Type `/explain` to understand code
- Use `/debug` when stuck
- Try `/refactor` to improve your code
- Use `/generate` for new code examples
- Try `/test` to create test cases

## 📈 Progress Tracking

Track your progress here:
- [ ] Lesson 0 completed
- [ ] Lesson 1 completed
- [ ] Lesson 2 completed
- [ ] Lesson 3 completed
- [ ] Lesson 4 completed

## 🔄 Adjusting Your Path

If you need to adjust this learning path:
1. Run `python init.py --update` to update your preferences
2. Or manually edit your `student_config.yaml` file
3. The system will regenerate your custom plan

## 📚 Additional Resources

Based on your interests in {{ interests }}, we recommend:
{% for resource in recommended_resources %}
- {{ resource }}
{% endfor %}

Remember: This is your journey! Feel free to adjust the pace and order of lessons to match your learning style. 