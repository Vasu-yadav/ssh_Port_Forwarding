import subprocess
import shlex

class TunnelManager:
    def __init__(self):
        # Store tunnels as: { host: [ {local, remote, process, active} ] }
        self.tunnels = {}

    def get_ports_for_host(self, host):
        return self.tunnels.get(host, [])

    def start_tunnel(self, host, port):
        if port["active"]:
            return
        cmd = f"ssh -N -L {port['local']}:localhost:{port['remote']} {host}"
        try:
            proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            port["process"] = proc
            port["active"] = True
        except Exception as e:
            print(f"Failed to start tunnel for {host}: {e}")
            port["active"] = False

    def stop_tunnel(self, host, port):
        proc = port.get("process")
        if proc:
            proc.terminate()
            proc.wait()
        port["active"] = False
        port["process"] = None

    def is_any_tunnel_active(self, host):
        return any(p["active"] for p in self.tunnels.get(host, []))

    def add_port_forward(self, host, local, remote):
        if host not in self.tunnels:
            self.tunnels[host] = []
        self.tunnels[host].append({
            "local": local,
            "remote": remote,
            "active": False,
            "process": None
        })