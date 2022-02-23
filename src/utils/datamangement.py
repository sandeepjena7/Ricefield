from pathlib import Path
from typing import Tuple
from tensorflow import  keras 
import logging
import os
from typing import Generator

def train_valid_genrator(data_dir:Path
                        ,img_size:Tuple[int,int]
                        ,batch_size:int
                        ,do_data_agumentaion:bool) -> Generator:


    datagenarator_kwargs = dict(
        rescale=1./255
    )
    dataflow_kwargs = dict(
        target_size=img_size
        ,batch_size=batch_size
        ,shuffle=True
    )
    valid_datagenartor = keras.preprocessing.image.ImageDataGenerator(**datagenarator_kwargs)

    if do_data_agumentaion:
        train_datagenartor = keras.preprocessing.image.ImageDataGenerator(shear_range=0.2
        ,rotation_range=30
        ,zoom_range=0.5
        ,**datagenarator_kwargs)
        logging.info("agumentation we used")
    else:
        train_datagenartor = valid_datagenartor
        logging.info('agumentation dont used')

    train_generator = train_datagenartor.flow_from_directory(
        directory=os.path.join(data_dir,'train')
        ,**dataflow_kwargs
    )
    valid_generator = valid_datagenartor.flow_from_directory(
        directory=os.path.join(data_dir,'val')
        ,**dataflow_kwargs
    )

    logging.info('train and valid generator was created')

    return train_generator,valid_generator
    




    