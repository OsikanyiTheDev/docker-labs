# 📘 Lab 6 — Docker Security Hardening (Flask + MySQL CRUD App)

## 🚀 Overview
This lab improves the Lab 5 Docker Compose Flask + MySQL application by applying container security best practices, improving architecture, and removing insecure configurations.

---

# 🔐 CHANGE LOG (SECURITY HARDENING)

---

## 🔐 CHANGE 1 — Non-root Flask Container

### What was changed
The Flask application container was updated to run as a non-root user.

### Implementation
```dockerfile
RUN useradd -m appuser
USER appuser
````

### Why this is important

* Applies **Principle of Least Privilege**
* Prevents full system access if container is compromised
* Reduces attack surface inside container

---

## 🔐 CHANGE 2 — Environment Variables for Secrets

### What was changed

Database credentials were removed from the Python code and moved to environment variables.

### Before (insecure)

```python
user="root"
password="rootpass"
database="labdb"
```

### After (secure)

```python
import os

host=os.getenv("DB_HOST")
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")
database=os.getenv("DB_NAME")
```

### Why this is important

* Prevents hardcoded secrets in source code
* Makes application portable across environments
* Improves security and maintainability

---

## 🔐 CHANGE 3 — MySQL Non-root User Added

### What was changed

A dedicated MySQL user was created instead of using only root.

### docker-compose update

```yaml
environment:
  MYSQL_ROOT_PASSWORD: rootpass
  MYSQL_DATABASE: labdb
  MYSQL_USER: appuser
  MYSQL_PASSWORD: apppass
```

### Why this is important

* Avoids direct use of root database account
* Implements **database-level least privilege**
* Reduces impact of credential leaks

---

## 🔐 CHANGE 4 — Persistent Database Storage

### What was changed

A Docker volume was added for MySQL data persistence.

### Implementation

```yaml
volumes:
  - db_data:/var/lib/mysql
```

### Why this is important

* Prevents data loss on container restart
* Ensures database persistence across deployments
* Mimics real production database storage

---

## 🔐 CHANGE 5 — MySQL Health Check Added

### What was changed

A health check was added to ensure MySQL is fully ready before Flask connects.

### Implementation

```yaml
healthcheck:
  test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
  timeout: 10s
  retries: 5
```

### Why this is important

* Prevents race condition at startup
* Ensures database availability before application starts
* Improves system reliability

---

## 🔐 CHANGE 6 — DB Connection Refactored

### What was changed

Database connection moved into a reusable function instead of a global connection.

### Before (insecure design)

```python
db = mysql.connector.connect(...)
cursor = db.cursor()
```

### After (secure design)

```python
def get_db():
    return mysql.connector.connect(...)
```

### Why this is important

* Prevents shared connection issues
* Improves thread safety
* Better scalability for real applications

---

## 🔐 CHANGE 7 — Per-request DB Connections

### What was changed

Each request now opens and closes its own database connection.

### Why this is important

* Prevents connection leaks
* Improves reliability under load
* Aligns with production backend patterns

---

# 🧠 FINAL SECURITY IMPROVEMENTS SUMMARY

After this lab, the system now includes:

✔ Non-root container execution
✔ Environment-based configuration
✔ Dedicated MySQL user
✔ Persistent storage
✔ Health checks
✔ Improved DB architecture
✔ Safer request handling

---

# 🚀 ARCHITECTURE (FINAL)

```
Flask Web App (Non-root user)
        │
        ▼
MySQL Database (with user separation)
        │
        ▼
Docker Compose Orchestration
        │
        ▼
Persistent Volume Storage
```


