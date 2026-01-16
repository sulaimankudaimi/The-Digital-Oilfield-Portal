import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Eng. Sulaiman | Digital Oilfield Portal", layout="wide")

# تطبيق لغة التصميم (الأسود الملكي + النصوص المضيئة)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@700;800&family=Inter:wght@400;600;700&display=swap');
    
    /* الخلفية بالأسود الصافي */
    .main { 
        background-color: #ff0000; 
    }
    
    .stApp {
        background-color: #ffffff;
    }

    /* هيدر نيون مشع على خلفية سوداء */
    .hero-section {
        padding: 60px 20px;
        text-align: center;
        background-color: #000000;
        border-bottom: 1px solid #00f2ff;
        margin-bottom: 50px;
    }
    
    .main-title {
        font-family: 'Exo 2', sans-serif;
        font-size: 4.5rem;
        font-weight: 800;
        color: #00f2ff; /* نيون سيان */
        letter-spacing: 3px;
        text-shadow: 0 0 20px #00f2ff;
        margin: 0;
        text-transform: uppercase;
    }

    /* التبويبات بنصوص فاتحة جداً */
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1.4rem !important;
        font-family: 'Exo 2', sans-serif;
        font-weight: 600;
        color: #ffffff !important; /* أبيض ناصع */
        background-color: transparent;
    }

    /* البطاقات بالأسود الصافي مع حدود نيون */
    .project-card {
        background-color: #0a0a0a; /* أسود ملكي */
        border: 1px solid #1a1a1a;
        border-left: 5px solid #00f2ff; /* لمسة نيون جانبية */
        border-radius: 10px;
        padding: 35px;
        transition: 0.4s ease;
        height: 320px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .project-card:hover {
        border-color: #00f2ff;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.2);
        background-color: #111111;
    }

    /* نصوص فاتحة جداً للقراءة */
    .card-title {
        font-family: 'Inter', sans-serif;
        color: #00f2ff; /* عناوين نيون سيان */
        font-size: 1.7rem;
        font-weight: 700;
        margin-bottom: 15px;
    }
    
    .card-desc {
        font-family: 'Inter', sans-serif;
        color: #e0e0e0; /* رمادي فاتح جداً يقترب من الأبيض */
        font-size: 1.1rem;
        line-height: 1.6;
    }

    /* زر الإطلاق الفاتح والمميز */
    .launch-btn {
        background-color: #ffffff; /* أبيض ناصع */
        color: #000000 !important; /* نص أسود للتباين */
        font-weight: 800;
        padding: 14px;
        border-radius: 4px;
        text-align: center;
        text-decoration: none;
        font-family: 'Inter', sans-serif;
        display: block;
        margin-top: 20px;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .launch-btn:hover {
        background-color: #00f2ff;
        box-shadow: 0 0 15px #00f2ff;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. الهيدر (Master Header)
st.markdown("""
    <div class="hero-section">
        <h1 class="main-title">THE DIGITAL OILFIELD PORTAL</h1>
        <p style="font-family: 'Inter'; font-size: 1.4rem; color: #ffffff; margin-top: 15px; font-weight: 300; letter-spacing: 1px;">
            Unified AI Command Center • <b>Eng. Sulaiman Kudaimi</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

# 3. التبويبات (Tabs)
tabs = st.tabs(["🌍 SUBSURFACE", "🏗️ DRILLING & PRODUCTION", "💎 DIGITAL TWINS", "🛡️ HSE & MAINTENANCE"])

# بيانات المشاريع
projects_data = {
    "Subsurface": [
        {"name": "Seismic Facies AI", "url": "https://global-seismic-ai-interpretation.streamlit.app/", "desc": "Deep Learning interpretation for automated seismic facies & fault classification."},
        {"name": "Rock & Mineral Expert", "url": "https://smart-lithology-ai-expert-ai.streamlit.app/", "desc": "Computer Vision for 100% accurate lithology identification from drill cuttings."},
        {"name": "Petrophysical Platform", "url": "https://safedrill-ai-pro.streamlit.app/", "desc": "Predictive well-log reconstruction and digital petrophysical evaluation."},
        {"name": "PetroVision AI", "url": "https://petrovision-ai.streamlit.app/", "desc": "High-end visualization platform for multi-modal geological data."}
    ],
    "Drilling & Production": [
        {"name": "SafeDrill AI Pro", "url": "https://safedrill-ai-pro.streamlit.app/", "desc": "Operational safety advisor for NPT reduction and hazard prediction."},
        {"name": "Production Forecaster", "url": "https://appuction-forecaster-ai.streamlit.app/", "desc": "Time-series forecasting and Decline Curve Analysis (DCA) for field assets."},
        {"name": "Flow Assurance AI", "url": "https://flow-assurance-ai.streamlit.app/", "desc": "Early warning system for wax, scale, and hydrate buildup in pipelines."},
        {"name": "PetroEconomic AI", "url": "https://petroeconomic-ai.streamlit.app/", "desc": "Smart economic simulator for NPV and field development optimization."}
    ],
    "Digital Twins": [
        {"name": "Reservoir Digital Twin", "url": "https://reservoir-digital-twin.streamlit.app/", "desc": "Real-time dynamic simulation twin for subsurface reservoir monitoring."},
        {"name": "Production AI Twin", "url": "https://digital-twin-petrol-ai.streamlit.app/", "desc": "End-to-end performance twin for surface production facilities."},
        {"name": "EOR Smart Simulator", "url": "https://eor-smart-simulator.streamlit.app/", "desc": "Intelligent recovery optimization for Water & Gas injection schemes."},
        {"name": "Unified PetroVision", "url": "https://petrovision-ai.streamlit.app/", "desc": "Integrated subsurface-surface visual analytics dashboard."}
    ],
    "HSE & Maintenance": [
        {"name": "AI Anomaly Detector", "url": "https://ai-anomaly-detector.streamlit.app/", "desc": "Root Cause Analysis (RCA) and predictive maintenance using sensor data."},
        {"name": "Acoustic Health AI", "url": "https://industrial-ai-diagnostic-system.streamlit.app/", "desc": "Pump diagnostics via acoustic fingerprinting and noise analysis."},
        {"name": "HSE Safety Twin", "url": "https://hse-twin-ai.streamlit.app/", "desc": "AI Video Analytics for onsite PPE compliance and personnel safety."},
        {"name": "PPE Monitor", "url": "https://ppe-detection-ai.streamlit.app/", "desc": "Real-time safety equipment detection and risk alerts."}
    ]
}

def render_cards(category):
    cols = st.columns(2)
    for idx, project in enumerate(projects_data[category]):
        with cols[idx % 2]:
            st.markdown(f"""
                <div class="project-card">
                    <div>
                        <div class="card-title">● {project['name']}</div>
                        <div class="card-desc">{project['desc']}</div>
                    </div>
                    <a href="{project['url']}" target="_blank" class="launch-btn">LAUNCH APPLICATION</a>
                </div>
                """, unsafe_allow_html=True)
            st.write("")

with tabs[0]: render_cards("Subsurface")
with tabs[1]: render_cards("Drilling & Production")
with tabs[2]: render_cards("Digital Twins")
with tabs[3]: render_cards("HSE & Maintenance")

st.markdown("<br><p style='text-align: center; color: #444444; font-family: Inter;'>Enterprise AI Hub | <b>Eng. Sulaiman Kudaimi</b> © 2024</p>", unsafe_allow_html=True)
