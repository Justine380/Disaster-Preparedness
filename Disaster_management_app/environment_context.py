from .models import EnvironmentalFactors

def get_environmental_factors(request):
    environmental_factors, created = EnvironmentalFactors.objects.get_or_create()
    message = "" 
    prediction = ""
    if environmental_factors.temperature > 30 and environmental_factors.humidity > 80:
        prediction = "Flood"
        message = "Warning: High temperature and humidity levels detected "
    elif environmental_factors.land_surface_temperature > 35 and environmental_factors.streamflow_river_discharge < 10:
        prediction = "Drought"
        message = "Warning: High land surface temperature and low streamflow detected "
    elif environmental_factors.open_flame > 0.5 and environmental_factors.smoke_detectors < 0.5:
        prediction = "Home fire"
        message = "Warning: Open flame detected without smoke detectors.  "
    elif environmental_factors.high_number_of_cases > 1000 and environmental_factors.high_transmission_rate > 0.5:
        prediction = "Pandemic"
        message = "Warning: High number of cases and transmission rate detected.  "

    return {"message": message, "prediction": prediction}
