
from src.utils.allutills import Read_Yaml,Create_Dir
from src.utils.callbacks import get_callbacks
from src.utils.models import load_full_model,get_unique_model_path
from src.utils.datamangement import train_valid_genrator
import argparse
import  os
from pathlib import Path

import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

def train_model(config_path:Path,parmas_path:Path) -> None:
    config = Read_Yaml(config_path) 
    params = Read_Yaml(parmas_path)
    artifact = config['artifacts'] 
    artifatcs_dir = artifact['Artifatcs_dir']
    train_model_dir = os.path.join(artifatcs_dir,artifact['Train_mode_dir'])

    Create_Dir([train_model_dir])
    callback_dir = os.path.join(artifatcs_dir,artifact['Callback_dir'])

    untrained_based_model_path = os.path.join(artifatcs_dir
                                ,artifact['Based_model_dir']
                                ,artifact['Updated_model_path'])

    model = load_full_model(untrained_based_model_path)
    callback = get_callbacks(callback_dir)

    train_gen,valid_gen = train_valid_genrator(
                            data_dir=config['data_source']['Process_data_dir']
                            ,img_size=tuple(params['img_shape'][:-1])
                            ,batch_size=params['batch_size']
                            ,do_data_agumentaion=params['augmentation']
                            )

    step_per_train = train_gen.samples // train_gen.batch_size
    step_per_valid = valid_gen.samples // valid_gen.batch_size
    
    logging.info("model was start to train ")
    model.fit(train_gen
            , epochs=params['epochs']
            ,validation_data=valid_gen
            ,steps_per_epoch=step_per_train
            ,validation_steps=step_per_valid
            ,callbacks=callback)
    
    logging.info("model was trained successful")
    
    model_save_file_path = get_unique_model_path(train_model_dir)
    model.save(model_save_file_path)
    logging.info(f"model was saved at {model_save_file_path}")

if __name__ == '__main__':
    args = argparse.ArgumentParser(description='get the data from bucket')
    args.add_argument('--config','-c',default='config/config.yaml')
    args.add_argument('--params','-p',default='params.yaml')

    parsed_args = args.parse_args()

    try:
        logging.info("stage six started >>>>>>>>>>>")
        train_model(config_path=parsed_args.config,parmas_path=parsed_args.params)
        logging.info("stage six model was trained................\n")
    except Exception as e: 
        logging.info(f"Error was occurred {e}\n\n")


