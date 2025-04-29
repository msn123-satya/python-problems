async function getWeather() {
    const city = document.getElementById("cityInput").value.trim();
    const country = document.getElementById("countrySelect").value;
    const apiKey = "9267261566db0cb16a506e977b3b59f4";
  
    if (!city) {
      alert("Please enter a city name");
      return;
    }
  
    const query = `${city},${country}`;
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${query}&appid=${apiKey}&units=metric`;
  
    try {
      const response = await fetch(url);
      const data = await response.json();
  
      if (data.cod === 200) {
        const info = `
          <p><strong>City:</strong> ${data.name}, ${data.sys.country}</p>
          <p><strong>Temperature:</strong> ${data.main.temp} °C</p>
          <p><strong>Humidity:</strong> ${data.main.humidity}%</p>
          <p><strong>Condition:</strong> ${data.weather[0].description}</p>
        `;
        document.getElementById("weatherInfo").innerHTML = info;
      } else {
        document.getElementById("weatherInfo").innerHTML = `<p>City not found.</p>`;
      }
    } catch (error) {
      document.getElementById("weatherInfo").innerHTML = `<p>Error fetching weather data.</p>`;
      console.error("Fetch error:", error);
    }
  }
  