import firefox
import subprocess

with subprocess.Popen(["bash ./firefox/places.sh"], stdout=subprocess.PIPE, shell=True) as proc:
    firefox_files = proc.stdout.read().decode("utf-8").strip().split("\n")

print(firefox)
print(firefox.read.call(firefox_files))
