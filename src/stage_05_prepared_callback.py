from src.utils.allutills import Read_Yaml,Create_Dir
from src.utils.callbacks import create_and_save_checkpint_callbacks,create_and_save_tesnoboard_callbacks
import argparse
import  os
from pathlib import Path

import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

def prepared_base_model(config_path:Path) -> None:
    config = Read_Yaml(config_path) 

    artifact = config['artifacts'] 
    artifatcs_dir = artifact['Artifatcs_dir']

    tensoboard_log_dir = os.path.join(artifatcs_dir
                        ,artifact['Tensorboard_dir'])
    
    checkpoint_dir = os.path.join(artifatcs_dir
                        ,artifact['Checkpoint_dir'])

    callback_dir = os.path.join(artifatcs_dir
                        ,artifact['Callback_dir'])
    
    Create_Dir([
        tensoboard_log_dir
        ,checkpoint_dir
        ,callback_dir
    ])

    create_and_save_tesnoboard_callbacks(callback_dir,tensoboard_log_dir)
    create_and_save_checkpint_callbacks(callback_dir,checkpoint_dir)




if __name__ == '__main__':
    args = argparse.ArgumentParser(description='get the data from bucket')
    args.add_argument('--config','-c',default='config/config.yaml')

    parsed_args = args.parse_args()

    try:
        logging.info("stage four started >>>>>>>>>>>")
        prepared_base_model(config_path=parsed_args.config)
        logging.info("stage four is callback create done was done  ................")
    except Exception as e: 
        logging.info(f"Error was occurred {e}")
