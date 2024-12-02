import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from cnnClassifier.logger import logger

logger.info("Welcome to my custom log")
