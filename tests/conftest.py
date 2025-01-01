"""Test configuration and fixtures."""

# Standard library imports
import sys
from pathlib import Path

# Third-party imports
import pytest
from fastapi.testclient import TestClient

# Configure Python path before local imports
project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)

# Local imports
# pylint: disable=wrong-import-position
from app.main import fastapi_app

# pylint: enable=wrong-import-position


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the FastAPI application."""
    return TestClient(fastapi_app)
