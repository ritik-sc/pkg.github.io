import subprocess
import getpass

def run_command(command):
    """Run a shell command with sudo."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def main():
    username = getpass.getuser()
    password = getpass.getpass("Enter Machine Password Please: ")

    # Install Anydesk
    commands = [
        f"echo {password} | sudo -kS bash -c \"wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | apt-key add -\"",
        f"echo {password} | sudo -kS bash -c 'echo \"deb http://deb.anydesk.com/ all main\" > /etc/apt/sources.list.d/anydesk-stable.list'",
        f"echo {password} | sudo -kS apt update -y",
        f"echo {password} | sudo -kS apt install -y libgtkglext1",
        f"echo {password} | sudo -kS apt install -y anydesk",
    ]

    for command in commands:
        run_command(command)

    # Check Secure Boot State
    run_command("mokutil --sb-state")

if __name__ == "__main__":
    main()
