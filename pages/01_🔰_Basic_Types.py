import streamlit as st
from units.unit01_basic import lecture, lab, quiz

# ==========================================
# ⚙️ ページ設定
# ==========================================
st.set_page_config(
    page_title="Chapter 1: Basics",
    page_icon="🔰",
    layout="wide"
)

# ==========================================
# 🎨 デザインカスタマイズ (CSS)
# ==========================================
st.markdown("""
<style>
    /* 全体の背景とフォント */
    .stApp {
        background-color: #f8f9fc;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    
    /* ヒーローヘッダー (章のタイトル) */
    .chapter-header {
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        padding: 40px 30px;
        border-radius: 15px;
        color: #1a4d2e;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .chapter-sub {
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.9rem;
        opacity: 0.8;
        margin-bottom: 5px;
        font-weight: bold;
    }
    .chapter-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
    }

    /* タブのデザイン */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
        padding-bottom: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        border-radius: 8px;
        background-color: white;
        border: 1px solid #e0e0e0;
        color: #555;
        font-weight: 600;
        transition: all 0.2s;
        padding: 0 20px;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #f0f7ff;
        border-color: #4a90e2;
        color: #4a90e2;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4a90e2 !important;
        color: white !important;
        border-color: #4a90e2 !important;
        box-shadow: 0 4px 6px rgba(74, 144, 226, 0.3);
    }
    
    /* ロック画面のデザイン */
    .lock-screen {
        background-color: #f1f3f5;
        border: 2px dashed #adb5bd;
        border-radius: 10px;
        padding: 40px;
        text-align: center;
        color: #868e96;
        margin-top: 20px;
    }
    .lock-icon {
        font-size: 3rem;
        margin-bottom: 15px;
        display: block;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🚀 メインコンテンツ
# ==========================================

# --- 章のヒーローヘッダー ---
st.markdown("""
<div class="chapter-header">
    <div class="chapter-sub">Chapter 01</div>
    <div class="chapter-title">🔰 変数とデータ型</div>
    <p style="margin-top: 10px; opacity: 0.9;">
        すべての基礎となる「メモリサイズ」の感覚を掴む。
    </p>
</div>
""", unsafe_allow_html=True)

# --- ナビゲーションタブ ---
tab1, tab2, tab3 = st.tabs(["📖 講義ノート", "🧪 サイズ実験室", "📝 クイズ"])

# --- ヘルパー関数: ロック画面表示 ---
def show_lock_screen(title, message="現在メンテナンス中です"):
    st.markdown(f"""
    <div class="lock-screen">
        <span class="lock-icon">🔒</span>
        <h3>{title} は閉鎖中です</h3>
        <p>{message}</p>
    </div>
    """, unsafe_allow_html=True)

# --- タブ1: 講義ノート (ここだけ表示) ---
with tab1:
    lecture.show()

# --- タブ2: 実験室 (閉鎖) ---
with tab2:
    # lab.show() <-- ロック
    show_lock_screen("データ型サイズ実験室", "講義パートの改修に伴い、一時的に閉鎖しています。<br>まずは講義でサイズの概念を確認してください。")

# --- タブ3: クイズ (閉鎖) ---
with tab3:
    # quiz.show() <-- ロック
    show_lock_screen("理解度チェック", "問題を作成中です。")