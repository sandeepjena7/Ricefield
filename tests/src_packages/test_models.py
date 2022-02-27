
from common import start_print
from common import status_print
from tensorflow import keras
import os
from src.utils.callbacks import (create_and_save_checkpint_callbacks
                                ,create_and_save_tesnoboard_callbacks
                                ,get_callbacks )


def test_save_callbacks(system_dict):
    forward = True 

    test = 'test_ create_and_save_tesnoboard_callbacks'
    system_dict["total_tests"] += 1
    start_print(system_dict['total_tests'],test)

    if forward:
        try:
            dir_ = "Workspace"
            tensoboard_log = os.path.join(dir_,'tb_logs')
            os.makedirs(tensoboard_log,exist_ok=True)

            ts = create_and_save_tesnoboard_callbacks(dir_,tensoboard_log)
            system_dict['successful_tests'] += 1
            status_print("Pass")

        except Exception as e:
            system_dict['failed_tests_exceptions'].append(e) 
            system_dict['failed_tests_lists'] .append(test) 
            status_print("Fail")
            forward = False
    else:
        system_dict['skipped_tests_lists'].append(test)
        status_print("Skipped")


    test='test_create_and_save_checkpint_callbacks'
    system_dict["total_tests"] += 1
    start_print(system_dict['total_tests'],test)

    if forward:
        try:
            dir_ = "Workspace"
            che_dir = os.path.join(dir_,'chek')
            os.makedirs(che_dir,exist_ok=True)

            ts = create_and_save_checkpint_callbacks(dir_,che_dir)
            system_dict['successful_tests'] += 1
            status_print("Pass")

        except Exception as e:
            system_dict['failed_tests_exceptions'].append(e) 
            system_dict['failed_tests_lists'] .append(test) 
            status_print("Fail")
            forward = False

    else:
        system_dict['skipped_tests_lists'].append(test)
        status_print("Skipped")

    test='test_get_callbacks'
    system_dict["total_tests"] += 1
    start_print(system_dict['total_tests'],test)

    if forward:
        try:
            dir_ = "Workspace"

            ts = get_callbacks(dir_)
            system_dict['successful_tests'] += 1
            status_print("Pass")

        except Exception as e:
            system_dict['failed_tests_exceptions'].append(e) 
            system_dict['failed_tests_lists'] .append(test) 
            status_print("Fail")
            forward = False

    else:
        system_dict['skipped_tests_lists'].append(test)
        status_print("Skipped")

    
    return system_dict
