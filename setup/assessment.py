"""
User assessment module for collecting initial preferences and skill levels.
"""

import logging
import questionary
from typing import Dict, List
from pathlib import Path

class UserAssessment:
    """Handles user assessment and preference collection."""

    THEMES = [
        "Space Exploration 🚀",
        "Fantasy Quest 🗡️",
        "Robotics Lab 🤖",
        "Nature Discovery 🌿",
        "Ocean Adventure 🌊"
    ]

    SKILL_LEVELS = ["Beginner", "Intermediate", "Advanced"]

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def assess_new_user(self) -> Dict:
        """Conduct a full assessment for a new user.

        Returns:
            Dict containing user preferences and assessment results
        """
        try:
            self.logger.info("Starting user assessment")
            return {
                "skill_level": self._get_skill_level(),
                "theme": self._get_theme(),
                "interests": self._get_interests(),
                "goals": self._get_goals(),
                "preferences": self._get_preferences()
            }
        except Exception as e:
            self.logger.error(f"Error during user assessment: {str(e)}")
            raise

    def update_assessment(self, current_data: Dict) -> Dict:
        """Update existing user assessment data.

        Args:
            current_data: Current user configuration data

        Returns:
            Updated configuration data
        """
        try:
            self.logger.info("Updating user assessment")
            return {
                "skill_level": self._get_skill_level(current_data.get("skill_level")),
                "theme": self._get_theme(current_data.get("theme")),
                "interests": self._get_interests(current_data.get("interests")),
                "goals": self._get_goals(current_data.get("goals")),
                "preferences": self._get_preferences(current_data.get("preferences", {}))
            }
        except Exception as e:
            self.logger.error(f"Error during assessment update: {str(e)}")
            raise

    def _get_skill_level(self, default: str = None) -> str:
        """Get user's skill level."""
        return questionary.select(
            "Select your programming skill level:",
            choices=self.SKILL_LEVELS,
            default=default or "Beginner"
        ).ask()

    def _get_theme(self, default: str = None) -> str:
        """Get user's preferred learning theme."""
        return questionary.select(
            "Choose a learning theme:",
            choices=self.THEMES,
            default=default or self.THEMES[0]
        ).ask()

    def _get_interests(self, default: List[str] = None) -> List[str]:
        """Get user's programming interests."""
        interests = questionary.text(
            "Enter your programming interests (comma-separated):",
            default=",".join(default) if default else ""
        ).ask()
        return [interest.strip() for interest in interests.split(",") if interest.strip()]

    def _get_goals(self, default: str = None) -> str:
        """Get user's learning goals."""
        return questionary.text(
            "Describe your learning goals:",
            default=default or ""
        ).ask()

    def _get_preferences(self, default: Dict = None) -> Dict:
        """Get user's learning preferences."""
        default = default or {}
        
        pace = questionary.select(
            "Select your preferred learning pace:",
            choices=["Quick", "Standard", "Thorough"],
            default=default.get("pace", "Standard")
        ).ask()

        practice_frequency = questionary.select(
            "How often would you like practice exercises?",
            choices=["After each concept", "End of each lesson", "Custom schedule"],
            default=default.get("practice_frequency", "After each concept")
        ).ask()

        return {
            "pace": pace,
            "practice_frequency": practice_frequency,
            "show_hints": default.get("show_hints", True),
            "notifications_enabled": default.get("notifications_enabled", True)
        }

    def validate_assessment(self, data: Dict) -> bool:
        """Validate assessment data.

        Args:
            data: Assessment data to validate

        Returns:
            True if valid, False otherwise
        """
        try:
            required_fields = ["skill_level", "theme", "interests", "goals", "preferences"]
            if not all(field in data for field in required_fields):
                self.logger.error("Missing required fields in assessment data")
                return False

            if data["skill_level"] not in self.SKILL_LEVELS:
                self.logger.error(f"Invalid skill level: {data['skill_level']}")
                return False

            if data["theme"] not in self.THEMES:
                self.logger.error(f"Invalid theme: {data['theme']}")
                return False

            return True
        except Exception as e:
            self.logger.error(f"Error validating assessment data: {str(e)}")
            return False 