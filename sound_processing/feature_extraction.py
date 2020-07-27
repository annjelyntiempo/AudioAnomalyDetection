# -*- coding: utf-8 -*-
"""feature_extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wpl4nex_ONCaLu3AX6B9spxNBYrO2alD
"""

# Commented out IPython magic to ensure Python compatibility.
import librosa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import os
import sklearn

class FeatureExtractor:
  """
      Extract features such as spectral centroid, spectral rolloff, spectral bandwidth, spectral flatness, rmse, MFCC and chroma feature.

      FeatureExtractor Args:

      sr (int): sampling rate

      Returns:
      array: extracted features
  """

  def __init__(self):
    self.extracted_features = []

  def spectral_centroid(self, data, sr):
    return librosa.feature.spectral_centroid(data=data, sr=sr)

  def spectral_rolloff(self, data, sr):
    return librosa.feature.spectral_rolloff(data=data, sr=sr)

  def spectral_bandwidth(self, data, sr):
    return librosa.feature.spectral_bandwidth(data=data, sr=sr)

  def spectral_flatness(self, data):
    return librosa.feature.spectral_flatness(data=data)

  def rmse(self, data, hop_length):
    return librosa.feature.rmse(data=data, hop_length=hop_length, center=True)

  def mfcss(self, data, sr):
    return librosa.feature.mfcc(data=data, sr=sr)

  def chromas(self, data, sr, hop_length):
    return librosa.feature.chroma_stft(data=data, sr=sr, hop_length=hop_length)

  def features(self, data, sr, hop_length):
    self.extracted_features.append(self.spectral_centroid(data, sr))
    self.extracted_features.append(self.spectral_rolloff(data, sr))
    self.extracted_features.append(self.spectral_bandwidth(data, sr))
    self.extracted_features.append(self.spectral_flatness(data))
    self.extracted_features.append(self.rmse(data, hop_length))
    self.extracted_features.append(self.mfcss(data, sr))
    self.extracted_features.append(self.chromas(data, sr, hop_length))

    return np.asarray(self.extracted_features)