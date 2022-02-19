
from src.utils.allutills import Read_Yaml,Create_Dir
from src.utils.callbacks import get_callbacks
from src.utils.models import load_full_model
import argparse
import  os
from pathlib import Path

import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

def train_model(config_path:Path) -> None:
    config = Read_Yaml(config_path) 

    artifact = config['artifacts'] 
    artifatcs_dir = artifact['Artifatcs_dir']
    train_model_dir = os.path.join(artifatcs_dir,artifact['Train_mode_dir'])

    Create_Dir([train_model_dir])
    callback_dir = os.path.join(artifatcs_dir,artifact['Callback_dir'])

    untrained_based_model_path = os.path.join(artifatcs_dir
                                ,artifact['Based_model_dir']
                                ,artifact['Updated_model_path'])

    model = load_full_model(untrained_based_model_path)
    callbacks = get_callbacks(callback_dir)


if __name__ == '__main__':
    args = argparse.ArgumentParser(description='get the data from bucket')
    args.add_argument('--config','-c',default='config/config.yaml')

    parsed_args = args.parse_args()

    try:
        logging.info("stage six started >>>>>>>>>>>")
        train_model(config_path=parsed_args.config)
        logging.info("stage six model was trained................\n")
    except Exception as e: 
        logging.info(f"Error was occurred {e}\n\n")


