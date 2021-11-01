# -*- coding: utf-8 -*- 
import streamlit as st 

st.header("Datasets ") 
st.write("The datasets in the project were sourced from: ") 
st.write("1.	“Open data on COVID-19 in Malaysia” by Malaysian’s Ministry of Health (MOH) (https://github.com/MoH-Malaysia/covid19-public) ") 
st.write("2.	“Open data on Malaysia's National Covid-19 Immunisation Programme” by Malaysian’s Ministry of Health (https://github.com/CITF-Malaysia/citf-public) ") 
st.write("Since both repos are still updating the datasets, the ones being used is retrieved on 31st October 2021. ") 

st.header("1 – Has Vaccination Helped in Reducing the Daily Cases? Which State(s) Have Shown the Effect of Vaccination? ") 
st.write("The datasets used for this question is cases_malaysia.csv, vax_malaysia.csv, and deaths_malaysia.csv. The three datasets were merged. Then, the graphs plot new cases, full vaccinations, and new deaths every day. ") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q1Malaysia.png") 

st.write("Based on the resulted graph, the vaccination helped in reducing the daily cases. The higher the number of full vaccinations performed, the lesser the daily cases. ") 
st.write("Most of the states have obvious affect of vaccinations on the daily cases. For example: ") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q1Johor.png") 
st.write("However, it is not entirely true on Sarawak and W.P. Labuan where at some point there is a spike in cases even though they have received their vaccinations. ") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q1Sarawak.png") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q1Labuan.png") 

st.header("2 – Which State(s) Require Attention Now? ")
st.write("The datasets used for this question is cases_state.csv and icu.csv. Each of the states were separated before merging the results from both datasets. Then, it was plotted on a stacked bar graph which shows daily new cases and daily ICU beds usage for covid in each state for the past 30 days. ")
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q2n9.png") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q2kl.png") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q2labuan.png") 
st.image("https://raw.githubusercontent.com/Heeuul/DMProject/main/q2putrajaya.png") 