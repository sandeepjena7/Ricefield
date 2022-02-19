import yaml
from pathlib import Path
from typing import Optional,Dict,List,TypeVar
import os
import time
import io
import logging
__all__ = ['Read_Yaml','Create_Dir',"Unique_Filename"]

keras_model = TypeVar('keras_model')
keras_summary = TypeVar('keras_summary')

def Read_Yaml(config:Optional[Path]) -> Dict[str,any] :

    with open(config, 'r') as config_file:
        file = yaml.safe_load(config_file)
        logging.info(f"yaml file was loaded sucessfully from {config} ...")
    return file


def Create_Dir(Names:List[str]) -> None:
     
    for dir_ in Names:
        os.makedirs(dir_,exist_ok=True)
    logging.info("creating dir sucessfully")


def Unique_Filename(filename:str) -> str:

    Timestamp = time.asctime().replace(" ", "_").replace(" ", "_")
    unique_filename = f"{filename}_{Timestamp}"
    logging.info("creating unique filename sucessfully")
    return unique_filename

def log_model_summary(model:keras_model) -> keras_summary:
    with io.StringIO() as stream:
        model.summary(print_fn=lambda x: stream.write(f"{x}\n"))
        summary_str = stream.getvalue()
    return summary_str
