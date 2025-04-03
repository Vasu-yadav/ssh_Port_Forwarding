# 🔐 SSH Port Forwarder (Cross-Platform GUI App)

A simple, cross-platform desktop app to manage SSH port forwarding using an easy-to-use GUI — inspired by VS Code's Ports panel.

Built with **Python** and **PyQt6**, this tool helps you:
- Parse your `~/.ssh/config`
- Create local-to-remote port tunnels
- Start/stop tunnels with a click
- View tunnel status in a table view

---

## 📦 Features

- 🔍 Auto-detect SSH hosts from `~/.ssh/config`
- 🪟 Clean UI similar to VS Code's PORTS panel
- 🔄 Start/Stop SSH port forwarding with one click
- 💾 Save common tunnel settings
- ⚙️ Easily extendable and cross-platform (macOS, Windows, Linux)

---

## 🧱 Requirements

- Python 3.8+
- PyQt6
- sshconf

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

```bash
python main.py
```

The app will launch with a GUI that allows you to select SSH hosts, specify ports, and manage tunnels.

---

## 📂 Project Structure

```
ssh_port_forwarder/
├── main.py               # Entry point
├── ssh_config_parser.py  # Parses ~/.ssh/config
├── tunnel_manager.py     # Manages SSH subprocesses
├── requirements.txt
└── README.md
```

---

## 🛠 Example SSH Tunnel Command Used

Under the hood, the app runs commands like:

```bash
ssh -N -L <local_port>:<remote_host>:<remote_port> user@host_alias
```

You must have valid entries in your `~/.ssh/config`.

---

## 🧪 Sample ~/.ssh/config

```ssh
Host dev-server
  HostName 192.168.1.100
  User ubuntu
  IdentityFile ~/.ssh/id_rsa
```

---

## 📦 Packaging the App

You can build standalone binaries for macOS, Windows, or Linux using:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

Or use `--windowed` to suppress terminal on launch (especially for Windows/macOS GUI):

```bash
pyinstaller --windowed main.py
```

---

## 📌 Roadmap

- [ ] System tray support
- [ ] Auto-reconnect on disconnect
- [ ] Save/load tunnel profiles
- [ ] Optional autossh integration

---

## 👨‍💻 Author

Made with ❤️ using Python & Qt

---

## 📝 License

Apache 2.0 License