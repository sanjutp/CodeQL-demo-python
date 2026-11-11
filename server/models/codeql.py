import subprocess

def run_command(cmd):
    subprocess.Popen(cmd, shell=True)
