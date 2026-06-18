import sqlite3, requests

# ─── CONFIG ───────────────────────────────────────────────────────────────────
GITEA_URL   = "http://100.117.79.103:8080/api/v1"
ADMIN_TOKEN = "your-admin-token"
TARGET_USER = "newdakha"
# ──────────────────────────────────────────────────────────────────────────────

headers = {"Authorization": f"token {ADMIN_TOKEN}"}

repos = [r["name"] for r in requests.get(f"{GITEA_URL}/users/{TARGET_USER}/repos", headers=headers).json()]
for i, repo in enumerate(repos):
    print(f"[{i}] {repo}")

chosen_repo = repos[int(input("Choose repo index: "))]

conn   = sqlite3.connect("users.db")
bots   = conn.cursor().execute("SELECT username, password FROM users").fetchall()
conn.close()

count = min(int(input(f"How many stars? (1-{len(bots)}): ")), len(bots))

for username, password in bots[:count]:
    res = requests.put(f"{GITEA_URL}/user/starred/{TARGET_USER}/{chosen_repo}", auth=(username, password))
    if res.status_code in (200, 204):
        print(f"[+] {username} starred {chosen_repo}")
    else:
        print(f"[-] Failed {username}: {res.status_code}")

print("Done.")
