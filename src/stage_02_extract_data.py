from src.utils.allutills import *
import argparse
import os
from typing import Optional
from pathlib import Path
import tarfile
import os
from tqdm import tqdm
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
Create_Dir([log_dir])
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

def extract_tarfile(filepath:Optional[Path],destdir:Path) -> None: # https://stackoverflow.com/questions/3667865/python-tarfile-progress-output
    with tarfile.open(filepath) as file:
        for member in tqdm(iterable=file.getmembers(), total=len(file.getmembers()), colour="green"):
            file.extract(member,path=destdir)

def extract_data(config:Optional[Path]) -> None:

    config= Read_Yaml(config)
    source_data_dir = config['data_source']['Download_data_dir']
    source_data_filename = config['data_source']['Dataset_name']
    local_data_dir = config['data_source']['Raw_data_dir']
    Create_Dir([local_data_dir])
    dataset = os.path.join(source_data_dir,source_data_filename)
    extract_tarfile(dataset,local_data_dir)



if __name__ == '__main__':
    args = argparse.ArgumentParser(description='get the data from bucket')
    args.add_argument('--config','-c',default='config/config.yaml')
    parsed_args = args.parse_args()

    try:
        logging.info("stage two started >>>>>>>>>>>")
        extract_data(config=parsed_args.config)
        logging.info("stage two is extract_data completed ................")
    except Exception as e: 
        logging.info(f"Error was occurred {e}")