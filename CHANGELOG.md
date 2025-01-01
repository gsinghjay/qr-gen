# CHANGELOG



## v0.1.1 (2025-01-01)

### Fix

* fix(release): install commitizen in release workflow

# Why:
- Fix release workflow failure
- Enable automated version bumping
- Ensure all required tools are available

# What:
- Added dependency installation step
- Included dev dependencies in Poetry install
- Maintained existing release configuration ([`11b30a7`](https://github.com/gsinghjay/qr-gen/commit/11b30a7352d7edd85a2bdd50472781dbc5b28df3))

### Unknown

* Merge pull request #3 from gsinghjay/test/release-workflow

fix(release): install commitizen in release workflow ([`93de1e6`](https://github.com/gsinghjay/qr-gen/commit/93de1e69ce263cbfdc4a852b6150eea1b67f925f))


## v0.1.0 (2025-01-01)

### Build

* build(deps): configure poetry dependencies

# Why:
- Set up project dependencies
- Configure development tools
- Establish project metadata

# What:
- Added FastAPI and core dependencies
- Configured development tools (black, isort, mypy)
- Set up pytest and testing tools
- Added commitizen for versioning ([`3d0408a`](https://github.com/gsinghjay/qr-gen/commit/3d0408a31771bda7206bb8acf861c5faf4a43e32))

* build(deps): add poetry.lock file

# Why:
- Ensure reproducible builds
- Lock dependency versions

# What:
- Added poetry.lock with exact versions
- Includes all production and development dependencies
- Configured for Python 3.11+ ([`94bbe62`](https://github.com/gsinghjay/qr-gen/commit/94bbe62f153762e445d3b226c5a3c3b52f0dcd68))

### Chore

* chore(init): initialize project structure

# Why:
- Set up initial project structure
- Configure version control
- Establish licensing

# What:
- Added .gitignore for Python projects
- Added MIT license
- Created basic README.md ([`9b5174d`](https://github.com/gsinghjay/qr-gen/commit/9b5174d0d25053bc7e6e90fdd90ff5dde684b898))

* chore(deps): update poetry configuration to use groups

# Why:
- Modernize dependency management
- Better organize development dependencies
- Support newer Poetry features

# What:
- Migrated from dev-dependencies to group.dev.dependencies
- Added test group for test-specific dependencies
- Updated tool configurations ([`c322cf0`](https://github.com/gsinghjay/qr-gen/commit/c322cf04a18c61d9414bb9f5138d71651c86d957))

* chore(config): add environment variables template

# Why:
- Provide template for required environment variables
- Document configuration options
- Ensure secure handling of sensitive data

# What:
- Added .env.example template with:
  - Database configurations
  - JWT settings
  - API configurations
  - Monitoring settings
  - Development options ([`884549f`](https://github.com/gsinghjay/qr-gen/commit/884549f3682f4341fdf4e0ada3d169a03c4c2f67))

* chore(deps): add poetry project configuration

# Why:
- Set up Python package management with Poetry
- Define project dependencies and development tools
- Configure project metadata and build settings

# What:
- Created pyproject.toml with:
  - Project metadata and dependencies
  - Development dependencies
  - Tool configurations for:
    - Black
    - isort
    - mypy
    - pytest
    - commitizen
- Set Python 3.11 as minimum version
- Added package build configuration ([`4239212`](https://github.com/gsinghjay/qr-gen/commit/423921279e500567d92fe0dcea923629b999cf55))

* chore(git): add pre-commit hooks configuration

# Why:
- Enforce consistent code quality and style
- Automate code formatting and validation
- Ensure commit message standards

# What:
- Added pre-commit hooks for:
  - Code formatting with black (v24.2.0)
  - Import sorting with isort (v5.13.2)
  - Type checking with mypy (v1.8.0)
  - Commit message validation with commitizen (v3.14.1)
  - Poetry dependency management (v1.7.1)
- Configured basic file checks:
  - Trailing whitespace
  - File ending fixes
  - YAML validation
  - Large file checks
- Set Python 3.11 as default version
- Added CI auto-fix and auto-update commit messages ([`247ebdb`](https://github.com/gsinghjay/qr-gen/commit/247ebdb061f255ef2f9d5e008b806429810a0295))

### Ci

* ci(release): add workflow permissions

# Why:
- Fix release workflow permissions
- Enable automated version bumping
- Allow GitHub Actions to create releases

# What:
- Added write permissions for contents
- Added write permissions for pull-requests
- Added write permissions for issues
- Maintained semantic release configuration ([`c9a3ff4`](https://github.com/gsinghjay/qr-gen/commit/c9a3ff4102ee45522111e812ec7f008d1d3ae793))

* ci(workflow): update commit validation strategy

Why:
- Previous commit validation was failing on PR branches
- Needed to simplify commit message validation

What:
- Move commit validation to push events on main branch only
- Add fetch-depth: 0 to checkout action
- Simplify commit range check to last commit ([`562e652`](https://github.com/gsinghjay/qr-gen/commit/562e65225ee428ff31ebc9e977a7d8778dd9d826))

* ci(pre-commit): remove mypy from pre-commit hooks

# Why:
- Fix pre-commit hook installation issues
- Simplify pre-commit configuration
- Remove problematic dependency

# What:
- Removed mypy pre-commit hook
- Kept essential code quality checks
- Maintained commitizen for commit validation ([`e6631b9`](https://github.com/gsinghjay/qr-gen/commit/e6631b944b2e78c0fb341a8f9541c0f4564deaa1))

* ci(workflow): add commit message validation ([`7a97e0c`](https://github.com/gsinghjay/qr-gen/commit/7a97e0c21cbcc2d281e0d3e02a0e9a0946486f3b))

* ci: add github actions and linting

# Why:
- Establish CI/CD pipeline
- Configure code quality checks
- Set up automated releases

# What:
- Added CI workflow for testing and linting
- Added release workflow for versioning
- Configured pylint with .pylintrc
- Set up PR validation checks ([`780ec0e`](https://github.com/gsinghjay/qr-gen/commit/780ec0e574353b4eb4fec95cfd7889924e5eb23a))

### Documentation

* docs(readme): update project documentation

# Why:
- Improve project documentation clarity
- Remove mypy references
- Add detailed Git workflow section

# What:
- Updated pre-commit hooks information
- Added Git workflow section with commit examples
- Clarified installation steps
- Removed mypy from tech stack
- Updated badges with correct repository links

# Note:
- Maintains backward compatibility
- Follows conventional commits
- Updates reflect current project structure ([`5aa5391`](https://github.com/gsinghjay/qr-gen/commit/5aa539137f330e3cb2f89a1547236ec083eb1a9e))

* docs(readme): add comprehensive project documentation

# Why:
- Provide clear project overview
- Document setup instructions
- Guide developers through contribution process

# What:
- Added project features and tech stack
- Included installation instructions
- Documented testing procedures
- Added development workflow
- Explained commit conventions
- Included version management details
- Added license information
- Linked to ROADMAP.md

# Note:
- Follows best practices for OSS documentation
- Includes all necessary badges and sections
- References semantic versioning ([`cd3e286`](https://github.com/gsinghjay/qr-gen/commit/cd3e286cd85889ec339ffa40ac0c2f6d86d41c89))

* docs(roadmap): add detailed project roadmap

# Why:
- Define clear project development phases
- Document technical requirements
- Establish project milestones

# What:
- Added 9 development phases:
  - Project Setup and Standards
  - REPL Development
  - Core Implementation
  - API Development
  - Testing and QA
  - Monitoring and Logging
  - Deployment
  - Documentation
  - Maintenance
- Included code examples and configurations
- Defined project structure ([`185e643`](https://github.com/gsinghjay/qr-gen/commit/185e6434749dc5fca32c1e7740ad0d00ca89308c))

* docs(readme): add comprehensive project roadmap and structure

# Why:
- Establish clear development phases and technical requirements
- Define FastAPI-based project structure
- Document development standards and CI/CD pipeline

# What:
- Added detailed implementation phases from setup to maintenance
- Defined FastAPI-specific project structure:
  - Routers, models, schemas, and CRUD operations
  - External services and utilities
  - Testing framework setup
- Included Poetry for dependency management
- Added CI/CD configuration with:
  - Commitizen and commitlint
  - Semantic versioning
  - GitHub Actions workflows
  - Testing and code quality checks ([`fca23d6`](https://github.com/gsinghjay/qr-gen/commit/fca23d65d1c120835d1091dc0c36eeeb054eb34f))

### Feature

* feat(structure): initialize project structure

# Why:
- Set up clean architecture for the QR code generator
- Establish modular project organization
- Follow FastAPI best practices

# What:
- Created core application structure:
  - crud/: Database operations
  - models/: SQLAlchemy models
  - schemas/: Pydantic models
  - routers/: API endpoints
  - external_services/: External integrations
- Added main.py for FastAPI application
- Added dependencies.py for dependency injection
- Set up __init__.py files for proper packaging

# Note:
- Follows clean architecture principles
- Prepares for modular development
- Enables easy testing and maintenance ([`687800e`](https://github.com/gsinghjay/qr-gen/commit/687800e74774be3907b14d4da141730b1ac18a3c))

* feat(core): add application configuration

# Why:
- Establish core application settings
- Set up environment configuration handling

# What:
- Created Settings class using pydantic-settings
- Added basic configuration for project name, version, and database
- Implemented environment variable support ([`c2a15b5`](https://github.com/gsinghjay/qr-gen/commit/c2a15b5f2f90973a5dc88f08978db9610215e021))

### Style

* style(lint): fix pylint issues and improve code organization

Why:
- Code had several pylint issues affecting code quality score
- Import organization needed improvement

What:
- Fixed import order in conftest.py with proper pylint comments
- Renamed app variable to fastapi_app to avoid shadowing
- Fixed trailing whitespace and newline issues
- Improved pylint score to 10.00/10 ([`19b40fe`](https://github.com/gsinghjay/qr-gen/commit/19b40fe10121ec0ca24491d288bc20aa63ead3f0))

### Test

* test(setup): initialize testing infrastructure

# Why:
- Enable automated testing
- Set up test fixtures and configuration

# What:
- Added conftest.py with FastAPI TestClient fixture
- Created initial test case for main application
- Configured pytest path handling ([`c7a57ea`](https://github.com/gsinghjay/qr-gen/commit/c7a57ea634465bd78d6cccd8a56f145b6a1cfa62))

* test: add initial pytest configuration

# Why:
- Set up testing infrastructure
- Configure test database and fixtures
- Enable async test support

# What:
- Added conftest.py with:
  - Database fixtures
  - FastAPI test client
  - Authentication helpers
- Configured async test support
- Added test database setup ([`8f4cb08`](https://github.com/gsinghjay/qr-gen/commit/8f4cb081786f9b00d6c5d5889344874b43220798))

### Unknown

* Merge pull request #2 from gsinghjay/test/release-workflow

ci(release): add workflow permissions ([`295afbd`](https://github.com/gsinghjay/qr-gen/commit/295afbd7b794c866400904b04170651c7abd5543))

* Merge pull request #1 from gsinghjay/test/github-actions

ci: Test/GitHub actions ([`1d91b13`](https://github.com/gsinghjay/qr-gen/commit/1d91b132a690e7bae346ec4070aef1471516b5cd))

* Initial commit ([`56fa104`](https://github.com/gsinghjay/qr-gen/commit/56fa1046d35576f070dd5ff3d7d41a9873dbd690))
