# DevOps Flask Application Design

## Goal

Create a small, polished Flask application that demonstrates a reliable CI/CD-ready service for a Jenkins and AWS EC2 assignment.

## Architecture

The application uses Flask's built-in routing and Jinja templates. The home page is rendered from `templates/index.html`, styled by `static/css/style.css`, and exposes a plain-text `/health` endpoint for load balancers and deployment checks. No database, external API, Docker image, secrets, or unnecessary runtime library is required.

The Jenkins pipeline creates or reuses a Python virtual environment, installs `requirements.txt`, runs pytest, and restarts a preconfigured `flask-github-repository.service` systemd unit. The README documents the expected Ubuntu setup and service contract.

## Requirements

- Listen on `0.0.0.0` port `5000`.
- Provide `/` and `/health` routes.
- Use a responsive navbar, hero section, feature cards, footer, and mobile layout.
- Include tests for the home page and health endpoint.
- Include `.gitignore`, `requirements.txt`, `Jenkinsfile`, and deployment documentation.
- Keep runtime dependencies minimal and include no credentials.