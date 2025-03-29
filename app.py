from datetime import datetime, timedelta
import google.generativeai as genai
import streamlit as st


# ===== SECURE CONFIGURATION =====
def initialize_gemini():
    """Safe API initialization with error handling"""
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("""
        🔒 API key missing. Please:
        1. Create `.streamlit/secrets.toml` locally
        2. Add to Streamlit Cloud secrets
        """)
        st.code("""
        # secrets.toml format
        GEMINI_API_KEY = "your_key_here"
        """)
        st.stop()
    
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        return genai.GenerativeModel('gemini-1.5-pro-latest')
    except Exception as e:
        st.error(f"🔐 Authentication failed: {str(e)}")
        st.stop()

# Initialize model safely
model = initialize_gemini()



def validate_dates(start_date_str, end_date_str):
    """Calculate trip duration including travel days"""
    try:
        start = datetime.strptime(start_date_str, "%Y-%m-%d")
        end = datetime.strptime(end_date_str, "%Y-%m-%d")
        return (end - start).days + 1  # +1 to include both start and end dates
    except ValueError:
        return 0

def generate_itinerary(params):
    """Generate complete itinerary with travel logistics"""
    try:
        prompt = f"""
        Create a comprehensive travel plan from {params['boarding_point']} to {params['destination']} 
        from {params['start_date']} to {params['end_date']} ({params['duration']} days total).
        
        Traveler Profile:
        - Budget: {params['budget']}
        - Interests: {', '.join(params['interests'])}
        - Special Needs: {params.get('special_reqs', 'None')}
        
        Required Sections:
        
        1. 🛫 OUTBOUND TRAVEL (Day 0)
        • Recommended transportation (flight/train) with:
          - Departure time from {params['boarding_point']}
          - Arrival time at destination
          - Duration and cost estimate
        • Transfer to accommodation details
        
        2. 🏨 DAILY ITINERARY (Day 1 to Day {params['duration']-2})
        For each day include:
        • Morning/Afternoon/Evening activities
        • Travel time between locations
        • Meal suggestions with price indicators ({params['budget']} level)
        • Recommended hotels/areas to stay
        
        3. 🛬 RETURN TRAVEL (Day {params['duration']-1})
        • Recommended return options with:
          - Check-out time
          - Departure time from destination
          - Arrival time back to {params['boarding_point']}
        
        Formatting Rules:
        - Use exact headers: 🛫 OUTBOUND TRAVEL, 🏨 DAY X, 🛬 RETURN TRAVEL
        - Each activity starts with •
        - Include duration in parentheses after each activity
        - List costs where applicable
        - No line breaks within activity descriptions
        """

        response = model.generate_content(
            contents={"parts": [{"text": prompt}]},
            generation_config={
                "temperature": 0.2,  # More structured output
                "top_p": 0.7,
                "max_output_tokens": 3000
            }
        )
        
        return format_itinerary(response.text)
    
    except Exception as e:
        return f"⚠️ Error generating itinerary: {str(e)}"

def format_itinerary(text):
    """Apply consistent formatting to the itinerary"""
    # Standardize section headers
    replacements = [
        ("OUTBOUND TRAVEL", "🛫 OUTBOUND TRAVEL"),
        ("RETURN TRAVEL", "🛬 RETURN TRAVEL"),
        ("DAY", "🏨 DAY"),
        ("•", "\n• "),  # Ensure proper bullet spacing
        ("  ", " "),    # Remove double spaces
        ("\n\n", "\n")  # Remove extra line breaks
    ]
    
    for old, new in replacements:
        text = text.replace(old, new)
    
    return text

def main():
    st.set_page_config(page_title="🌍 Complete Travel Planner", layout="wide")
    
    # Initialize session state
    if 'params' not in st.session_state:
        st.session_state.params = {}
        st.session_state.show_itinerary = False
    
    st.title("✈️ Complete Travel Planner")
    st.subheader("Plan your trip from departure to return")
    
    with st.form("travel_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.session_state.params['boarding_point'] = st.text_input("Departure City", key="departure")
            st.session_state.params['destination'] = st.text_input("Destination City", key="destination")
            st.session_state.params['budget'] = st.selectbox(
                "Budget Level",
                ["Budget", "Mid-range", "Luxury"],
                key="budget"
            )
            
        with col2:
            st.session_state.params['start_date'] = st.date_input("Start Date", key="start_date").strftime("%Y-%m-%d")
            st.session_state.params['end_date'] = st.date_input("End Date", key="end_date").strftime("%Y-%m-%d")
            st.session_state.params['interests'] = st.multiselect(
                "Interests",
                ["History", "Nature", "Food", "Adventure", "Art", "Shopping", "Relaxation"],
                key="interests"
            )
        
        st.session_state.params['special_reqs'] = st.text_area(
            "Special Requirements (dietary, mobility, etc.)",
            key="special_reqs"
        )
        
        if st.form_submit_button("Generate Complete Itinerary"):
            days = validate_dates(
                st.session_state.params['start_date'],
                st.session_state.params['end_date']
            )
            if days >= 2:  # Minimum 1 day at destination + travel days
                st.session_state.params['duration'] = days
                st.session_state.show_itinerary = True
            else:
                st.error("Please select at least 2 days for a valid trip")
                st.session_state.show_itinerary = False
    
    if st.session_state.show_itinerary:
        st.divider()
        st.header("Your Personalized Travel Plan")
        
        with st.spinner("Creating your perfect itinerary..."):
            itinerary = generate_itinerary(st.session_state.params)
            st.markdown(itinerary)
            
        st.download_button(
            "Download Itinerary",
            itinerary,
            file_name=f"{st.session_state.params['destination']}_itinerary.txt"
        )

if __name__ == "__main__":
    main()