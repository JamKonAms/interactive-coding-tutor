"""
Setup package for the Interactive Learning Environment.
Handles initial configuration, workspace setup, and user assessment.
"""

from .assessment import UserAssessment
from .workspace import WorkspaceManager
from .lesson_plan import LessonPlanGenerator
from .prompt_setup import PromptManager

__all__ = ['UserAssessment', 'WorkspaceManager', 'LessonPlanGenerator', 'PromptManager'] 