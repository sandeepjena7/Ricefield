from src.utils.allutills import *
import argparse
import  os
from typing import Optional
from pathlib import Path
import splitfolders
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")


def prepared_data(config:Optional[Path]):

    config= Read_Yaml(config)
    local_data_dir = config['data_source']['Raw_data_dir']
    processed_data_dir = config['data_source']['Process_data_dir']
    train_ratio = config['data_source']['Train']
    test_ratio = config['data_source']['Test']
    valid_ratio = config['data_source']['Valid']

    Create_Dir([processed_data_dir])
    splitfolders.ratio(local_data_dir,processed_data_dir,ratio=(train_ratio,valid_ratio,test_ratio),move=True)

if __name__ == '__main__':
    args = argparse.ArgumentParser(description='get the data from bucket')
    args.add_argument('--config','-c',default='config/config.yaml')
    parsed_args = args.parse_args()

    try:
        logging.info("stage three started >>>>>>>>>>>")
        prepared_data(config=parsed_args.config)
        logging.info("stage three is split dataset into (train,test,valid) folder  completed ................")
    except Exception as e: 
        logging.info(f"Error was occurred {e}")