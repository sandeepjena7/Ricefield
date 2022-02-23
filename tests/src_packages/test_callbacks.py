
from common import start_print
from common import status_print
from tensorflow import keras
import os

def test_callbacks(system_dict):
    forward = True 

    test = 'test_ tesnoboard_callbacks'
    system_dict["total_tests"] += 1
    start_print(system_dict['total_tests'],test)

    if forward:
        try:
            dir_ = "Workspace"
            ts = keras.callbacks.TensorBoard(log_dir=dir_)
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


    test='test_checkpoint_callbacks'
    system_dict["total_tests"] += 1
    start_print(system_dict['total_tests'],test)

    if forward:
        try:
            dir_ = "Workspace"

            ts = keras.callbacks.ModelCheckpoint(file_path=os.path.join(dir_,'models.h5'))
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
