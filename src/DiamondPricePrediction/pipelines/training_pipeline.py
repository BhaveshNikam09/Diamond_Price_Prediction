from src.DiamondPricePrediction.components.data_ingestion import data_ingestion

import os
import sys
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import custom_exception
import pandas as pd 

obj=data_ingestion()

obj.intiate_data_ingestion()