from torch.utils.data import DataLoader, ConcatDataset
from torchvision import transforms,datasets
from src.utils.common import read_yaml
import torch
import logging
import os
from sklearn.model_selection import KFold
from torch.utils.data import SubsetRandomSampler
from torch.utils.data import DataLoader

data_dir = "D:\\PYthon_project\\Farming\\data\\processed"
input_size =48
data_transforms = {
    'train': transforms.Compose([
        transforms.Resize(input_size),
        transforms.RandomResizedCrop(input_size),
        transforms.RandomRotation(degrees=30),
        transforms.ColorJitter(brightness=0.3, contrast=0.2, saturation=0.1, hue=0.1),
        transforms.ToTensor(),
        # transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'valid': transforms.Compose([
        transforms.Resize(input_size),
        transforms.CenterCrop(input_size),
        transforms.RandomRotation(degrees=30),
        transforms.ColorJitter(brightness=0.3, contrast=0.2, saturation=0.1, hue=0.1),
        transforms.ToTensor(),
        # transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'test': transforms.Compose([
        transforms.Resize(48)
        ,transforms.ToTensor()
    ])

}


image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x), data_transforms[x]) for x in ['train', 'valid','test']}


images_datasets_concat = {"train":ConcatDataset([image_datasets["train"],image_datasets['valid']]),"test":image_datasets["test"]}

k_folds = 3
seed = 7
kfold = KFold(n_splits=k_folds,shuffle=True,random_state=seed)
batch_size = 32


for fold,(train,val) in enumerate(kfold.split(images_datasets_concat['train'])):

    subsampler_dict = { name:SubsetRandomSampler(x) for name,x in zip(['train','val'] ,[train,val])}
    dataloader_dict = {x:DataLoader(images_datasets_concat['train'],batch_size=batch_size,sampler=subsampler_dict[x],num_workers=1)  for x in ['train','val']}
    print(len(dataloader_dict['train'])*batch_size,len(dataloader_dict['val'])*batch_size)