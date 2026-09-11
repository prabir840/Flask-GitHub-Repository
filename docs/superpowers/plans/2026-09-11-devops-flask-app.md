# DevOps Flask Application Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a modern, minimal Flask service suitable for Jenkins CI/CD on Ubuntu AWS EC2.

**Architecture:** Keep request handling in `app.py`, presentation in a Jinja template and one stylesheet, and deployment behavior in `Jenkinsfile` plus README instructions. Test the public HTTP contract through Flask's test client.

**Tech Stack:** Python 3, Flask, pytest, HTML, CSS, Jenkins Pipeline, systemd.

**Spec:** `docs/superpowers/specs/2026-09-11-devops-flask-app-design.md`

## Global Constraints

- Listen on `0.0.0.0` port `5000`.
- Keep runtime dependencies minimal and include no credentials.
- Do not add Docker unless required.
- Preserve the existing repository and push to its existing `origin` remote.

---

### Task 1: Define the HTTP contract with tests

**Files:**
- Create: `tests/test_app.py`

**Interfaces:**
- Consumes: the future Flask application object exported as `app` from `app.py`.
- Produces: executable checks for `/` and `/health`.

- [ ] **Step 1: Write the failing tests**

```python
from app import app


def test_home_page_renders_application_content():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert b"Ship with confidence" in response.data


def test_health_endpoint_returns_successful_plain_text_response():
    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.text == "healthy"
    assert response.mimetype == "text/plain"
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/test_app.py -v`
Expected: collection fails because `app.py` does not yet exist.

### Task 2: Implement the Flask service and UI

**Files:**
- Create: `app.py`
- Create: `templates/index.html`
- Create: `static/css/style.css`

**Interfaces:**
- Consumes: the tests from Task 1.
- Produces: `app`, `/`, `/health`, and a responsive CI/CD operations landing page.

- [ ] **Step 1: Implement the minimal routes**

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/health")
def health():
    return "healthy", 200, {"Content-Type": "text/plain; charset=utf-8"}
```

- [ ] **Step 2: Add the responsive template and stylesheet**

The template must include a navbar, hero, feature cards, deployment status content, and footer. The stylesheet must define responsive layouts for narrow screens and use stable spacing and readable contrast.

- [ ] **Step 3: Run the focused tests**

Run: `python -m pytest tests/test_app.py -v`
Expected: both tests pass.

### Task 3: Add deployment and repository configuration

**Files:**
- Create: `requirements.txt`
- Create: `.gitignore`
- Create: `Jenkinsfile`
- Modify: `README.md`

**Interfaces:**
- Consumes: the service contract from Task 2.
- Produces: Ubuntu setup docs, Jenkins stages for checkout/install/test/systemd restart, and Python ignore rules.

- [ ] **Step 1: Add the dependency and ignore files**

`requirements.txt` contains Flask and pytest. `.gitignore` excludes virtual environments, Python caches, coverage output, local environment files, and editor metadata.

- [ ] **Step 2: Add the Jenkins pipeline**

The pipeline uses `python3 -m venv .venv`, installs requirements, runs `python -m pytest`, and invokes `sudo systemctl restart flask-github-repository.service` in a deployment stage.

- [ ] **Step 3: Document local and Jenkins usage**

README sections must cover project description, features, structure, virtualenv setup, startup on `0.0.0.0:5000`, `/health`, and the systemd/Jenkins deployment overview.

### Task 4: Verify, commit, and push

**Files:**
- Verify: all project files and git state.

- [ ] **Step 1: Run the full test suite**

Run: `python -m pytest -v`
Expected: all tests pass.

- [ ] **Step 2: Start the service and check HTTP behavior**

Run: `python app.py` in a background terminal, then request `http://127.0.0.1:5000/health` and stop the process. Expected response: `healthy`.

- [ ] **Step 3: Verify required files and git status**

Run: `git status --short` and confirm `app.py`, `requirements.txt`, `templates/`, `static/css/`, `README.md`, `Jenkinsfile`, `.gitignore`, and `tests/` are present.

- [ ] **Step 4: Commit and push**

Run: `git add .; git commit -m "feat: add Jenkins-ready Flask application"; git push origin main`.