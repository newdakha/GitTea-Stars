# Gitea Fake Stars

![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![Gitea](https://img.shields.io/badge/Gitea-API-609926?logo=gitea)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Stars a chosen Gitea repository using fake accounts stored in `users.db` (created by Gitea Fake Followers).

---

## Setup

1. Run [Gitea Fake Followers](../fake-followers) first to populate `users.db`
2. Set your values in the config block:

```python
GITEA_URL   = "http://your-gitea-instance/api/v1"
ADMIN_TOKEN = "your-admin-token"
TARGET_USER = "username"
```

3. Run: `python main.py`

---

## How it works

- Lists all repos of `TARGET_USER`
- Reads bot accounts from `users.db`
- Each selected bot stars the chosen repo
