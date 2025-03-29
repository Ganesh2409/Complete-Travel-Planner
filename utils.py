from datetime import datetime, timedelta
import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.5-pro-latest')

def validate_dates(start_date_str, end_date_str):
    try:
        start = datetime.strptime(start_date_str, "%Y-%m-%d")
        end = datetime.strptime(end_date_str, "%Y-%m-%d")
        return (end - start).days + 1
    except ValueError:
        return 0

def generate_itinerary(params):
    try:
        prompt = f"""Generate a detailed {params['duration']}-day itinerary from {params['boarding_point']} to {params['destination']}:
        
        Travel Details:
        - Boarding From: {params['boarding_point']}
        - Destination: {params['destination']}
        - Travel Dates: {params['start_date']} to {params['end_date']}
        - Budget: {params['budget']}
        - Interests: {', '.join(params['interests'])}
        - Special Requirements: {params.get('special_reqs', 'None')}

        Include these specific elements:
        1. OUTBOUND JOURNEY:
           • Recommended flights/trains with approximate duration
           • Best time to depart from {params['boarding_point']}
           • Estimated arrival time at destination

        2. DAILY ITINERARY (Day 1 to Day {params['duration']-1}):
           • Morning/Afternoon/Evening activities with durations
           • Travel time between locations
           • Meal suggestions with price ranges
           • Hotel recommendations

        3. RETURN JOURNEY:
           • Best return options with travel duration
           • Recommended departure time from destination

        Sample Format:
        
        OUTBOUND JOURNEY (Day 0):
        • 6:00 PM: Depart from {params['boarding_point']} via Flight XYZ123 (Duration: 2h 15m)
        • 8:15 PM: Arrive at {params['destination']} Airport
        • 9:00 PM: Transfer to hotel (30m taxi)
        
        Day 1: City Exploration
        • 9-11 AM: Guided city tour (Meet at Central Square)
        • 12-1 PM: Lunch at Seaside Cafe ($$, local cuisine)
        • 2-5 PM: Museum visit (3h with audio guide)
        
        RETURN JOURNEY (Day {params['duration']}):
        • 4:00 PM: Check out from hotel
        • 5:30 PM: Flight ABC456 back to {params['boarding_point']} (2h)
        • 7:30 PM: Arrive home"""

        response = model.generate_content(
            contents={"parts": [{"text": prompt}]},
            generation_config={
                "temperature": 0.3,
                "top_p": 0.8,
                "max_output_tokens": 2500
            }
        )
        
        return format_itinerary(response.text)
    
    except Exception as e:
        return f"Error: {str(e)}"

def format_itinerary(text):
    """Enhanced formatting with travel days"""
    replacements = [
        ("OUTBOUND JOURNEY", "\n✈️ OUTBOUND JOURNEY"),
        ("RETURN JOURNEY", "\n✈️ RETURN JOURNEY"),
        ("•", "\n•"),
        ("Day 1 :", "Day 1:"),
        ("Day 0:", "🛫 TRAVEL DAY:")
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text