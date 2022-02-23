
from common import start_print
from common import status_print
from tensorflow import keras
import os
from src.utils.datamangement import train_valid_genrator

def test_train_valid_genrator(system_dict):
    forward = True 

    test = 'test_train_valid_genrator'
    system_dict["total_tests"] += 1
    start_print(system_dict['total_tests'],test)

    if forward:
        try:
            ts_trai,ts_val = train_valid_genrator(data_dir="data/processed"
                                                ,batch_size=32
                                                ,img_size=(224,224)
                                                ,do_data_agumentaion=True
                                                )

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
