import subprocess

# Run script1.py
process1 = subprocess.Popen(['python3', 'putter.py'])

# Run script2.py
process2 = subprocess.Popen(['python3', 'getter.py'])

# Wait for both processes to finish
process1.wait()
process2.wait()

print("Both scripts have finished.")
