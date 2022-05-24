import subprocess

for i in range(1,256):
	subprocess.run(["ping" ,f"10.25.25.{i}", "-c", "3"])
