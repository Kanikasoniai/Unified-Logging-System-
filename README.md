# Unified Logging System

## Overview

The Unified Logging System is a centralized logging framework built using Python and Flask. It standardizes log generation across multiple modules and stores logs in a common JSON format for debugging, monitoring, and analytics.

## Objective

* Standardize logs across all modules
* Enable debugging and monitoring
* Store logs in a consistent format
* Provide API support for centralized logging

---

## Features

* Standardized logging schema
* Centralized log storage
* Reusable logging utility
* Flask API endpoint for log ingestion
* JSON-based storage
* Sample module integration

---

## Project Structure

```text
Unified Logging System/
│
├── app/
│   ├── api.py
│   ├── logger.py
│   ├── schema.py
│   └── storage.py
│
├── modules/
│   ├── auth.py
│   ├── evaluation.py
│   └── notification.py
│
├── logs/
│   └── logs.json
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Log Schema

Each log follows a standard structure:

```json
{
  "module": "evaluation",
  "event": "score_generated",
  "timestamp": "2026-05-31T14:27:30.148765",
  "data": {
    "score": 95
  }
}
```

### Fields

| Field     | Description                           |
| --------- | ------------------------------------- |
| module    | Name of the module generating the log |
| event     | Event type                            |
| timestamp | ISO formatted timestamp               |
| data      | Additional event information          |

---

## Sample Modules

### Authentication Module

```python
log_event(
    module="auth",
    event="user_login",
    data={"user_id": 101}
)
```

### Evaluation Module

```python
log_event(
    module="evaluation",
    event="score_generated",
    data={"score": 95}
)
```

### Notification Module

```python
log_event(
    module="notification",
    event="email_sent",
    data={"recipient": "student@gmail.com"}
)
```

---

## API Endpoint

### POST /log

Stores a new log entry.

### Request Body

```json
{
  "module": "test",
  "event": "api_test",
  "data": {
    "status": "success"
  }
}
```

### Response

```json
{
  "message": "Log stored successfully"
}
```

---

## Technologies Used

* Python
* Flask
* Pydantic
* JSON
* Git & GitHub

---

## Constraints Handled

* Standardized inconsistent log formats
* Validation through schema enforcement
* Centralized storage mechanism
* Extensible design for future database integration

---

## Future Enhancements

* SQLite / MongoDB integration
* Log filtering and search APIs
* Log rotation
* Asynchronous logging
* Dashboard for log analytics

---

## Author

**Kanika Soni**

B.Tech (Artificial Intelligence & Machine Learning)
Government Engineering College, Jaipur

GitHub: https://github.com/Kanikasoniai
