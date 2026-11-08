
import customtkinter as ctk
import requests

app = ctk.CTk()
app.title("City Information Finder")
app.geometry("600x500")


def get_city_info():
    city = city_entry.get()

    response = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={
            "name": city,
            "count": 1,
            "language": "en"
        }
    )

    print(response.status_code)

    data = response.json()

    if "results" not in data:
        result_label.configure(text="City not found!")
        return

    city_data = data["results"][0]

    population = city_data.get("population", "Unknown")
    longitude = city_data.get("longitude", "Unknown")
    latitude = city_data.get("latitude", "Unknown")

    result_label.configure(
        text=f"Population: {population}\n"
             f"Longitude: {longitude}\n"
             f"Latitude: {latitude}"
    )


city_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter a city",
    font=("Arial", 14)
)
city_entry.pack(padx=10, pady=10)

search_button = ctk.CTkButton(
    app,
    text="Search",
    font=("Arial", 14),
    command=get_city_info
)
search_button.pack(padx=10, pady=20)

result_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 14)
)
result_label.pack(padx=10, pady=30)


app.mainloop()
