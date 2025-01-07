"""
Prompt management module for handling Learning Assistant prompts.
"""

import logging
import webbrowser
from pathlib import Path
from typing import Dict, Optional

class PromptManager:
    """Manages Learning Assistant prompts and setup."""

    def __init__(self, prompt_file: str = "ai_agents/prompts/learning_assistant.md"):
        """Initialize prompt manager.
        
        Args:
            prompt_file: Path to the Learning Assistant prompt file
        """
        self.logger = logging.getLogger(__name__)
        self.prompt_file = Path(prompt_file)

    def display_prompt(self) -> Optional[str]:
        """Display the Learning Assistant prompt.
        
        Returns:
            Prompt content if successful, None otherwise
        """
        try:
            if not self.prompt_file.exists():
                self.logger.error(f"Prompt file not found: {self.prompt_file}")
                return None
                
            content = self.prompt_file.read_text()
            print("\n=== Learning Assistant Prompt ===\n")
            print(content)
            print("\n=== End of Prompt ===\n")
            
            self._display_setup_instructions()
            return content
            
        except Exception as e:
            self.logger.error(f"Error displaying prompt: {str(e)}")
            return None

    def open_in_browser(self) -> bool:
        """Open the prompt file in the default browser.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            if not self.prompt_file.exists():
                self.logger.error(f"Prompt file not found: {self.prompt_file}")
                return False
                
            prompt_path = self.prompt_file.resolve()
            webbrowser.open(f"file://{prompt_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening prompt in browser: {str(e)}")
            return False

    def customize_prompt(self, user_data: Dict) -> Optional[str]:
        """Customize the Learning Assistant prompt based on user preferences.
        
        Args:
            user_data: User preferences and assessment data
            
        Returns:
            Customized prompt content if successful, None otherwise
        """
        try:
            if not self.prompt_file.exists():
                self.logger.error(f"Prompt file not found: {self.prompt_file}")
                return None
                
            # Load base prompt
            content = self.prompt_file.read_text()
            
            # Customize based on user preferences
            replacements = {
                "{{SKILL_LEVEL}}": user_data.get("skill_level", "beginner"),
                "{{THEME}}": user_data.get("theme", "General"),
                "{{LEARNING_PACE}}": user_data.get("preferences", {}).get("pace", "Standard")
            }
            
            for key, value in replacements.items():
                content = content.replace(key, value)
                
            return content
            
        except Exception as e:
            self.logger.error(f"Error customizing prompt: {str(e)}")
            return None

    def _display_setup_instructions(self) -> None:
        """Display instructions for setting up the Learning Assistant in Cursor."""
        print("To set this as your default AI chat in Cursor IDE:")
        print("1. Copy the content above.")
        print("2. Open Cursor IDE settings:")
        print("   - Windows/Linux: File > Settings > AI Chat")
        print("   - macOS: Cursor > Settings > AI Chat")
        print("3. Paste the content into the 'System Prompt' field.")
        print("4. Click 'Save' and restart Cursor IDE.\n")

    def validate_prompt(self, content: str) -> bool:
        """Validate prompt content.
        
        Args:
            content: Prompt content to validate
            
        Returns:
            True if content is valid, False otherwise
        """
        try:
            # Check for required sections
            required_sections = [
                "## Purpose",
                "## Usage",
                "## Parameters",
                "## Example Interactions",
                "## Response Format"
            ]
            
            for section in required_sections:
                if section not in content:
                    self.logger.error(f"Missing required section: {section}")
                    return False
            
            # Check minimum content length
            if len(content.split('\n')) < 50:
                self.logger.error("Prompt content is too short")
                return False
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error validating prompt: {str(e)}")
            return False

    def get_prompt_status(self) -> Dict:
        """Get current prompt status.
        
        Returns:
            Dictionary containing prompt status information
        """
        return {
            "exists": self.prompt_file.exists(),
            "path": str(self.prompt_file),
            "size": self.prompt_file.stat().st_size if self.prompt_file.exists() else 0,
            "last_modified": self.prompt_file.stat().st_mtime if self.prompt_file.exists() else None
        } 