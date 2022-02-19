import pytest
import yaml



@pytest.fixture
def config(config_path="config.yaml"):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


@pytest.mark.parametrize("name",
    [
        ("batch_size")
        ,("workers")
        ,("kfolds")
        ,("epochs")

    ]
)
                        
def test_parmstyp(config,name):
    parms = config['params']
    assert isinstance(parms[name],int) ,f"{name} it not type of int"

def test_lrlimit(config):
    lr = config['params']['lr']
    assert lr < 10 , f"lr should be less than {lr}"
