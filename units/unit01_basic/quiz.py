import streamlit as st

def show():
    st.markdown("### 📝 理解度チェック")
    
    st.write("Q1. 一般的な環境で、`int` 型の変数は何バイトのメモリを使いますか？")
    ans = st.radio("回答を選択:", ["1 byte", "4 bytes", "8 bytes"], key="q1_basic")
    
    if st.button("回答する", key="btn_q1_basic"):
        if ans == "4 bytes":
            st.success("正解！🙆‍♂️ 整数は基本的に4バイトです。")
        else:
            st.error("不正解...🙅‍♂️ 講義ノートの表を確認しよう！")