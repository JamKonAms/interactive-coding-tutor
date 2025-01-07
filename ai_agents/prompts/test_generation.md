# Test Generation Prompt

## Purpose
Generate test cases to validate code functionality, ensure correctness, and demonstrate proper usage.

## Usage
- Command: `/test`
- Highlight the code to test
- Optionally specify test types or coverage goals

## Input Format
```python
# Highlight code to test:
def your_code():
    # ... code to test ...

# Optionally add test requirements:
# Test: Unit tests
# Test: Edge cases
# Test: Integration
```

## Parameters
- **Language**: Programming language being tested
- **Test Type**: Unit/integration/edge cases
- **Coverage**: Test coverage goals
- **Framework**: Preferred testing framework

## Example Interactions

### 1. Basic Unit Tests
**User Input:**
```python
def calculate_grade(score: float) -> str:
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
```

**Assistant Response:**
```
Here are pytest unit tests for the grade calculator:

```python
import pytest

def test_calculate_grade_basic():
    """Test basic grade calculations."""
    assert calculate_grade(95) == 'A'
    assert calculate_grade(85) == 'B'
    assert calculate_grade(75) == 'C'
    assert calculate_grade(65) == 'D'
    assert calculate_grade(55) == 'F'

def test_calculate_grade_boundaries():
    """Test grade boundary conditions."""
    assert calculate_grade(90) == 'A'  # Lower A boundary
    assert calculate_grade(89.9) == 'B'  # Upper B boundary
    assert calculate_grade(80) == 'B'  # Lower B boundary
    assert calculate_grade(70) == 'C'  # Lower C boundary
    assert calculate_grade(60) == 'D'  # Lower D boundary

def test_calculate_grade_invalid():
    """Test invalid inputs."""
    with pytest.raises(TypeError):
        calculate_grade("not a number")
    
    # Optional: Test out of range values
    assert calculate_grade(-10) == 'F'
    assert calculate_grade(110) == 'A'

# Run with: pytest test_grades.py -v
```

Key test cases covered:
1. Basic grade ranges
2. Boundary values
3. Invalid inputs
4. Edge cases
```

### 2. Integration Tests
**User Input:**
```python
class UserDatabase:
    def __init__(self):
        self.users = {}
    
    def add_user(self, username: str, email: str) -> bool:
        if username in self.users:
            return False
        self.users[username] = email
        return True
    
    def get_user(self, username: str) -> str:
        return self.users.get(username)
```

**Assistant Response:**
```
Here are integration tests using pytest fixtures:

```python
import pytest
from typing import Tuple

@pytest.fixture
def user_db():
    """Create a fresh UserDatabase for each test."""
    return UserDatabase()

@pytest.fixture
def sample_user() -> Tuple[str, str]:
    """Provide a sample user for testing."""
    return ("testuser", "test@example.com")

def test_add_user(user_db, sample_user):
    """Test adding a new user."""
    username, email = sample_user
    assert user_db.add_user(username, email) == True
    assert user_db.get_user(username) == email

def test_add_duplicate_user(user_db, sample_user):
    """Test adding a duplicate user."""
    username, email = sample_user
    # First addition should succeed
    assert user_db.add_user(username, email) == True
    # Second addition should fail
    assert user_db.add_user(username, "new@example.com") == False
    # Email should remain unchanged
    assert user_db.get_user(username) == email

def test_get_nonexistent_user(user_db):
    """Test retrieving a non-existent user."""
    assert user_db.get_user("nonexistent") is None

def test_user_workflow():
    """Test complete user management workflow."""
    db = UserDatabase()
    
    # Add multiple users
    assert db.add_user("user1", "user1@example.com")
    assert db.add_user("user2", "user2@example.com")
    
    # Verify all users
    assert db.get_user("user1") == "user1@example.com"
    assert db.get_user("user2") == "user2@example.com"
    
    # Try duplicate and nonexistent
    assert not db.add_user("user1", "new@example.com")
    assert db.get_user("user3") is None

# Run with: pytest test_user_db.py -v
```

Test coverage includes:
1. Basic operations
2. Error cases
3. State persistence
4. Complete workflows
```

## Response Format
The assistant will:
1. Generate appropriate tests
2. Explain test coverage
3. Include setup instructions
4. Note important assertions
5. Suggest additional tests

## Caveats & Limitations
- Focuses on Python testing frameworks
- May need mocking for external dependencies
- Complex scenarios may need manual setup
- Some tests may need environment configuration

## Best Practices
1. **Test Structure**
   - Use clear test names
   - Follow AAA pattern (Arrange-Act-Assert)
   - Include docstrings
   - Group related tests

2. **Coverage Goals**
   - Test happy paths
   - Include edge cases
   - Handle invalid inputs
   - Check error conditions

3. **Test Organization**
   - Use fixtures for setup
   - Group related tests
   - Keep tests independent
   - Follow testing pyramid

## Integration with Other Commands
- Use `/debug` to fix failing tests
- Use `/explain` to understand test cases
- Use `/refactor` to improve test code
- Use `/generate` for test data

Remember: The Test Generation Assistant helps ensure your code works correctly by creating comprehensive test suites.
``` 