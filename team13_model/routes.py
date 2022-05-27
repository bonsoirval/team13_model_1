from flask import Flask, render_template, request, url_for
import pickle
import numpy as np
import os
from team13_model import app

file_path = os.getcwd()
filename = "catboost.pkl"
file_path = file_path + f"/team13_model/{filename}"
model = pickle.load(open(file_path, 'rb'))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        timeday = request.form.get('timeday')
        timehour = request.form.get('timehour')
        timeyear = int(request.form['timeyear'])
        timeday_part = request.form.get('timeday_part')
        timeday_of_week = request.form.get('timeday_of_week')
        timeday_of_year = int(request.form["timeday_of_year"])
        timeweekofyear = int(request.form['timeweekofyear'])
        timeis_weekend = request.form.get('timeis_weekend')
        Bilbao_pressure = int(request.form['Bilbao_pressure'])
        Madrid_wind_speed = int(request.form["Madrid_wind_speed"])
        timemonth = request.form.get("timemonth")
        Barcelona_pressure = int(request.form["Barcelona_pressure"])
        Valencia_wind_deg = int(request.form["Valencia_wind_deg"])
        Bilbao_wind_speed = int(request.form["Bilbao_wind_speed"])
        Valencia_wind_speed = int(request.form["Valencia_wind_speed"])
        Bilbao_clouds_all = int(request.form['Bilbao_clouds_all'])
        Valencia_humidity = int(request.form['Valencia_humidity'])
        Seville_pressure = int(request.form['Seville_pressure'])
        Barcelona_temp_min = int(request.form['Barcelona_temp_min'])
        Madrid_temp_min = int(request.form['Madrid_temp_min'])


        data = np.array([[timeday,timehour, timeyear, timeday_part, timeday_of_week, timeday_of_year,
                          timeweekofyear, timeis_weekend, Bilbao_pressure, Madrid_wind_speed, timemonth, Barcelona_pressure,
                          Valencia_wind_deg, Bilbao_wind_speed, Valencia_wind_speed, Bilbao_clouds_all, Valencia_humidity,
                          Seville_pressure, Barcelona_temp_min, Madrid_temp_min]])

        my_prediction = model.predict(data)

        return render_template('results.html', prediction= np.round(my_prediction, 2))
    elif request.method == 'GET': # reload the form as the pserson has not submitted form as required
        return render_template('index.html')
