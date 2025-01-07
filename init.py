#!/usr/bin/env python3

"""
Interactive Learning Environment Initializer

This script sets up a personalized learning environment with the help of an AI Learning Assistant.
It guides users through:
1. Skill level assessment
2. Theme selection
3. Interest identification
4. Learning goal setting

The AI Learning Assistant then:
- Customizes lesson content based on preferences
- Integrates with Cursor's slash commands for enhanced learning
- Provides contextual help throughout the lessons
- Adapts examples to the chosen theme
- Offers personalized feedback and guidance

Usage:
    python init.py         # First-time setup
    python init.py --update # Update existing configuration
"""

import argparse
import logging
import sys
from pathlib import Path

# Import setup modules
from setup.assessment import UserAssessment
from setup.workspace import WorkspaceManager
from setup.lesson_plan import LessonPlanGenerator
from setup.prompt_setup import PromptManager
from config.config_manager import ConfigManager

# Constants
TEMPLATE_FILE = "LESSON_PLAN_TEMPLATE.md"
OUTPUT_FILE = "LESSON_PLAN_CUSTOM.md"
PROMPT_FILE = "ai_agents/prompts/learning_assistant.md"

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("init.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def initial_setup():
    """Perform initial setup of the learning environment."""
    try:
        logger.info("Starting initial setup")
        
        # Initialize components
        assessment = UserAssessment()
        workspace = WorkspaceManager()
        lesson_gen = LessonPlanGenerator()
        prompt_mgr = PromptManager()
        config = ConfigManager()
        
        # Collect user preferences
        user_data = assessment.assess_new_user()
        if not assessment.validate_assessment(user_data):
            logger.error("Invalid assessment data")
            return False
            
        # Initialize student configuration
        config.initialize_student(
            name=user_data.get("name", "Student"),
            skill_level=user_data.get("skill_level", "beginner")
        )
        
        # Configure workspace
        if not workspace.configure_workspace(PROMPT_FILE):
            logger.error("Failed to configure workspace")
            return False
            
        # Generate lesson plan
        if not lesson_gen.generate_plan(TEMPLATE_FILE, OUTPUT_FILE, user_data):
            logger.error("Failed to generate lesson plan")
            return False
            
        # Setup Learning Assistant prompt
        prompt_content = prompt_mgr.customize_prompt(user_data)
        if not prompt_content or not prompt_mgr.validate_prompt(prompt_content):
            logger.error("Failed to setup Learning Assistant prompt")
            return False
            
        # Display setup instructions
        prompt_mgr.display_prompt()
        prompt_mgr.open_in_browser()
        
        logger.info("Initial setup completed successfully")
        return True
        
    except Exception as e:
        logger.error(f"Error during initial setup: {str(e)}")
        return False

def update_configuration():
    """Update existing configuration."""
    try:
        logger.info("Updating existing configuration")
        
        # Initialize components
        assessment = UserAssessment()
        workspace = WorkspaceManager()
        lesson_gen = LessonPlanGenerator()
        config = ConfigManager()
        
        # Load current configuration
        current_data = config.get_student_preference("")  # Get all preferences
        
        # Update assessment
        user_data = assessment.update_assessment(current_data)
        if not assessment.validate_assessment(user_data):
            logger.error("Invalid assessment data")
            return False
            
        # Update workspace configuration
        workspace_updates = {
            "settings": {
                "theme": user_data.get("theme"),
                "skill_level": user_data.get("skill_level")
            }
        }
        if not workspace.update_workspace_config(workspace_updates):
            logger.error("Failed to update workspace configuration")
            return False
            
        # Regenerate lesson plan
        if not lesson_gen.generate_plan(TEMPLATE_FILE, OUTPUT_FILE, user_data):
            logger.error("Failed to regenerate lesson plan")
            return False
            
        logger.info("Configuration update completed successfully")
        return True
        
    except Exception as e:
        logger.error(f"Error during configuration update: {str(e)}")
        return False

def main():
    """Main entry point for the initialization script."""
    parser = argparse.ArgumentParser(description="Initialize the Interactive Coding Tutor.")
    parser.add_argument('--update', action='store_true', help='Update existing configuration')
    args = parser.parse_args()

    success = update_configuration() if args.update else initial_setup()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 