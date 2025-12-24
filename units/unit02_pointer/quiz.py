import streamlit as st

def show():
    """クイズを表示する関数"""
    st.markdown("### 📝 理解度チェック")
    
    st.write("Q1. `int *p = &a;` と宣言したとき、`p` の中身に入っている値は何ですか？")
    
    answer = st.radio(
        "正解を選んでください:",
        ("変数 a の値 (10など)", "変数 a のメモリアドレス (0x1000など)", "p 自身のメモリアドレス (0x2000など)"),
        key="quiz_q1"
    )
    
    if st.button("回答する", key="btn_quiz_q1"):
        if "変数 a のメモリアドレス" in answer:
            st.balloons()
            st.success("正解！🙆‍♂️ ポインタには「変数の住所」が入ります。")
        else:
            st.error("残念...🙅‍♂️ 講義ノートを見直してみよう！")