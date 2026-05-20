import streamlit as st
from streamlit_js_eval import get_geolocation

# 1. Page Configuration & Branding
st.set_page_config(page_title="Reel Fast Fishing App", page_icon="🎣", layout="centered")

st.title("🎣 Reel Fast Fishing App")
st.caption("No trials. No subscriptions. Just fast fishing Intel.")
st.markdown("---")

# 2. Force Location Access
st.subheader("📍 Step 1: Establish Your Location")
st.write("To get instant bait and lure recommendations, we need your current coordinates.")

# Trigger the browser's native location prompt
location = get_geolocation()

if not location:
    st.warning("⚠️ Action Required: Please enable/allow location services in your browser to unlock local tackle recommendations.")
    st.info("Reel Fast requires location data so you don't waste time using the wrong presentation.")
else:
    # Extract Coordinates
    lat = round(location['coords']['latitude'], 4)
    lon = round(location['coords']['longitude'], 4)
    
    st.success(f"✅ Location Locked: {lat}, {lon}")
    
    st.markdown("---")
    st.subheader("🐟 Step 2: Local Tackle & Bait Guide")

    # 3. Location-Based Recommendation Logic (Galveston / Coastal Texas Region)
    if (29.0 <= lat <= 30.0) and (-95.5 <= lon <= -94.5):
        location_name = "Galveston & Coastal Bays"
        target_species = "Redfish, Speckled Trout, Black Drum, Flounder"
        
        lures = [
            "**Soft Plastics:** 3-inch paddle tails (Chicken on a Chain or New Penny colors) on a 1/4 oz jig head.",
            "**Topwater:** Bone-colored or chrome topwater plugs (Heddon Super Spook Jr.) for early morning.",
            "**Spoons:** 1/4 oz gold spoons for grassy flats."
        ]
        
        baits = [
            "**Live Bait:** Live shrimp under a popping cork (highly recommended for Black Drum and Trout).",
            "**Cut Bait:** Fresh cut mullet or menhaden fished on the bottom for big Reds."
        ]
    else:
        # Default fallback for any other location
        location_name = "General Inland / Freshwater"
        target_species = "Largemouth Bass, Catfish, Bluegill"
        
        lures = [
            "**Soft Plastics:** Green Pumpkin Texas-rigged senkos or trick worms.",
            "**Moving Lures:** 3/8 oz white spinnerbaits or square-bill crankbaits."
        ]
        
        baits = [
            "**Live Bait:** Nightcrawlers (earthworms) under a bobber.",
            "**Catfish Bait:** Stink bait, chicken liver, or live minnows."
        ]

    # 4. Display the Intel
    st.metric(label="Current Fishing Ground", value=location_name)
    st.write(f"**Primary Target Species right now:** {target_species}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🪝 Recommended Lures")
        for lure in lures:
            st.markdown(f"* {lure}")
            
    with col2:
        st.markdown("### 🪱 Recommended Bait")
        for bait in baits:
            st.markdown(f"* {bait}")

    st.markdown("---")
    st.info("💡 **Reel Fast Tip:** If you're fishing moving water, cast into the current and let your bait drift naturally past structure.")
