import tkinter as tk
from tkinter import messagebox
import paramiko


def connect_ssh(host, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, port=int(port), username=username, password=password)
        return True, "Connection successful"
    except Exception as exc:
        return False, str(exc)
    finally:
        client.close()


def create_gui():
    root = tk.Tk()
    root.title("SSH Client")

    host_var = tk.StringVar()
    port_var = tk.StringVar(value="22")
    user_var = tk.StringVar()
    pwd_var = tk.StringVar()

    def on_connect():
        host = host_var.get().strip()
        port = port_var.get().strip() or "22"
        user = user_var.get().strip()
        pwd = pwd_var.get()
        if not host or not user:
            messagebox.showerror("Error", "Host and username are required")
            return
        success, msg = connect_ssh(host, port, user, pwd)
        if success:
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Connection Failed", msg)


    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill=tk.BOTH, expand=True)


    # Host
    host_label = tk.Label(frame, text="Host:")
    host_label.grid(row=0, column=0, sticky=tk.W)
    host_entry = tk.Entry(frame, textvariable=host_var)
    host_entry.grid(row=0, column=1)

    # Port
    port_label = tk.Label(frame, text="Port:")
    port_label.grid(row=1, column=0, sticky=tk.W)
    port_entry = tk.Entry(frame, textvariable=port_var)
    port_entry.grid(row=1, column=1)

    # Username
    user_label = tk.Label(frame, text="Username:")
    user_label.grid(row=2, column=0, sticky=tk.W)
    user_entry = tk.Entry(frame, textvariable=user_var)
    user_entry.grid(row=2, column=1)

    # Password
    pwd_label = tk.Label(frame, text="Password:")
    pwd_label.grid(row=3, column=0, sticky=tk.W)
    pwd_entry = tk.Entry(frame, textvariable=pwd_var, show="*")
    pwd_entry.grid(row=3, column=1)

    connect_btn = tk.Button(frame, text="Connect", command=on_connect)
    connect_btn.grid(row=4, column=0, columnspan=2, pady=(10, 0))

    root.mainloop()


def main():
    create_gui()


if __name__ == "__main__":
    main()
