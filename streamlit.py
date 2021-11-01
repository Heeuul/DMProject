# -*- coding: utf-8 -*- 
from datetime import date, timedelta 
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
import numpy as np 
import datetime 
import streamlit as st 

from sklearn import preprocessing 
from sklearn.cluster import KMeans 
from sklearn.cluster import DBSCAN 
import scipy.cluster.hierarchy as shc 
from sklearn.feature_selection import SelectKBest 
from sklearn.feature_selection import chi2 
from sklearn.model_selection import train_test_split 

from sklearn.tree import DecisionTreeRegressor 
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import accuracy_score 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier 

st.header("Datasets") 
st.text("The datasets in the project were sourced from: ") 
st.text("1.	“Open data on COVID-19 in Malaysia” by Malaysian’s Ministry of Health (MOH) (https://github.com/MoH-Malaysia/covid19-public)") 
st.text("2.	“Open data on Malaysia's National Covid-19 Immunisation Programme” by Malaysian’s Ministry of Health (https://github.com/CITF-Malaysia/citf-public)") 
st.text("Since both repos are still updating the datasets, the ones being used is retrieved on 31st October 2021.") 