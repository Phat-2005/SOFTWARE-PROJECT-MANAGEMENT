# SDP Starter

Starter application for **72ITDS30103 Software Development Platforms** (Van Lang University, FIT).
A small FastAPI web API that you will containerise, connect to a database, deploy and test
during the course.

## Get your own copy (Week 2, one member per team)

1. On this page, click **Use this template → Create a new repository**.
2. Owner: your account. Name: your team's repository name. Visibility: **Public**.
3. Click **Create repository**.
4. In the new repository: **Settings → Collaborators → Add people**, and add each teammate.
5. Everyone clones the new repository over SSH:

   ```bash
   git clone git@github.com:<owner>/<team-repo>.git
   ```

Do not fork this repository and do not push to it — work only in your team's copy.

## Run it on your machine

In Git Bash, from the repository folder:

```bash
python -m venv .venv
source .venv/Scripts/activate        # Windows Git Bash
# source .venv/bin/activate          # macOS / Linux
pip install -r requirements-dev.txt
python -m uvicorn app.main:app --port 8000
```

Open http://localhost:8000 — you should see a JSON greeting.
Also try http://localhost:8000/health and http://localhost:8000/docs.
Press Ctrl+C to stop.

## Run the tests

```bash
pytest
```
## Run with Compose (Week 4)

### Requirements

- Podman 4 or later with a Compose provider, or Docker Desktop.
- Git installed.

### Start the application

1. Clone the repository:

   ```bash
   git clone https://github.com/Phat-2005/SOFTWARE-PROJECT-MANAGEMENT.git
   cd SOFTWARE-PROJECT-MANAGEMENT
   ```

2. Create the environment file:

   ```bash
   cp .env.example .env
   ```

3. Edit `.env` and set `DB_PASSWORD` to a password containing letters and digits only. Do not commit `.env`.

4. Build and start the application and PostgreSQL database:

   ```bash
   podman compose up --build
   ```

5. Open http://localhost:3000/health/db.

   Expected response:

   ```json
   {"db":"ok","notes":2}
   ```

   The number of notes may differ if the database already contains additional data.

### Stop the application

```bash
podman compose down
```

The named database volume is preserved when you stop the stack this way.

### Reset the database

**Warning: This deletes the database volume and its data.**

```bash
podman compose down -v
podman compose up --build
```

The database is initialized again using `db/init.sql`.

## What is in here

| Path | What it is |
|---|---|
| `app/main.py` | The application. The FastAPI object is called `app`, so the start command is `app.main:app`. |
| `requirements.txt` | Packages the app needs to run. This is what the Dockerfile installs. |
| `requirements-dev.txt` | Extra packages for testing only. |
| `tests/` | Tests run by `pytest`, and by the pipeline from Week 6. |
| `.env.example` | Every environment variable the app reads, with no secret values. |
| `TEAM.md` | Team members. |
| `notes/` | Personal notes, one file per person. |

## Endpoints

| Method | Path | Returns |
|---|---|---|
| GET | `/` | App name, version and a greeting |
| GET | `/health` | `{"status": "ok"}` — used by Render and the pipeline |
| GET | `/items` | A list of items |
| GET | `/items/{id}` | One item, or 404 |
| GET | `/docs` | Interactive API documentation |

## Environment variables

| Name | Needed from | Meaning |
|---|---|---|
| `APP_NAME` | optional | Name shown by `/` |
| `DATABASE_URL` | Week 4 | PostgreSQL connection string |
