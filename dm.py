# -*- coding: utf-8 -*- 
import streamlit as st 

st.header("Datasets ") 
st.write("The datasets in the project were sourced from: ") 
st.write("1. “Open data on COVID-19 in Malaysia” by Malaysian’s Ministry of Health (MOH) (https://github.com/MoH-Malaysia/covid19-public) ") 
st.write("2. “Open data on Malaysia's National Covid-19 Immunisation Programme” by Malaysian’s Ministry of Health (https://github.com/CITF-Malaysia/citf-public) ") 
st.write("Since both repos are still updating the datasets, the ones being used is retrieved on 31st October 2021. ") 

st.header("1 – Has Vaccination Helped in Reducing the Daily Cases? Which State(s) Have Shown the Effect of Vaccination? ") 
st.write("The datasets used for this question is cases_malaysia.csv, vax_malaysia.csv, and deaths_malaysia.csv. The three datasets were merged. Then, the graphs plot new cases, full vaccinations, and new deaths every day. ") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q1Malaysia.png") 
st.caption("Malaysia's daily vaccination, new cases, and new deaths over time") 

st.write("Based on the resulted graph, the vaccination helped in reducing the daily cases. The higher the number of full vaccinations performed, the lesser the daily cases. ") 
st.write("Most of the states have obvious affect of vaccinations on the daily cases. For example: ") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q1Johor.png") 
st.caption("Johor's daily vaccination, new cases, and new deaths over time") 
st.write("However, it is not entirely true on Sarawak and W.P. Labuan where at some point there is a spike in cases even though they have received their vaccinations. ") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q1Sarawak.png") 
st.caption("Sarawak's daily vaccination, new cases, and new deaths over time") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q1Labuan.png") 
st.caption("Labuan's daily vaccination, new cases, and new deaths over time") 

st.header("2 – Which State(s) Require Attention Now? ")
st.write("The datasets used for this question is cases_state.csv and icu.csv. Each of the states were separated before merging the results from both datasets. Then, it was plotted on a stacked bar graph which shows daily new cases and daily ICU beds usage for covid in each state for the past 30 days. ")
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q2n9.png") 
st.caption("Negeri Sembilan's daily active cases and covid ICU beds past 30 days") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q2kl.png") 
st.caption("Kuala Lumpur's daily active cases and covid ICU beds past 30 days") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q2labuan.png") 
st.caption("W.P. Labuan's daily active cases and covid ICU beds past 30 days") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q2putrajaya.png") 
st.caption("W.P. Putrajaya's daily active cases and covid ICU beds past 30 days") 
st.write("Based on the stacked bar charts, the states that requires attention now are Negeri Sembilan, W.P. Kuala Lumpur, W.P. Labuan, and W.P. Putrajaya. It is because the daily active cases are either increasing or high in value for the last few days. ") 

st.header("3 – Which Data Modelling Method Best Predicts the Recovery Rate? ") 
st.write("The datasets used in this question is cases_malaysia.csv and vax_malaysia.csv. Both datasets are first merged, and the date is dropped before the next step. Then, feature selection is performed using Boruta on the daily recovered cases. The Boruta scores after removing features under 0.5 are as follows: ") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q3table.png") 
st.caption("Boruta score of daily recovered cases") 

st.write("Next, data modelling was performed with feature selection based on the Boruta scores. Multiple methods are used to compare their accuracy. The methods are regression and classification models of decision trees and random forests. After running each of the methods, following are the accuracy results: ") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q3table2.png") 
st.caption("Accuration score of data models") 
st.write("Based on the results, random forest(regression) works best on predicting the recovery rate of the datasets. ") 

st.header("4 - Is there any correlation on vaccination and daily cases between states? ") 
