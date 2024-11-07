
import os

from numerapi import NumerAPI
from src.util.constants import PATH_RAW_TRAIN_SET, PATH_RAW_VALIDATE_SET

numerAPI = NumerAPI()
if os.path.exists(PATH_RAW_TRAIN_SET):
    os.remove(PATH_RAW_TRAIN_SET)
if os.path.exists(PATH_RAW_VALIDATE_SET):
    os.remove(PATH_RAW_VALIDATE_SET)

numerAPI.download_dataset("v5.0/train.parquet", PATH_RAW_TRAIN_SET)
numerAPI.download_dataset("v5.0/validation.parquet", PATH_RAW_VALIDATE_SET)
