
from src.utils.allutills import Read_Yaml
from common import start_print
from common import status_print



def test_Read_Yaml(system_dict):
    forward = True 

    test = 'test_Read_Yaml'
    system_dict["total_tests"] += 1
    start_print(system_dict['total_tests'],test)

    if forward:
        try:
            yam = Read_Yaml("params.yaml")
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

