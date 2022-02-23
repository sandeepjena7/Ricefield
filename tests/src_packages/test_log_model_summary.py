
from src.utils.allutills import log_model_summary
from common import start_print
from common import status_print
from tensorflow import keras

def test_Unique_Filename(system_dict):
    forward = True 

    test = 'test_ log_model_summary'
    system_dict["total_tests"] += 1
    start_print(system_dict['total_tests'],test)

    if forward:
        try:
            
            model = keras.Sequential([
                keras.layers.Dense(2)
            ])

            ts = log_model_summary(model)

            system_dict['successful_tests'] += 1
            status_print("Pass")
        except Exception as e:
            system_dict['failed_tests_exceptions'].append(e) 
            system_dict['failed_tests_lists'] .append(test) 
            status_print("Fail")
    
    else:
        system_dict['skipped_tests_lists'].append(test)
        status_print("Skipped")
    
    return system_dict
