from app import app
from flask import request
from app.services import hvac_statistics

@app.route('/')
@app.route('/calculate_ventilation_demand', methods=['POST'])
def calculate_ventilation_demand():
    data = request.get_data()
    ventilation_demand_as_json = hvac_statistics.statistics_calculator(data)
    return ventilation_demand_as_json