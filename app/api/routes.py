from app import app
from flask import request
from app.services import hvac_statistics

@app.route('/')
@app.route('/statistics_calculator', methods=['POST'])
def statistics_calculator():
    data = request.get_data()
    hvac_statistics_calculated = hvac_statistics.statistics_calculation(data)
    return hvac_statistics_calculated