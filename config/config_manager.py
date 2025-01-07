#!/usr/bin/env python3

"""
Configuration Manager for Interactive Learning Environment

This utility manages configuration files for the learning environment:
- student_config.yaml: Personal preferences and learning profile
- progress.json: Progress tracking and achievements
- settings.yaml: System-wide settings and configurations

Usage:
    from config.config_manager import ConfigManager
    config = ConfigManager()
    
    # Get student preferences
    theme = config.get_student_preference('learning.theme')
    
    # Update progress
    config.update_progress('lesson_completed', 'lesson_1')
    
    # Check system settings
    debug_enabled = config.get_setting('ai_assistants.specialized_agents.debug.enabled')
"""

import os
import json
import yaml
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, Union

class ConfigManager:
    """Manages configuration files for the learning environment."""
    
    def __init__(self, config_dir: str = "."):
        """Initialize the configuration manager.
        
        Args:
            config_dir: Directory containing configuration files (defaults to current directory)
        """
        self.config_dir = Path(config_dir)
        self.student_config_path = self.config_dir / "student_config.yaml"
        self.progress_path = self.config_dir / "progress.json"
        self.settings_path = self.config_dir / "settings.yaml"
        
        # Create config directory if it doesn't exist
        self.config_dir.mkdir(exist_ok=True)
        
        # Load configurations
        self.reload_configs()

    # ... rest of the code remains the same ... 