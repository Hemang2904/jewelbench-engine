import streamlit as st
import requests
import trimesh
import tempfile
import os

st.set_page_config(page_title="JewelBench STL Pricing", layout="centered")

def get_live_prices():
    # In a production app, you'd use a real API like GoldAPI.io or Metals-API.
    # For this demo, we use a fallback mock or a scrape-less approach.
    # Note: Kitco requires specific headers/auth for high-freq access.
    return {
        "Gold 24K (g)": 7500.0,  # Example INR prices
        "Gold 22K (g)": 6875.0,
        "Gold 18K (g)": 5625.0,
        "Silver (g)": 95.0,
        "Platinum (g)": 3200.0
    }

st.title("💎 JewelBench STL Live Pricing")

# Sidebar for Metal Pricing
st.sidebar.header("Metal Settings")
prices = get_live_prices()
metal_choice = st.sidebar.selectbox("Select Metal / Purity", list(prices.keys()))
current_price = prices[metal_choice]

st.sidebar.metric(label=f"Live Price ({metal_choice})", value=f"₹{current_price:,.2f}")

# Main Upload Area
st.subheader("1. Upload STL File")
uploaded_file = st.file_uploader("Choose an STL file", type=['stl'])

if uploaded_file is not None:
    # Save to temp file to process with trimesh
    with tempfile.NamedTemporaryFile(delete=False, suffix=".stl") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    try:
        mesh = trimesh.load(tmp_path)
        volume_mm3 = mesh.volume
        
        # Densities (g/cm3)
        densities = {
            "Gold 24K (g)": 19.32,
            "Gold 22K (g)": 17.50,
            "Gold 18K (g)": 15.58,
            "Silver (g)": 10.49,
            "Platinum (g)": 21.45
        }
        
        density = densities.get(metal_choice, 19.32)
        # Weight = Volume (cm3) * Density
        # mm3 to cm3 is / 1000
        weight_g = (volume_mm3 / 1000) * density
        total_value = weight_g * current_price

        st.subheader("2. Calculations")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Volume", f"{volume_mm3:.2f} mm³")
            st.metric("Estimated Weight", f"{weight_g:.3f} g")
        
        with col2:
            st.metric("Metal Value", f"₹{total_value:,.2f}")

        st.info(f"Calculation based on density for {metal_choice}: {density} g/cm³")

    except Exception as e:
        st.error(f"Error processing mesh: {e}")
    finally:
        os.remove(tmp_path)
else:
    st.info("Please upload an STL file to see the estimated weight and live value.")

st.markdown("---")
st.caption("Powered by O.R.I.O.N. for JewelBench.ai")
