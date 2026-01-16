import streamlit as st
import time

# 1. إعدادات الصفحة والهوية البصرية (Orbitron & Inter Style)
st.set_page_config(page_title="Eng. Sulaiman | Unified AI Hub", layout="wide", initial_sidebar_state="expanded")

# تطبيق لغة التصميم (CSS) بناءً على توصيات خبير الـ UX
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    .main { background-color: #050a0f; color: white; }
    
    /* هيدر سينمائي */
    .hero-section {
        background: linear-gradient(135deg, #0a192f 0%, #001220 100%);
        padding: 60px;
        border-radius: 20px;
        border-bottom: 3px solid #00f2ff;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(0, 242, 255, 0.1);
    }
    
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #00f2ff;
        text-shadow: 0 0 20px rgba(0, 242, 255, 0.5);
        margin-bottom: 10px;
    }
    
    /* تصميم البطاقات Glassmorphism */
    .project-card {
        background: rgba(16, 23, 32, 0.8);
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 15px;
        padding: 25px;
        transition: all 0.4s ease;
        height: 280px;
        backdrop-filter: blur(10px);
    }
    
    .project-card:hover {
        border-color: #ffcc00;
        box-shadow: 0 0 25px rgba(255, 204, 0, 0.3);
        transform: translateY(-10px);
    }
    
    .card-title {
        font-family: 'Orbitron', sans-serif;
        color: #ffcc00;
        font-size: 1.4rem;
        margin-bottom: 15px;
    }
    
    .card-desc {
        font-family: 'Inter', sans-serif;
        color: #bdc3c7;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    /* أزرار الإطلاق */
    .launch-btn {
        background: linear-gradient(90deg, #00f2ff, #0072ff);
        color: black;
        font-weight: bold;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        display: block;
        text-decoration: none;
        margin-top: 20px;
        font-family: 'Inter', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية (Sidebar) - دليل المستخدم والروابط السريعة
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2991/2991148.png", width=100) # أيقونة تعبيرية
    st.title("📘 System Manual")
    st.info("""
    **How to use the Hub:**
    1. Select a **Sector** from the top tabs.
    2. Review the **AI Capability** of each tool.
    3. Click **Launch Tool** to open the specific application.
    
    *Developed by Eng. Sulaiman Kudaimi to unify the Digital Oilfield experience.*
    """)
    st.divider()
    st.markdown("### 📞 Contact Expert")
    st.write("Eng. Sulaiman Kudaimi")
    st.write("Digital Transformation Lead")

# 3. الهيدر (Hero Section)
st.markdown("""
    <div class="hero-section">
        <p class="main-title">THE PETRO-AI COMMAND CENTER</p>
        <p style="font-family: 'Inter'; font-size: 1.2rem; color: #bdc3c7;">
            Integrated Neural Network Solutions for 15+ Industrial Oilfield Challenges
        </p>
    </div>
    """, unsafe_allow_html=True)

# 4. نظام التبويبات (Tabs) - تقسيم الـ 15 مشروعاً
tabs = st.tabs(["🌍 Subsurface", "🏗️ Drilling & Production", "💎 Digital Twins", "🛡️ HSE & Maintenance"])

# تعريف البيانات
projects_data = {
    "Subsurface": [
        {"name": "Seismic Facies AI", "url": "https://global-seismic-ai-interpretation.streamlit.app/", "desc": "Deep learning for automated seismic facies and fault interpretation."},
        {"name": "Rock & Mineral Expert", "url": "https://smart-lithology-ai-expert-ai.streamlit.app/", "desc": "High-accuracy lithology classification from cutting images (100% Acc)."},
        {"name": "Petrophysical Platform", "url": "https://safedrill-ai-pro.streamlit.app/", "desc": "Advanced well-log reconstruction and petrophysical properties estimation."},
        {"name": "PetroVision AI", "url": "https://petrovision-ai.streamlit.app/", "desc": "A unified platform for geological and visualization AI tools."}
    ],
    "Drilling & Production": [
        {"name": "SafeDrill AI Pro", "url": "https://safedrill-ai-pro.streamlit.app/", "desc": "Real-time drilling advisor for NPT reduction and safety monitoring."},
        {"name": "Production Forecaster", "url": "https://appuction-forecaster-ai.streamlit.app/", "desc": "AI-driven Decline Curve Analysis and forecasting for Volve field data."},
        {"name": "Flow Assurance AI", "url": "https://flow-assurance-ai.streamlit.app/", "desc": "Early detection of wax, scale, and hydrate formation in pipelines."},
        {"name": "PetroEconomic AI", "url": "https://petroeconomic-ai.streamlit.app/", "desc": "Smart economic advisor for field development and recovery ROI."}
    ],
    "Digital Twins": [
        {"name": "Reservoir Digital Twin", "url": "https://reservoir-digital-twin.streamlit.app/", "desc": "A high-fidelity dynamic twin for subsurface monitoring."},
        {"name": "Production AI Twin", "url": "https://digital-twin-petrol-ai.streamlit.app/", "desc": "Full asset performance twin for surface facility management."},
        {"name": "EOR Smart Simulator", "url": "https://eor-smart-simulator.streamlit.app/", "desc": "Smart waterflooding and gas injection optimization simulator."},
        {"name": "Unified PetroVision", "url": "https://petrovision-ai.streamlit.app/", "desc": "Integrating subsurface vision with field development metrics."}
    ],
    "HSE & Maintenance": [
        {"name": "AI Anomaly Detector", "url": "https://ai-anomaly-detector.streamlit.app/", "desc": "Predictive maintenance & Root Cause Analysis using sensor data."},
        {"name": "Acoustic Health AI", "url": "https://industrial-ai-diagnostic-system.streamlit.app/", "desc": "Machine health monitoring using industrial acoustic signatures (MIMII)."},
        {"name": "HSE Safety Twin", "url": "https://hse-twin-ai.streamlit.app/", "desc": "Real-time PPE detection and safety compliance monitor."},
        {"name": "PPE Monitor", "url": "https://ppe-detection-ai.streamlit.app/", "desc": "Computer vision for ensuring onsite personnel safety."}
    ]
}

# دالة لعرض البطاقات
def render_cards(category):
    cols = st.columns(2)
    for idx, project in enumerate(projects_data[category]):
        with cols[idx % 2]:
            st.markdown(f"""
                <div class="project-card">
                    <div class="card-title">💠 {project['name']}</div>
                    <div class="card-desc">{project['desc']}</div>
                    <a href="{project['url']}" target="_blank" class="launch-btn">LAUNCH APPLICATION 🚀</a>
                </div>
                """, unsafe_allow_html=True)
            st.write("")

# عرض المحتوى في كل تبويب
with tabs[0]: render_cards("Subsurface")
with tabs[1]: render_cards("Drilling & Production")
with tabs[2]: render_cards("Digital Twins")
with tabs[3]: render_cards("HSE & Maintenance")

# 5. الفوتر (Footer)
st.divider()
st.markdown("<p style='text-align: center; color: #8b949e; font-family: Inter;'>Digital Transformation Hub | <b>Eng. Sulaiman Kudaimi</b> | Portfolio © 2024</p>", unsafe_allow_html=True)
