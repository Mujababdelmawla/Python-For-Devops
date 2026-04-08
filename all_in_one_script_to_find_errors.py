import subprocess
import re 
class TaskManager:
    def __init__(self):
        self.logs = []
    def execute_command(self, command):
        # run the system command 
        result = subprocess.run(command, capture_output=True , text=True , shell=True)
        # log both stdout and stderr (for error detection)
        self.logs.append(result.stdout + result.stderr)
        print(f"\n--- command output ---\n){result.stdout}{result.stderr}")
        return result.stdout + result.stderr 

    def parse_logs(self):
        # regex to detect errors|warnings 
        error_pattern = r"(error|warning)"
        errors = []
        for log in self.logs:
            errors.extend(re.findall(error_pattern, log, re.IGNORECASE))
            return errors




task_manager = TaskManager()
# intentionally run a command that fails to generate an error 
output = task_manager.execute_command("ls /nonexistentdirectory")
# parse for errors or warnings 
errors = task_manager.parse_logs
print(f"\n Errors Found : {errors}")