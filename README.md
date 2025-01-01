# QR Code Generator

[![CI](https://github.com/gsinghjay/qr-gen/actions/workflows/ci.yml/badge.svg)](https://github.com/gsinghjay/qr-gen/actions/workflows/ci.yml)
[![Release](https://github.com/gsinghjay/qr-gen/actions/workflows/release.yml/badge.svg)](https://github.com/gsinghjay/qr-gen/actions/workflows/release.yml)
[![codecov](https://codecov.io/gh/gsinghjay/qr-gen/branch/main/graph/badge.svg)](https://codecov.io/gh/gsinghjay/qr-gen)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust static and dynamic QR code generator built with FastAPI and modern Python practices.

## 🚀 Features

- FastAPI-based REST API
- Clean Architecture
- Automated testing with pytest
- Semantic versioning with Commitizen
- Type checking with mypy
- Code formatting with black and isort
- Git hooks with pre-commit
- Comprehensive test coverage
- Structured logging
- Prometheus metrics

## 🛠️ Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy (with async support)
- Poetry
- Pytest
- Alembic
- Pydantic V2
- Commitizen

## 📦 Installation

1. Prerequisites:
   ```bash
   # Install Python 3.11+
   python --version  # Should be 3.11+

   # Install Poetry
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/gsinghjay/qr-gen.git
   cd qr-gen
   ```

3. Install dependencies:
   ```bash
   poetry install  # Install all dependencies
   poetry install --without dev,test  # Production only
   ```

4. Set up pre-commit hooks:
   ```bash
   poetry run pre-commit install
   poetry run pre-commit install --hook-type commit-msg  # For Commitizen
   ```

## 🏗️ Project Structure

```
qr-gen/
├── app/
│   ├── core/          # Application configuration
│   ├── crud/          # Database operations
│   ├── models/        # SQLAlchemy models
│   ├── schemas/       # Pydantic models
│   ├── routers/       # API routes
│   └── external_services/  # External integrations
├── tests/             # Test suite
└── docs/             # Documentation
```

## 🧪 Testing

Run the test suite:
```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=app

# Run specific tests
poetry run pytest tests/test_main.py -v
```

## 📝 Development

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```

2. Make changes and commit using Commitizen:
   ```bash
   poetry run cz commit
   ```

3. Bump version and update CHANGELOG:
   ```bash
   poetry run cz bump --changelog
   ```

## 🔄 Commit Convention

We use [Conventional Commits](https://www.conventionalcommits.org/) with Commitizen:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code refactoring
- `test`: Testing
- `chore`: Maintenance

## 🚀 Running the Application

1. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

2. Run the application:
   ```bash
   # Development
   poetry run uvicorn app.main:app --reload

   # Production
   poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

## 📚 API Documentation

Once running, access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔄 Version Management

We use semantic versioning (MAJOR.MINOR.PATCH):
- MAJOR: Breaking changes
- MINOR: New features (backwards compatible)
- PATCH: Bug fixes (backwards compatible)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit changes with `poetry run cz commit`
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🗺️ Roadmap

See [ROADMAP.md](ROADMAP.md) for the development roadmap.

## 🔄 Git Workflow

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```

2. Make changes and commit:
   ```bash
   # Stage your changes
   git add .

   # Commit with conventional format
   git commit -m "type(scope): description"
   ```

3. Common commit types:
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation changes
   - `style`: Formatting changes
   - `refactor`: Code refactoring
   - `test`: Adding/updating tests
   - `chore`: Maintenance tasks

4. Pre-commit hooks will:
   - Format code with black
   - Sort imports with isort
   - Check YAML files
   - Validate commit messages
   - Generate requirements.txt
