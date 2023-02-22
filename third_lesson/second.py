import weather

forecast = weather.forecast("Lviv")
print(forecast.today["20:00"].temp)
