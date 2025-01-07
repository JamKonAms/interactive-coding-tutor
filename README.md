# Interactive Coding Tutor

A personalized learning environment with an AI Learning Assistant that adapts to your skill level, interests, and learning pace.

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/interactive-coding-tutor.git
cd interactive-coding-tutor
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the initialization script:
```bash
python init.py
```

## Features

- 🎯 Personalized learning paths
- 🚀 Theme-based learning (Space, Fantasy, Robotics, Nature, Ocean)
- 📚 Skill-level adaptation (Beginner, Intermediate, Advanced)
- 🤖 AI Learning Assistant integration with Cursor IDE
- 🔄 Progress tracking and adaptive content
- 💡 Interactive exercises and real-time feedback

## Project Structure

```
.
├── ai_agents/              # AI agent prompts and configurations
├── config/                 # Configuration management
├── docs/                   # Documentation and templates
├── lessons/               # Lesson content and exercises
├── setup/                 # Setup and initialization modules
├── init.py               # Main initialization script
└── requirements.txt      # Project dependencies
```

## Testing

1. Fork this repository to your GitHub account
2. Clone your fork locally
3. Follow the Quick Start steps above
4. The initialization script will:
   - Assess your skill level and preferences
   - Generate a personalized lesson plan
   - Configure the AI Learning Assistant
   - Set up your workspace in Cursor IDE

## Development

To modify or extend the tutor:

1. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes
3. Test thoroughly
4. Create a pull request

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 