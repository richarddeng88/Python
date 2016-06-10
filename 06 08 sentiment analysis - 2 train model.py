import pyprind
import pandas as pd
import os
import time
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('./movie_data.csv')
print df.head(3)

count = CountVectorizer()