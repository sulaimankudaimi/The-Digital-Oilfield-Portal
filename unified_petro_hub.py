import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Eng. Sulaiman | Digital Oilfield Portal", layout="wide")

# تطبيق التعديلات الجمالية بناءً على ملاحظات المهندس سليمان
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@700;800&family=Inter:wght@400;600;700&display=swap');
    
    .main { background-color: #050a0f; }
    
    /* تعديل العنوان الرئيسي - كبير وواضح وبخط Exo 2 */
    .hero-section {
        background: linear-gradient(180deg, rgba(0,242,255,0.05) 0%, rgba(5,10,15,1) 100%);
        padding: 50px 20px;
        text-align: center;
        border-bottom: 2px solid #00f2ff;
        margin-bottom: 40px;
    }
    
    .main-title {
        font-family: 'Exo 2', sans-serif;
        font-size: 5rem; /* حجم ضخم */
        font-weight: 800;
        color: #00f2ff;
        letter-spacing: 2px;
        text-shadow: 0 0 30px rgba(0, 242, 255, 0.4);
        margin: 0;
        text-transform: uppercase;
    }

    /* تكبير حجم خط التبويبات (Tabs) */
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1.5rem !important; /* تكبير الخط */
        font-family: 'Exo 2', sans-serif;
        font-weight: 600;
        padding: 10px 20px;
    }

    /* تعديل اسم الأداة - خط Inter احترافي وجذاب */
    .card-title {
        font-family: 'Inter', sans-serif;
        color: #ffcc00;
        font-size: 1.6rem; /* حجم مريح للعين */
        font-weight: 700;
        margin-bottom: 12px;
        letter-spacing: -0.5px;
    }
    
    .project-card {
        background: rgba(16, 23, 32, 0.6);
        border: 1px solid rgba(0, 242, 255, 0.3);
        border-radius: 12px;
        padding: 30px;
        transition: 0.3s;
        height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .project-card:hover {
        border-color: #ffcc00;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.2);
    }

    .card-desc {
        font-family: 'Inter', sans-serif;
        color: #bdc3c7;
        font-size: 1.05rem;
        line-height: 1.5;
    }

    .launch-btn {
        background: #00f2ff;
        color: #050a0f !important;
        font-weight: 800;
        padding: 12px;
        border-radius: 6px;
        text-align: center;
        text-decoration: none;
        font-family: 'Inter', sans-serif;
        display: block;
        margin-top: 15px;
        font-size: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. الهيدر المحدث
st.markdown("""
    <div class="hero-section">
        <h1 class="main-title">THE DIGITAL OILFIELD COMMAND CENTER</h1>
        <p style="font-family: 'Inter'; font-size: 1.3rem; color: #8b949e; margin-top: 10px;">
            15+ Enterprise-Grade AI Solutions Developed by <b>Eng. Sulaiman Kudaimi</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

# 3. التبويبات بحجم خط مكبر
tabs = st.tabs(["🌍 Subsurface", "🏗️ Drilling & Production", "💎 Digital Twins", "🛡️ HSE & Maintenance"])

# نفس بيانات المشاريع السابقة (لم تتغير)
projects_data = {
    "Subsurface": [
        {"name": "Seismic Facies AI", "url": "https://global-seismic-ai-interpretation.streamlit.app/", "desc": "Automated seismic facies & fault interpretation using Deep Learning."},
        {"name": "Rock & Mineral Expert", "url": "https://smart-lithology-ai-expert-ai.streamlit.app/", "desc": "10,000+ Image dataset for 100% accurate lithology classification."},
        {"name": "Petrophysical Platform", "url": "https://safedrill-ai-pro.streamlit.app/", "desc": "Well-log reconstruction and petrophysical estimation."},
        {"name": "PetroVision AI", "url": "https://petrovision-ai.streamlit.app/", "desc": "A unified platform for geological and visualization AI tools."}
    ],
    "Drilling & Production": [
        {"name": "SafeDrill AI Pro", "url": "https://safedrill-ai-pro.streamlit.app/", "desc": "Predictive advisor for drilling hazards and NPT reduction."},
        {"name": "Production Forecaster", "url": "https://appuction-forecaster-ai.streamlit.app/", "desc": "AI-driven forecasting and DCA models for Volve field."},
        {"name": "Flow Assurance AI", "url": "https://flow-assurance-ai.streamlit.app/", "desc": "Early detection of wax, scale, and hydrate formation."},
        {"name": "PetroEconomic AI", "url": "https://petroeconomic-ai.streamlit.app/", "desc": "Economic advisor for field development and ROI optimization."}
    ],
    "Digital Twins": [
        {"name": "Reservoir Digital Twin", "url": "https://reservoir-digital-twin.streamlit.app/", "desc": "High-fidelity subsurface dynamic simulation twin."},
        {"name": "Production AI Twin", "url": "https://digital-twin-petrol-ai.streamlit.app/", "desc": "Asset-wide performance monitoring and facilities twin."},
        {"name": "EOR Smart Simulator", "url": "https://eor-smart-simulator.streamlit.app/", "desc": "Optimization model for smart water and gas injection."},
        {"name": "Unified PetroVision", "url": "https://petrovision-ai.streamlit.app/", "desc": "Integrating subsurface vision with development metrics."}
    ],
    "HSE & Maintenance": [
        {"name": "AI Anomaly Detector", "url": "https://ai-anomaly-detector.streamlit.app/", "desc": "Predictive maintenance and Root Cause Analysis."},
        {"name": "Acoustic Health AI", "url": "https://industrial-ai-diagnostic-system.streamlit.app/", "desc": "Pump health monitoring via acoustic signatures."},
        {"name": "HSE Safety Twin", "url": "https://hse-twin-ai.streamlit.app/", "desc": "Real-time PPE detection and safety compliance monitor."},
        {"name": "PPE Monitor", "url": "https://ppe-detection-ai.streamlit.app/", "desc": "Computer vision for onsite personnel safety."}
    ]
}

def render_cards(category):
    cols = st.columns(2)
    for idx, project in enumerate(projects_data[category]):
        with cols[idx % 2]:
            st.markdown(f"""
                <div class="project-card">
                    <div>
                        <div class="card-title">{project['name']}</div>
                        <div class="card-desc">{project['desc']}</div>
                    </div>
                    <a href="{project['url']}" target="_blank" class="launch-btn">LAUNCH TOOL 🚀</a>
                </div>
                """, unsafe_allow_html=True)
            st.write("")

with tabs[0]: render_cards("Subsurface")
with tabs[1]: render_cards("Drilling & Production")
with tabs[2]: render_cards("Digital Twins")
with tabs[3]: render_cards("HSE & Maintenance")

st.markdown("<br><p style='text-align: center; color: #5d6d7e;'>Digital Oilfield Portal | Eng. Sulaiman Kudaimi © 2024</p>", unsafe_allow_html=True)
