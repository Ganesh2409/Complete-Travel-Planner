# prompts.py
ITINERARY_PROMPT = """
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

Example Output:
Day 1: Arrival & Exploration
• 9AM: Check into hotel (2 hours)
• 12PM: Lunch at Le Restaurant (French cuisine)
• 2PM: Walking tour (3 hours)
• 7PM: Dinner (1.5 hours)

"""

REFINEMENT_PROMPT = """
Based on these user inputs:
{dict_str}

Generate ONLY ONE clarifying question about the most important missing detail from:
1. Dietary restrictions
2. Mobility needs
3. Accommodation type preference
4. Special interests not yet mentioned
"""