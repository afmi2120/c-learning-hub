import streamlit as st
import base64
import streamlit.components.v1 as components

def get_mermaid_url(code):
    b64 = base64.b64encode(code.encode("utf-8")).decode("ascii")
    return f"https://mermaid.ink/svg/{b64}"

def render_diagram(mermaid_code, height=200):
    url = get_mermaid_url(mermaid_code)
    components.html(
        f"""<body style="margin:0; padding:0; overflow:hidden; display:flex; justify-content:center; align-items:center;">
            <iframe src="{url}" style="width:100%; height:100%; border:none;"></iframe></body>""",
        height=height
    )

def show():
    # CSSデザイン（第2章と統一）
    st.markdown("""
    <style>
        h2 { border-left: 8px solid #0056b3; padding-left: 15px; background: #f0f4f8; padding-top: 8px; padding-bottom: 8px; border-radius: 0 5px 5px 0; }
        .keyword { color: #d63384; font-weight: bold; background-color: #fff0f6; padding: 2px 5px; border-radius: 3px; }
        .note-box { background-color: #fff9db; border-left: 5px solid #ffec99; padding: 20px; margin: 20px 0; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("#### 講義: メモリとデータ型の基礎")
    st.markdown("C言語を学ぶ上で避けて通れないのが**「型（Type）」と「サイズ（Size）」**の関係である。")

    st.markdown("## 1. 変数は「箱」である")
    st.markdown("""
    コンピュータのメモリは、1バイト（8ビット）ごとの細かい区画に分かれている。
    変数を宣言するというのは、この区画を**「いくつか占領して、名前をつける」**ことである。
    
    重要なのは、**「型によって、占領する広さが違う」**ということだ。
    """)

    st.markdown("### 代表的なデータ型とサイズ")
    st.markdown("""
    | 型名 | サイズ | イメージ | 用途 |
    | :--- | :--- | :--- | :--- |
    | `char` | **1 byte** | 📦 | 文字 (A, b, @) |
    | `int` | **4 bytes** | 📦📦📦📦 | 整数 (100, -5) |
    | `double`| **8 bytes** | 📦x8 | 実数 (3.14) |
    """)

    st.markdown("## 2. sizeof演算子")
    st.write("変数のサイズを調べるには `sizeof` 演算子を使う。")
    st.code('printf("int型の大きさ: %d bytes", sizeof(int));', language="c")
    
    st.markdown("""
    <div class="note-box">
    <strong>💡 なぜサイズが重要なのか？</strong><br>
    将来「配列」や「ポインタ」を扱うとき、「1つ隣のデータ」がメモリ上で何バイト先にあるかを知る必要があるからだ。<br>
    隣のタブで、実際の大きさの違いを目で見て確認せよ。
    </div>
    """, unsafe_allow_html=True)