"""
Test suite for setup modules.
"""

import unittest
from pathlib import Path
from setup.assessment import UserAssessment
from setup.workspace import WorkspaceManager
from setup.lesson_plan import LessonPlanGenerator
from setup.prompt_setup import PromptManager

class TestSetup(unittest.TestCase):
    """Test cases for setup modules."""

    def setUp(self):
        """Set up test environment."""
        self.assessment = UserAssessment()
        self.workspace = WorkspaceManager(cursor_config_dir="test_cursor")
        self.lesson_gen = LessonPlanGenerator(template_dir="test_docs")
        self.prompt_mgr = PromptManager(prompt_file="test_prompt.md")

    def tearDown(self):
        """Clean up test environment."""
        # Clean up test files
        test_files = [
            "test_cursor",
            "test_docs",
            "test_prompt.md",
            "test_lesson_plan.md"
        ]
        for file in test_files:
            path = Path(file)
            if path.is_dir():
                for child in path.glob('*'):
                    child.unlink()
                path.rmdir()
            elif path.exists():
                path.unlink()

    def test_assessment_validation(self):
        """Test assessment data validation."""
        # Test valid data
        valid_data = {
            "skill_level": "Beginner",
            "theme": "Space Exploration 🚀",
            "interests": ["python", "web"],
            "goals": "Learn programming",
            "preferences": {"pace": "Standard"}
        }
        self.assertTrue(self.assessment.validate_assessment(valid_data))

        # Test invalid data
        invalid_data = {
            "skill_level": "Expert",  # Invalid skill level
            "theme": "Invalid Theme",
            "interests": [],
            "goals": "",
            "preferences": {}
        }
        self.assertFalse(self.assessment.validate_assessment(invalid_data))

    def test_workspace_configuration(self):
        """Test workspace configuration."""
        # Create test prompt file
        Path("test_prompt.md").write_text("Test prompt content")

        # Test configuration
        self.assertTrue(self.workspace.configure_workspace("test_prompt.md"))
        self.assertTrue(Path("test_cursor/workspace_config.yaml").exists())

        # Test configuration content
        config = self.workspace._load_workspace_config()
        self.assertEqual(config["system_prompt_file"], "test_prompt.md")
        self.assertTrue(config["settings"]["auto_save"])

    def test_lesson_plan_generation(self):
        """Test lesson plan generation."""
        # Create test template
        Path("test_docs").mkdir(exist_ok=True)
        template_content = """
        # Learning Plan for {{student_name}}
        Level: {{skill_level}}
        Theme: {{theme}}
        """
        Path("test_docs/template.md").write_text(template_content)

        # Test generation
        user_data = {
            "name": "Test Student",
            "skill_level": "Beginner",
            "theme": "Space"
        }
        self.assertTrue(
            self.lesson_gen.generate_plan(
                "template.md",
                "test_lesson_plan.md",
                user_data
            )
        )
        self.assertTrue(Path("test_lesson_plan.md").exists())

    def test_prompt_customization(self):
        """Test prompt customization."""
        # Create test prompt file
        prompt_content = """
        Skill Level: {{SKILL_LEVEL}}
        Theme: {{THEME}}
        Pace: {{LEARNING_PACE}}
        """
        Path("test_prompt.md").write_text(prompt_content)

        # Test customization
        user_data = {
            "skill_level": "Beginner",
            "theme": "Space",
            "preferences": {"pace": "Quick"}
        }
        result = self.prompt_mgr.customize_prompt(user_data)
        self.assertIsNotNone(result)
        self.assertIn("Skill Level: Beginner", result)
        self.assertIn("Theme: Space", result)
        self.assertIn("Pace: Quick", result)

if __name__ == '__main__':
    unittest.main() 