import streamlit as st
import base64
import streamlit.components.v1 as components

def get_mermaid_url(code):
    b64 = base64.b64encode(code.encode("utf-8")).decode("ascii")
    return f"https://mermaid.ink/svg/{b64}"

def render_diagram(mermaid_code, height=300):
    url = get_mermaid_url(mermaid_code)
    components.html(
        f"""<body style="margin:0; padding:0; overflow:hidden; display:flex; justify-content:center; align-items:center;">
            <iframe src="{url}" style="width:100%; height:100%; border:none;"></iframe></body>""",
        height=height
    )

def show():
    st.markdown("### 🧪 データ型サイズ比較ラボ")
    st.info("データ型を選択して、メモリ上でどれくらいのスペース（バイト数）を使うか比較しよう。")

    dtype = st.radio(
        "型を選択してください:",
        ["char (文字)", "int (整数)", "double (実数)"],
        horizontal=True
    )

    if "char" in dtype:
        st.success("✅ `char` は **1バイト** です。最小単位です。")
        mermaid = """
        graph LR
        subgraph Memory [メモリ空間]
            c[char: 1byte]:::char
        end
        classDef char fill:#ffcc80,stroke:#333;
        """
    elif "int" in dtype:
        st.success("✅ `int` は **4バイト** です。charの4倍の場所をとります。")
        mermaid = """
        graph LR
        subgraph Memory [メモリ空間]
            direction LR
            i1[1]:::int --- i2[2]:::int --- i3[3]:::int --- i4[4]:::int
        end
        classDef int fill:#90caf9,stroke:#333;
        """
    else:
        st.success("✅ `double` は **8バイト** です。かなり巨大な領域を使います。")
        mermaid = """
        graph LR
        subgraph Memory [メモリ空間]
            direction LR
            d1[1]:::dbl --- d2[2]:::dbl --- d3[3]:::dbl --- d4[4]:::dbl
            d4 --- d5[5]:::dbl --- d6[6]:::dbl --- d7[7]:::dbl --- d8[8]:::dbl
        end
        classDef dbl fill:#a5d6a7,stroke:#333;
        """

    render_diagram(mermaid, height=200)