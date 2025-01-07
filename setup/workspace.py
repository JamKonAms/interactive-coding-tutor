"""
Workspace management module for configuring the learning environment.
"""

import logging
import yaml
from pathlib import Path
from typing import Dict, Optional

class WorkspaceManager:
    """Manages workspace configuration and setup."""

    def __init__(self, cursor_config_dir: str = ".cursor"):
        """Initialize workspace manager.
        
        Args:
            cursor_config_dir: Directory for Cursor IDE configuration
        """
        self.logger = logging.getLogger(__name__)
        self.cursor_config_dir = Path(cursor_config_dir)
        self.workspace_config_file = self.cursor_config_dir / "workspace_config.yaml"

    def configure_workspace(self, prompt_file: str) -> bool:
        """Configure the workspace for Cursor IDE.
        
        Args:
            prompt_file: Path to the Learning Assistant prompt file
            
        Returns:
            True if configuration successful, False otherwise
        """
        try:
            self.logger.info("Configuring workspace")
            
            # Create Cursor config directory
            self.cursor_config_dir.mkdir(exist_ok=True)
            
            # Create workspace configuration
            config_content = {
                "system_prompt_file": prompt_file,
                "settings": {
                    "auto_save": True,
                    "format_on_save": True,
                    "show_line_numbers": True
                }
            }
            
            # Save configuration
            self._save_workspace_config(config_content)
            
            self.logger.info(f"Workspace configuration created at {self.workspace_config_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error configuring workspace: {str(e)}")
            return False

    def update_workspace_config(self, updates: Dict) -> bool:
        """Update existing workspace configuration.
        
        Args:
            updates: Dictionary of configuration updates
            
        Returns:
            True if update successful, False otherwise
        """
        try:
            current_config = self._load_workspace_config()
            
            # Update configuration
            for key, value in updates.items():
                if isinstance(value, dict) and key in current_config:
                    current_config[key].update(value)
                else:
                    current_config[key] = value
            
            # Save updated configuration
            self._save_workspace_config(current_config)
            
            self.logger.info("Workspace configuration updated")
            return True
            
        except Exception as e:
            self.logger.error(f"Error updating workspace configuration: {str(e)}")
            return False

    def _load_workspace_config(self) -> Dict:
        """Load current workspace configuration."""
        if not self.workspace_config_file.exists():
            return {}
        with open(self.workspace_config_file, 'r') as f:
            return yaml.safe_load(f) or {}

    def _save_workspace_config(self, config: Dict) -> None:
        """Save workspace configuration to file."""
        with open(self.workspace_config_file, 'w') as f:
            yaml.dump(config, f, default_flow_style=False)

    def validate_workspace(self) -> bool:
        """Validate workspace configuration and structure.
        
        Returns:
            True if workspace is valid, False otherwise
        """
        try:
            # Check Cursor config directory
            if not self.cursor_config_dir.exists():
                self.logger.error("Cursor config directory not found")
                return False

            # Check workspace configuration
            config = self._load_workspace_config()
            if not config:
                self.logger.error("Workspace configuration is empty")
                return False

            # Check prompt file
            prompt_file = config.get("system_prompt_file")
            if not prompt_file or not Path(prompt_file).exists():
                self.logger.error(f"Prompt file not found: {prompt_file}")
                return False

            return True
            
        except Exception as e:
            self.logger.error(f"Error validating workspace: {str(e)}")
            return False

    def get_workspace_status(self) -> Dict:
        """Get current workspace status.
        
        Returns:
            Dictionary containing workspace status information
        """
        return {
            "configured": self.workspace_config_file.exists(),
            "config_dir_exists": self.cursor_config_dir.exists(),
            "config": self._load_workspace_config()
        } 