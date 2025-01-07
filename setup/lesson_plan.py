"""
Lesson plan generation module for creating personalized learning paths.
"""

import logging
from pathlib import Path
from typing import Dict, Optional
from jinja2 import Environment, FileSystemLoader, Template

class LessonPlanGenerator:
    """Generates personalized lesson plans based on user preferences."""

    def __init__(self, template_dir: str = "docs"):
        """Initialize lesson plan generator.
        
        Args:
            template_dir: Directory containing lesson plan templates
        """
        self.logger = logging.getLogger(__name__)
        self.template_dir = Path(template_dir)
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def generate_plan(self, 
                     template_file: str,
                     output_file: str,
                     user_data: Dict) -> bool:
        """Generate a personalized lesson plan.
        
        Args:
            template_file: Name of the template file
            output_file: Path to save the generated plan
            user_data: User preferences and assessment data
            
        Returns:
            True if generation successful, False otherwise
        """
        try:
            self.logger.info(f"Generating lesson plan from template: {template_file}")
            
            # Load and validate template
            template = self._load_template(template_file)
            if not template:
                return False
                
            # Generate content
            content = self._render_template(template, user_data)
            if not content:
                return False
                
            # Save generated plan
            output_path = Path(output_file)
            output_path.parent.mkdir(exist_ok=True)
            output_path.write_text(content)
            
            self.logger.info(f"Lesson plan generated at {output_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error generating lesson plan: {str(e)}")
            return False

    def _load_template(self, template_file: str) -> Optional[Template]:
        """Load a template file.
        
        Args:
            template_file: Name of the template file
            
        Returns:
            Loaded template or None if error
        """
        try:
            return self.env.get_template(template_file)
        except Exception as e:
            self.logger.error(f"Error loading template {template_file}: {str(e)}")
            return None

    def _render_template(self, template: Template, user_data: Dict) -> Optional[str]:
        """Render a template with user data.
        
        Args:
            template: Loaded template
            user_data: User data for template rendering
            
        Returns:
            Rendered content or None if error
        """
        try:
            return template.render(
                student_name=user_data.get("name", "Student"),
                skill_level=user_data.get("skill_level", "beginner"),
                theme=user_data.get("theme", "General"),
                interests=user_data.get("interests", []),
                pace=user_data.get("preferences", {}).get("pace", "Standard")
            )
        except Exception as e:
            self.logger.error(f"Error rendering template: {str(e)}")
            return None

    def customize_lessons(self, user_data: Dict) -> Dict:
        """Customize lesson content based on user preferences.
        
        Args:
            user_data: User preferences and assessment data
            
        Returns:
            Dictionary of customized lesson parameters
        """
        skill_level = user_data.get("skill_level", "beginner").lower()
        theme = user_data.get("theme", "General")
        pace = user_data.get("preferences", {}).get("pace", "Standard").lower()
        
        # Adjust content based on skill level
        content_depth = {
            "beginner": {
                "detail_level": "basic",
                "examples_per_concept": 2,
                "practice_exercises": 3
            },
            "intermediate": {
                "detail_level": "intermediate",
                "examples_per_concept": 3,
                "practice_exercises": 4
            },
            "advanced": {
                "detail_level": "advanced",
                "examples_per_concept": 4,
                "practice_exercises": 5
            }
        }.get(skill_level, {})
        
        # Adjust pace
        pace_multiplier = {
            "quick": 0.8,
            "standard": 1.0,
            "thorough": 1.2
        }.get(pace, 1.0)
        
        return {
            "content_depth": content_depth,
            "pace_multiplier": pace_multiplier,
            "theme": theme,
            "skill_level": skill_level
        }

    def validate_lesson_plan(self, content: str) -> bool:
        """Validate generated lesson plan content.
        
        Args:
            content: Generated lesson plan content
            
        Returns:
            True if content is valid, False otherwise
        """
        try:
            # Check for required sections
            required_sections = [
                "# Learning Objectives",
                "## Prerequisites",
                "## Content",
                "## Exercises",
                "## Additional Resources"
            ]
            
            for section in required_sections:
                if section not in content:
                    self.logger.error(f"Missing required section: {section}")
                    return False
            
            # Check minimum content length
            if len(content.split('\n')) < 20:
                self.logger.error("Lesson plan content is too short")
                return False
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error validating lesson plan: {str(e)}")
            return False 