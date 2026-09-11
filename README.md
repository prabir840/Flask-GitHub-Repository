# Pulse Deploy

A clean, lightweight Flask web application for demonstrating a practical DevOps delivery workflow with Jenkins and Ubuntu AWS EC2.

## Features

- Responsive Flask/Jinja web interface with a navbar, hero section, feature cards, workflow section, and footer.
- Health endpoint at `/health` for deployment checks and load balancers.
- Binds to `0.0.0.0` on port `5000`.
- Pytest coverage for the public HTTP routes.
- Jenkins pipeline for checkout, virtual environment setup, dependency installation, testing, and systemd restart.
- No database, secrets, API keys, Docker, or unnecessary runtime services.

## Project structure

```text
.
├── app.py
├── Jenkinsfile
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   └── css/
│       └── style.css
└── tests/
	└── test_app.py
```

## Local setup

Ubuntu:

```bash
sudo apt update
sudo apt install -y python3 python3-venv
git clone https://github.com/prabir840/Flask-GitHub-Repository.git
cd Flask-GitHub-Repository
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to run

Start the application from the repository root:

```bash
python app.py
```

The service listens on `0.0.0.0:5000`. Open `http://<server-ip>:5000` after allowing TCP port 5000 in the EC2 security group.

Run tests with:

```bash
python -m pytest -v
```

## Health endpoint

Request `http://<server-ip>:5000/health`. A healthy service returns HTTP 200 with the plain-text response `healthy`.

## Jenkins CI/CD overview

The `Jenkinsfile` checks out the repository, creates or reuses `.venv`, installs `requirements.txt`, runs the pytest suite, restarts `flask-github-repository.service`, and confirms that systemd reports the service as active.

Before using the pipeline on Ubuntu, create a systemd unit that runs `app.py` from the deployment directory and grant the Jenkins user the least-privilege `sudo` permission to restart and inspect that unit. Keep credentials in Jenkins or the host environment; do not commit them here.

The EC2 instance must have Python 3, Python venv support, Jenkins, and an inbound security-group rule for port 5000 when direct browser access is required.