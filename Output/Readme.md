## Final Set of Prompts Used

### System Prompt:
```
Generate a {days}-day itinerary for {destination} from {start_date} to {end_date}:
- Budget Level: {budget}
- Interests: {interests}
- Special Requirements: {special_reqs}

Include:
- Logical grouping of nearby attractions
- Estimated costs in USD where applicable
- Transportation time between locations
- Weather-appropriate clothing suggestions

Format Requirements:
1. Use numbered days (e.g., "Day 1:", not "Day 1:")
2. Each activity on a new line starting with •
3. No random line breaks or spaces between characters
4. Time durations in parentheses after activities
5. Keep all text on single lines (no mid-word breaks)
```

### User Prompt:
```
Generate a detailed {params['duration']}-day itinerary from {params['boarding_point']} to {params['destination']}:

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
```

### Model Response:
The response follows the structured itinerary format including travel details, daily activities, meal recommendations, and return travel arrangements.

---

## Sample Inputs and Outputs

### Sample User Inputs:
```
{
  "duration": 3,
  "boarding_point": "Delhi",
  "destination": "Hyderabad",
  "start_date": "2025-03-29",
  "end_date": "2025-04-01",
  "budget": "mid-range",
  "interests": ["historical sites", "local cuisine", "city exploration"],
  "special_reqs": "vegetarian meals only"
}
```

### Sample Output:
```
🛫 OUTBOUND TRAVEL (Day 0)
• Flight from Delhi (DEL) to Hyderabad (HYD) (Approx. 2 hours)
  - Departure: 2025-03-29, Evening (e.g., 6:00 PM)
  - Arrival: 2025-03-29, Evening (e.g., 8:00 PM)
  - Cost: ₹4,000 - ₹6,000
• Transfer to hotel in Banjara Hills/Jubilee Hills (30 minutes) - ₹500 - ₹800

🏨 DAY 1
• Morning: Visit Charminar (2 hours)
• Lunch: Biryani at Paradise Restaurant (₹500 - ₹700 for two)
• Afternoon: Explore Golconda Fort (3 hours)
• Dinner: Chutneys, Banjara Hills (₹800 - ₹1,200 for two)

🏨 DAY 2
• Morning: Qutb Shahi Tombs (2 hours)
• Lunch: Rayalaseema Ruchulu (₹600 - ₹900 for two)
• Afternoon: Hussain Sagar Lake boat ride (3 hours)
• Evening: Street food at Charminar (₹300 - ₹500 for two)

🏨 DAY 3
• Full day at Ramoji Film City (₹1,000 - ₹1,500 per person)
• Evening: Return to hotel, light dinner (₹500 - ₹700 for two)

🛬 RETURN TRAVEL (Day 3)
• Flight from Hyderabad (HYD) to Delhi (DEL) (Approx. 2 hours)
  - Departure: 2025-04-01, Late Night (11:30 PM)
  - Arrival: 2025-04-02, Early Morning (1:30 AM)
  - Cost: ₹4,000 - ₹6,000
```

---

## Documentation Process

### Step 1: Input Validation
- Used `validate_dates(start_date_str, end_date_str)` from `utils.py` to ensure valid date ranges.

### Step 2: Prompt Execution
- `generate_itinerary(params)` constructs the final travel prompt dynamically using user inputs.
- The `model.generate_content()` function generates structured output.

### Step 3: Formatting
- `format_itinerary(text)` refines the raw response, ensuring consistency in bullet points, headers, and emoji usage.

### Step 4: Output Delivery
- The final itinerary is formatted and displayed to the user in a structured, readable manner.

