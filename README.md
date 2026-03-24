# 🌦️ Weather App (Python CLI) - BM804

A simple and interactive Command-Line Weather Application built using Python. It fetches real-time weather data such as temperature, humidity, and wind speed using the Open-Meteo API. This project is beginner-friendly and demonstrates API integration without requiring any API key.

---

## 🚀 Features

- 🌍 Fetch real-time weather data  
- 🌡️ Temperature display (°C)  
- 💧 Humidity information  
- 🌬️ Wind speed details  
- ⚡ Fast and lightweight CLI tool  
- 🔓 No API key required  

---

## 🛠️ Tech Stack

- Python  
- requests module  
- Open-Meteo API  

---

## 🔑 API Information

### ✅ No API Key Needed
This project uses the Open-Meteo API, which is:
- Completely free  
- No authentication required  
- No signup needed  

API used in this project:
https://api.open-meteo.com/v1/forecast?latitude=22.5626&longitude=88.363&hourly=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m&timezone=auto

---

### 🔐 API Key Based Alternatives (Optional)

If you want to use APIs that require API keys:

- OpenWeatherMap → https://openweathermap.org/api  
- WeatherAPI → https://www.weatherapi.com  

👉 These require signup and API key generation.

---

## 📂 Project Structure

weather.py   # Main application file  

---

## ▶️ How to Run

1. Install Python  
2. Install required module:
   pip install requests  
3. Run the program:
   python weather.py  

---

## 💡 Example Output

🌦️ WEATHER APP (BM804)

📍 Location: Kolkata  
🌡️ Temperature: 30°C  
💧 Humidity: 70%  
🌬️ Wind Speed: 10 km/h  

---

## 🎯 Learning Outcomes

- API integration  
- JSON data handling  
- Error handling  
- CLI-based application development  

---

## 🖼️ Visual Preview

+----------------------------+  
|   🌦️ WEATHER APP (BM804)   |  
+----------------------------+  
| 📍 Kolkata                |  
| 🌡️ Temp: 30°C            |  
| 💧 Humidity: 70%         |  
| 🌬️ Wind: 10 km/h        |  
+----------------------------+  

---

## 🔮 Future Improvements

- 🌆 Add city input (dynamic location)  
- 📅 7-day forecast  
- 🖥️ GUI version (Tkinter)  
- 📍 Auto-detect location  

---

## 🤝 Contributing

Feel free to fork and improve this project 🚀

---

## 📜 License

This project is open-source and free to use.
