async function getWeather() {
    const city = document.getElementById('city').value;
    const units = document.getElementById('units').value;
    const response = await fetch(`/weather?city=${city}&units=${units}`);
    const data = await response.json();

    const weatherInfo = document.getElementById('weather-info');
    if (data.error) {
        weatherInfo.innerHTML = `<p>${data.error}</p>`;
    } else {
        weatherInfo.innerHTML = `
            <h2>${data.city}</h2>
            <p>Temperature: ${data.temperature}° ${units === 'metric' ? 'C' : 'F'}</p>
            <p>Condition: ${data.description}</p>
            <p>Wind Speed: ${data.wind_speed} ${units === 'metric' ? 'm/s' : 'mph'}</p>
            <img src="http://openweathermap.org/img/wn/${data.icon}@2x.png" alt="Weather icon">
        `;
    }
}
