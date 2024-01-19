import os
from subprocess import Popen, PIPE, STDOUT
class Shell:
    def exec(command=None):
        print(f'\nejecutando comando {command}\n')
        process = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
        return process.communicate()
        
        #run(commad, shell=True, capture_output=False, text=True)
    
    