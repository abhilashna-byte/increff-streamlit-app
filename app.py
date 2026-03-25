import streamlit as st
import base64
import os

# --- Page Config ---
st.set_page_config(
    page_title="Increff USP Automation",
    layout="wide"
)

# --- Function: Convert image to base64 ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

# --- Function: Render Logo ---
def set_high_qual_logo(path, height="60px"):
    bin_str = get_base64_of_bin_file(path)
    if bin_str:
        return f'''
        <img src="data:image/png;base64,{bin_str}" 
             style="
                height:{height};
                width:auto;
                object-fit:contain;
                margin:5px;
             ">
        '''
    return ""

# --- Header Section (Improved UI) ---
current_dir = os.path.dirname(__file__)
path_increff = os.path.join(current_dir, "logo.png")
path_levis = os.path.join(current_dir, "logo2.png")

st.markdown(f"""
    <div style="
        display:flex;
        align-items:center;
        justify-content:space-between;
        padding: 15px 30px;
        background-color: #ffffff;
        border-bottom: 2px solid #f0f0f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border-radius: 10px;
        margin-bottom: 20px;
    ">

        <!-- Left Logo -->
        <div style="flex:1; display:flex; align-items:center;">
            {set_high_qual_logo(path_increff, "110px")}
        </div>

        <!-- Title -->
        <div style="flex:2; text-align:center;">
            <h1 style="
                margin:0;
                font-size:42px;
                font-weight:800;
                color:#d32f2f;
                letter-spacing: -1px;
            ">
                Increff USP Automation
            </h1>
        </div>

        <!-- Right Logo -->
        <div style="flex:1; display:flex; justify-content:flex-end; align-items:center;">
            {set_high_qual_logo(path_levis, "110px")}
        </div>

    </div>
""", unsafe_allow_html=True)

# --- Navigation Tabs ---
tabs = st.tabs([
    "👑 Master",
    "📊 Inventory management",
    "🚀 Order Fulfilment",
    "📦 Order Manager",
    "🔴 Order Cancellation",
    "🔁 Returns",
    "🧾 Logs"
])

# --- MASTER TAB ---
with tabs[0]:

    st.markdown("### ➕ Create Articles | 📦 Create MP Listing | 📦 Create EFS Listing")

    st.markdown("---")

    st.markdown("## Create New Article Master")

    sku = st.text_input("Enter Client SKU ID", placeholder="e.g. LEVI11")

    if st.button("🚀 Create Article"):
        if sku:
            st.success(f"Article '{sku}' created successfully!")
        else:
            st.warning("Please enter SKU ID")

# --- Other Tabs Placeholder ---
for i in range(1, len(tabs)):
    with tabs[i]:
        st.info("This section is under development 🚧")
