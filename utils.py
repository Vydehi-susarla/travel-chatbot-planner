# utils.py
def build_advanced_prompt(budget, duration, season, location, trip_type, filters):
    filters_str = ', '.join(filters)
    return f"""
    I am planning a {trip_type} trip.

    Details:
    - Budget: ₹{budget}
    - Duration: {duration}
    - Season: {season}
    - Location: {location}
    - Filters: {filters_str}

    Please suggest:
    1. 2-3 suitable destinations with short reasons
    2. Estimated total trip cost for each
    3. A day-by-day itinerary with local food, activities, and cultural experiences
    4. Any visa or safety advice for Indian travelers

    Format it cleanly and clearly.
    """
