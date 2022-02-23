import sys
import os
import time


origstdout = sys.stdout

print("Running Tests...")

os.makedirs("logs",exist_ok=True)
sys.stdout = open(os.path.join("logs","test_logs.txt"), 'w')


system_dict = {};
system_dict["total_tests"] = 0
system_dict["successful_tests"] = 0
system_dict["failed_tests_lists"] = []
system_dict["failed_tests_exceptions"] = []
system_dict["skipped_tests_lists"] = []

os.makedirs("Workspace", exist_ok=True)

start = time.time()

exp_num = 1