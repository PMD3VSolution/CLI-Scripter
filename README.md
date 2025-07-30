# CLI-Scripter

This repository provides a simple Python application that allows you to establish an SSH connection to a remote system from a Windows environment. The application uses a minimal Tkinter GUI to collect connection details (host, username, password, port) and attempts to connect using `paramiko`.

## Requirements

- Python 3.8+
- `paramiko`

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

Run the application from a command prompt:

```bash
python ssh_client.py
```

Enter your SSH credentials in the GUI and press **Connect**. A message box will display whether the connection succeeded or failed.
