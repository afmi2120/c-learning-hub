import streamlit as st

# ==========================================
# ⚙️ ページ設定
# ==========================================
st.set_page_config(
    page_title="C Visualizer Hub",
    page_icon="⚡",
    layout="wide"
)

# ==========================================
# 🎨 デザインカスタマイズ (CSSマジック)
# ==========================================
st.markdown("""
<style>
    /* 全体のフォントと背景 */
    .stApp {
        background-color: #f8f9fc; /* 超薄いブルーグレー */
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }

    /* ヒーローセクション（タイトル周り） */
    .hero-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 60px 40px;
        border-radius: 20px;
        color: white;
        margin-bottom: 40px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin: 0;
        background: -webkit-linear-gradient(#fff, #e0e0e0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        margin-top: 15px;
        opacity: 0.9;
        font-weight: 300;
    }

    /* カリキュラムカードのデザイン */
    .card-container {
        background: white;
        border-radius: 16px;
        padding: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04);
        border: 1px solid #f0f0f0;
        transition: all 0.3s ease;
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    
    /* ホバー時のエフェクト（浮き上がる） */
    .card-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.08);
        border-color: #4a90e2;
    }

    /* カード内の装飾 */
    .card-icon {
        font-size: 3rem;
        margin-bottom: 15px;
        display: inline-block;
        padding: 10px;
        background: #f0f7ff;
        border-radius: 12px;
    }
    .card-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .card-desc {
        color: #666;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    
    /* ステータスバッジ */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 15px;
    }
    .badge-active {
        background: #e3f2fd;
        color: #1565c0;
    }
    .badge-lock {
        background: #f5f5f5;
        color: #999;
    }

</style>
""", unsafe_allow_html=True)

# ==========================================
# 🏠 メインコンテンツ
# ==========================================

# --- ヒーローセクション ---
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">C Visualizer Hub</h1>
    <p class="hero-subtitle">「見えないメモリ」を可視化する、エンジニアのための実験室。</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📚 Curriculum")

# --- グリッドレイアウト (3列) ---
col1, col2, col3 = st.columns(3)

# カード1：変数と型 (第1章)
with col1:
    st.markdown("""
    <div class="card-container">
        <span class="badge badge-active">Start Here</span>
        <div class="card-icon">🔰</div>
        <div class="card-title">Chapter 1: Basics</div>
        <p class="card-desc">
            C言語の第一歩。<br>
            変数ごとの「メモリ消費量（サイズ）」の違いを視覚的に理解します。
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/01_🔰_Basic_Types.py", label="第1章へ進む", use_container_width=True)

# カード2：ポインタ (第2章)
with col2:
    st.markdown("""
    <div class="card-container">
        <span class="badge badge-active">Popular</span>
        <div class="card-icon">👉</div>
        <div class="card-title">Chapter 2: Pointer</div>
        <p class="card-desc">
            最難関「ポインタ」を攻略。<br>
            アドレス操作と間接参照の仕組みを、実験室で動かして学びます。
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/02_👉_Pointers.py", label="第2章へ進む", use_container_width=True)

# カード3：配列 (Coming Soon)
with col3:
    st.markdown("""
    <div class="card-container">
        <span class="badge badge-lock">Coming Soon</span>
        <div class="card-icon">🚃</div>
        <div class="card-title">Chapter 3: Array</div>
        <p class="card-desc">
            配列とポインタの密接な関係。<br>
            メモリ上の連続データ配置とポインタ演算を学びます。
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.button("ロック中 🔒", disabled=True, key="btn_c3", use_container_width=True)

# --- フッター ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #aaa; font-size: 0.8rem;">
    © 2025 C Visualizer Hub | Designed for Kosen Students
</div>
""", unsafe_allow_html=True)