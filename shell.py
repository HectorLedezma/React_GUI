import os
import subprocess

class Shell:
    def exec(commad):
        subprocess.run(commad, shell=True, capture_output=False, text=True)
    
    