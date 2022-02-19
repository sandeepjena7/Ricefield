
from tensorflow import keras
from typing import List,TypeVar
from pathlib import Path
import logging

keras_model = TypeVar("keras_model")

def  own_model(img_shape:List[int],num_classes:int,model_path:Path) -> keras_model:

    model = keras.Sequential()
    model.add(keras.layers.Conv2D(8,(3,3),padding='same',kernel_initializer=keras.initializers.HeNormal(),activation='relu',input_shape=tuple(img_shape)))
    model.add(keras.layers.Conv2D(8,(3,3),kernel_initializer=keras.initializers.HeNormal(),activation='relu'))
    model.add(keras.layers.MaxPooling2D(pool_size=(2,2),strides=(2,2)))
    model.add(keras.layers.Conv2D(4,(1,1),padding='same',kernel_initializer=keras.initializers.HeNormal(),activation='relu'))
    model.add(keras.layers.Conv2D(16,(3,3),kernel_initializer=keras.initializers.HeNormal(),activation='relu'))
    model.add(keras.layers.Conv2D(4,(1,1),padding='same',kernel_initializer=keras.initializers.HeNormal(),activation='relu'))
    model.add(keras.layers.Conv2D(16,(3,3),kernel_initializer=keras.initializers.HeNormal(),activation='relu'))
    model.add(keras.layers.MaxPooling2D(pool_size=(2,2),strides=(2,2)))
    model.add(keras.layers.Conv2D(4,(1,1),padding='same',kernel_initializer=keras.initializers.HeNormal(),activation='relu'))
    model.add(keras.layers.Conv2D(64,(3,3),kernel_initializer=keras.initializers.HeNormal(),activation='relu'))
    model.add(keras.layers.GlobalAveragePooling2D())
    model.add(keras.layers.Dense(num_classes,activation='softmax'))

    model.save(model_path)
    logging.info(f'our model was save at {model_path}')

    return model


def prepared_model(model:keras_model
        ,learning_rate:float
        ,momentum:float
        ,nesterov:bool
        ,metrics:List[str]) -> keras_model:

    model.compile(optimizer=keras.optimizers.SGD(learning_rate=learning_rate,momentum=momentum,nesterov=nesterov)
                ,metrics=metrics
                ,loss=keras.losses.CategoricalCrossentropy())
    logging.info("Ready to train our own model is compile")
    
    return model

def load_full_model(untrain_model_path:Path) -> keras_model:

    model = keras.models.load_model(untrain_model_path)

    logging.info("Loading model was successful")
    return model

if __name__ == '__main__':
    model = own_model([48,48,3],num_classes=3,model_path=None)
    s = prepared_model(model,learning_rate=0.002,momentum=0.9,nesterov=False,metrics=['accuracy'])