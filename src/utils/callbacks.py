
from pathlib import Path
from src.utils.allutills import Unique_Filename
from tensorflow import keras
import os 
import joblib
import logging
from typing import TypeVar,List

keras_calbacks = TypeVar("keras_calbacks")

def create_and_save_tesnoboard_callbacks(callback_dir:Path,tensoboard_log_dir:Path) -> None:
    
    unique_filename = Unique_Filename('tenbor_logs')
    running_logs = os.path.join(tensoboard_log_dir,unique_filename)

    tensoboard_callbacks = keras.callbacks.TensorBoard(log_dir=running_logs)
    tb_callback_path = os.path.join(callback_dir,'tensoboard_cb.cb')

    joblib.dump(tensoboard_callbacks,tb_callback_path)
    logging.info(f'tensoboard call back is complete and save at {tb_callback_path}')


def create_and_save_checkpint_callbacks(callback_dir:Path,checkpoint_dir:Path):
    
    checkpint_file = os.path.join(checkpoint_dir,'ckpt_model.h5')
    checkpoint_callback = keras.callbacks.ModelCheckpoint(filepath=checkpint_file
                                                ,monitor='val_accuracy'
                                                ,save_best_only=True
                                                )

                        
    ckpt_callback_path = os.path.join(callback_dir,'checkpoint_cb.cb')

    joblib.dump(checkpoint_callback,ckpt_callback_path)
    logging.info(f'tensoboard call back is complete and save at {ckpt_callback_path}')


def get_callbacks(callback_dir:Path) -> List[keras_calbacks]:
    
    callbacks_path = [
        os.path.join(callback_dir,bin_files) for bin_files in os.listdir(callback_dir)
    ]

    callbacks = [
        joblib.load(path) for path in callbacks_path
    ]

    return callbacks