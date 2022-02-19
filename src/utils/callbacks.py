
from pathlib import Path
from src.utils.allutills import Unique_Filename
from tensorflow import keras
import os 
import joblib
import logging

def create_and_save_tesnoboard_callbacks(callback_dir:Path,tensoboard_log_dir:Path) -> None:
    
    unique_filename = Unique_Filename('tenbor_logs')
    running_logs = os.path.join(tensoboard_log_dir,unique_filename)

    tensoboard_callbacks = keras.callbacks.TensorBoard(log_dir=running_logs)
    tb_callback_path = os.path.join(callback_dir,'tensoboard_cb.cb')

    joblib.dump(tensoboard_callbacks,tb_callback_path)
    logging.info(f'tensoboard call back is complete and save at {tb_callback_path}')


def create_and_save_checkpint_callbacks(callback_dir:Path,checkpint_dir:Path):
    pass