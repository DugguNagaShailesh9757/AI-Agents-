from datetime import datetime

def export_to_txt(content):
    filename = f"travel_itinerary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    return filename
