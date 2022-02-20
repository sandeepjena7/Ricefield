from src.utils.allutills import *
import argparse
import os
from typing import Optional
from pathlib import Path
import logging
from tqdm import tqdm


def download_files(source_file_name:Path,destination_file_name:Path):# https://gist.github.com/gargolito/073dead3ed3daac2f93dcdc5d4274f18

    fsize = int(os.path.getsize(source_file_name))
    with open(source_file_name, 'rb') as f:
        with open(destination_file_name, 'ab') as n:
            with tqdm(ncols=60, total=fsize, bar_format='{l_bar}{bar} | Remaining: {remaining}') as pbar:
                buffer = bytearray()
                while True:
                    buf = f.read(8192)
                    n.write(buf)
                    if len(buf) == 0:
                        break
                    buffer += buf
                    pbar.update(len(buf))


logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
Create_Dir([log_dir])
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")



def get_data(config:Optional[Path]) -> None:

    config= Read_Yaml(config)
    source_data_dir = config['data_source']['Download_data_dir']
    source_data_filename = config['data_source']['Dataset_name']
    files_name_path = os.path.join(source_data_dir,source_data_filename)
    data = "D:\\data\\rice\\rice.tgz"
    download_files(data,files_name_path)


if __name__ == '__main__':
    args = argparse.ArgumentParser(description='get the data from bucket')
    args.add_argument('--config','-c',default='config/config.yaml')
    parsed_args = args.parse_args()

    try:
        logging.info("stage two started >>>>>>>>>>>")
        get_data(config=parsed_args.config)
        logging.info("stage two is extract_data completed ................\n")
    except Exception as e: 
        logging.info(f"Error was occurred {e}\n")