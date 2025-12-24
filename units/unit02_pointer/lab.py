import streamlit as st
import base64
import streamlit.components.v1 as components

def get_mermaid_url(code):
    b64 = base64.b64encode(code.encode("utf-8")).decode("ascii")
    return f"https://mermaid.ink/svg/{b64}"

def show():
    """ポインタ実験室を表示する関数"""
    
    # State管理
    if 'memory' not in st.session_state:
        st.session_state.memory = {}
    if 'code_log' not in st.session_state:
        st.session_state.code_log = []
    if 'explanation' not in st.session_state:
        st.session_state.explanation = "👈 左側の操作パネルから実験を開始してください。"

    st.markdown("#### 🧪 ポインタ・シミュレーター")
    
    col1, col2 = st.columns([1, 2])
    
    # --- 左側: 操作パネル ---
    with col1:
        with st.expander("Step 1: 宣言", expanded=True):
            if st.button("int a = 10;", key="btn_decl_a"):
                st.session_state.memory['a'] = {'type': 'int', 'value': 10, 'address': '0x1000'}
                st.session_state.code_log.append("int a = 10;")
                st.session_state.explanation = "変数 `a` を確保しました。アドレスは `0x1000` です。"

            if st.button("int *p = &a;", key="btn_decl_p"):
                if 'a' in st.session_state.memory:
                    st.session_state.memory['p'] = {'type': 'pointer', 'value': '0x1000', 'address': '0x2000', 'target': 'a'}
                    st.session_state.code_log.append("int *p = &a;")
                    st.session_state.explanation = "ポインタ `p` を宣言しました。`p` の中身は `a` のアドレスです。"
                else:
                    st.error("⚠️ 先に変数 a を宣言してください")

        with st.expander("Step 2: 操作", expanded=True):
            if st.button("a = 50;", key="btn_assign_a"):
                if 'a' in st.session_state.memory:
                    st.session_state.memory['a']['value'] = 50
                    st.session_state.code_log.append("a = 50;")
                    st.session_state.explanation = "`a` に直接 `50` を代入しました。"

            if st.button("*p = 99;", key="btn_assign_p"):
                if 'p' in st.session_state.memory:
                    target = st.session_state.memory['p']['target']
                    st.session_state.memory[target]['value'] = 99
                    st.session_state.code_log.append("*p = 99;")
                    st.session_state.explanation = "ポインタ `p` を経由して、遠隔操作で `a` を `99` に変えました！"

        if st.button("🗑️ リセット", key="btn_reset"):
            st.session_state.memory.clear()
            st.session_state.code_log.clear()
            st.session_state.explanation = "リセットしました。"

        st.caption("実行コード履歴")
        for c in st.session_state.code_log:
            st.code(c, language="c")

    # --- 右側: メモリ可視化 ---
    with col2:
        if not st.session_state.memory:
            mermaid = """
            graph TD;
            Start[👈 実験を始めてください]:::guide;
            classDef guide fill:#fff,stroke:#ccc,stroke-width:2px,stroke-dasharray: 5 5;
            """
        else:
            mermaid = "graph LR;\n"
            mermaid += "classDef int_box fill:#daf5e9,stroke:#333,stroke-width:2px,font-size:18px;\n"
            mermaid += "classDef ptr_box fill:#fdfd96,stroke:#333,stroke-width:2px,font-size:18px;\n"
            mermaid += "classDef changed fill:#ffcccc,stroke:#f00,stroke-width:4px,font-size:18px;\n"

            for name, data in st.session_state.memory.items():
                value = data['value']
                label = f"{name}<br/>(Addr:{data['address']})<hr/>{value}"
                mermaid += f'{name}["{label}"];\n'
                style_class = "int_box" if data['type'] == 'int' else "ptr_box"
                if value == 50 or value == 99:
                    style_class = "changed"
                mermaid += f"class {name} {style_class};\n"

            edge_index = 0
            for name, data in st.session_state.memory.items():
                if data['type'] == 'pointer':
                    mermaid += f"{name} --> {data['target']};\n"
                    mermaid += f"linkStyle {edge_index} stroke:red,stroke-width:3px;\n"
                    edge_index += 1

        url = get_mermaid_url(mermaid)

        # 二重iframe構造（エラー回避の要）
        components.html(
            f"""
            <body style="margin:0; padding:0; overflow:hidden;">
                <iframe src="{url}" style="width:100%; height:100%; border:none;"></iframe>
            </body>
            """,
            height=400
        )
        
        st.info(st.session_state.explanation)