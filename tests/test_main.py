"""Test main application."""

from fastapi.testclient import TestClient


def test_read_main(client: TestClient) -> None:
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 404  # Since we haven't defined a root endpoint yet
