from src.utils.allutills import Read_Yaml,Create_Dir,log_model_summary
from src.utils.models import own_model,prepared_model
import argparse
import  os
from typing import Optional
from pathlib import Path

import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

def prepared_base_model(config_path:Path,params_path:Path):
    config = Read_Yaml(config_path) 
    params = Read_Yaml(params_path)

    artifact = config['artifacts'] 

    artifatcs_dir = artifact['Artifatcs_dir']
    base_model_dir = artifact["Based_model_dir"]
    base_model_name = artifact["Based_model_name"]
    updated_model_name = artifact['Updated_model_path']
    
    base_model_dir_path = os.path.join(artifatcs_dir, base_model_dir)
    base_model_path = os.path.join(base_model_dir_path, base_model_name)
    
    Create_Dir([artifatcs_dir,base_model_dir_path])

    base_model = own_model(img_shape=params['img_shape']
                        , num_classes=params['classes']
                        ,model_path=base_model_path)

    full_model = prepared_model(base_model 
                                ,learning_rate=params['lr']
                                ,momentum=params['momentum']
                                ,nesterov=params['nesterov']
                                ,metrics=params['metrics'])

    updated_model_path = os.path.join(base_model_dir_path,updated_model_name)
    full_model.save(updated_model_path)
    logging.info(f'model summary was {log_model_summary(full_model)}')
    logging.info(f'Updated model was saved at {updated_model_path}')





if __name__ == '__main__':
    args = argparse.ArgumentParser(description='get the data from bucket')
    args.add_argument('--config','-c',default='config/config.yaml')
    args.add_argument('--params','-p',default='params.yaml')

    parsed_args = args.parse_args()

    try:
        logging.info("stage four started >>>>>>>>>>>")
        prepared_base_model(config_path=parsed_args.config,params_path=parsed_args.params)
        logging.info("stage four is create base model completed  ................\n")
    except Exception as e: 
        logging.info(f"Error was occurred {e}\n")
