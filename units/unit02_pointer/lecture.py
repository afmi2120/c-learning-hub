import streamlit as st
import base64
import streamlit.components.v1 as components

# ==========================================
# 🛠️ ヘルパー関数（図解表示用）
# ==========================================
def get_mermaid_url(code):
    """MermaidのコードをBase64変換してURL化する"""
    b64 = base64.b64encode(code.encode("utf-8")).decode("ascii")
    return f"https://mermaid.ink/svg/{b64}"

def render_diagram(mermaid_code, height=250, caption=""):
    """Iframeを使って図を確実に表示する"""
    url = get_mermaid_url(mermaid_code)
    if caption:
        st.caption(f"▼ {caption}")
    components.html(
        f"""
        <body style="margin:0; padding:0; overflow:hidden; display:flex; justify-content:center; align-items:center;">
            <iframe src="{url}" style="width:100%; height:100%; border:none;"></iframe>
        </body>
        """,
        height=height
    )

# ==========================================
# 📖 講義メインパート
# ==========================================
def show():
    # --- CSSデザイン (高専スタイル＋実用性) ---
    st.markdown("""
    <style>
        .stApp { font-family: "Helvetica Neue", Arial, sans-serif; line-height: 1.7; color: #333; }
        /* 大見出し */
        h2 {
            border-left: 8px solid #0056b3;
            padding-left: 15px; margin-top: 60px; margin-bottom: 25px;
            background: #f0f4f8; padding-top: 8px; padding-bottom: 8px;
            font-size: 24px; font-weight: bold;
        }
        /* 中見出し */
        h3 {
            margin-top: 40px; border-bottom: 2px solid #ddd;
            padding-bottom: 5px; color: #444; font-size: 20px;
        }
        /* 強調キーワード */
        .keyword {
            color: #d63384; font-weight: bold; background-color: #fff0f6;
            padding: 2px 5px; border-radius: 3px;
        }
        /* 目次ボックス */
        .toc-box {
            background-color: #f8f9fa; border: 1px solid #ddd;
            padding: 20px; border-radius: 5px; margin-bottom: 40px;
        }
        .toc-list a { text-decoration: none; color: #0056b3; font-weight: 500; }
        .toc-list a:hover { text-decoration: underline; }
        /* 応用例の枠 */
        .use-case-box {
            border: 1px solid #28a745; border-top: 4px solid #28a745;
            background-color: #f9fff9; padding: 15px; margin-top: 20px;
            border-radius: 3px;
        }
        .use-case-title {
            color: #28a745; font-weight: bold; margin-bottom: 10px;
            display: flex; align-items: center;
        }
        .use-case-title::before { content: "🚀"; margin-right: 8px; }
    </style>
    """, unsafe_allow_html=True)

    st.title("👉 第2章: ポインタの基礎と応用")
    st.markdown("**基礎知識から、現場で必須となる実践的な活用パターンまでを網羅する。**")

    # --- 目次 ---
    st.markdown("""
    <div class="toc-box">
    <strong>📚 講義目次</strong>
    <ul class="toc-list" style="list-style:none; padding-left:0;">
        <li><strong>第1部：基礎編</strong></li>
        <li style="margin-left:20px;"><a href="#sec1">1. ポインタの本質（復習）</a></li>
        <li style="margin-left:20px;"><a href="#sec2">2. 参照渡し（Swap関数）</a></li>
        <li style="margin-top:15px;"><strong>第2部：応用・活用編</strong></li>
        <li style="margin-left:20px;"><a href="#sec3">3. 配列とポインタの密接な関係</a></li>
        <li style="margin-left:20px;"><a href="#sec4">4. 動的メモリ確保 (malloc/free)</a></li>
        <li style="margin-left:20px;"><a href="#sec5">5. 構造体とアロー演算子 (->)</a></li>
        <li style="margin-left:20px;"><a href="#sec6">6. その他の重要活用例</a></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.header("第1部：基礎編（要点のみ）")

    # =================================================================
    # 1. 基礎復習
    # =================================================================
    st.markdown('<h2 id="sec1">1. ポインタの本質（復習）</h2>', unsafe_allow_html=True)
    st.write("""
    ポインタとは、データそのものではなく**「データの居場所（メモリアドレス）」を記憶する変数**である。
    これを使うことで、メモリ上の特定の位置を遠隔操作（間接参照）できる。
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.code("int *p = &a; // aの住所をpに入れる", language="c")
        st.caption("アドレス演算子 `&`")
    with col2:
        st.code("*p = 99;     // pが指す場所の中身を書き換える", language="c")
        st.caption("間接参照演算子 `*`")

    # =================================================================
    # 2. 参照渡し
    # =================================================================
    st.markdown('<h2 id="sec2">2. 参照渡し（Swap関数）</h2>', unsafe_allow_html=True)
    st.write("""
    関数の引数として巨大なデータを渡す際、コピーを作成するとメモリと時間の無駄になる。
    ポインタ（住所）を渡せば、関数内から呼び出し元のオリジナルデータを直接操作でき、効率が良い。
    （※詳細な図解は前回のバージョンを参照。ここでは結論のみ述べる）
    """)

    st.markdown("---")
    st.header("第2部：応用・活用編（ここからが本番）")

    # =================================================================
    # 3. 配列とポインタ
    # =================================================================
    st.markdown('<h2 id="sec3">3. 配列とポインタの密接な関係</h2>', unsafe_allow_html=True)
    st.markdown("""
    C言語において、**「配列名」は実質的に「先頭要素へのポインタ」**として扱われる。
    これが理解できないと、C言語で配列操作はできない。
    """)

    st.subheader("活用例 3.1: ポインタ演算による配列アクセス")
    st.write("配列の要素はメモリ上に連続して並んでいる。そのため、ポインタに 1 を足すと「次の要素のアドレス」になる。")

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.code("""
int arr[3] = {10, 20, 30};
int *p = arr; // 配列名は先頭アドレス!

// 以下の3つは全て同じ意味
printf("%d", arr[1]);    // 添字アクセス
printf("%d", *(p + 1));  // ポインタ演算
printf("%d", *(arr + 1));// 配列名でポインタ演算
// 出力: 全て 20
        """, language="c")
    with col2:
        mermaid_arr = """
        graph LR
        subgraph Memory [メモリ空間 (連続)]
            direction LR
            e0[arr[0]: 10] --- e1[arr[1]: 20] --- e2[arr[2]: 30]
        end
        p_ptr[ポインタ p] -- p+0 --> e0
        p_ptr -- p+1 --> e1
        p_ptr -- p+2 --> e2
        style p_ptr fill:#fdfd96,stroke:#fbc02d
        linkStyle 0,1,2 stroke:red,stroke-width:2px;
        """
        render_diagram(mermaid_arr, height=180, caption="図: ポインタに足し算すると隣の要素を指す")

    # =================================================================
    # 4. 動的メモリ確保
    # =================================================================
    st.markdown('<h2 id="sec4">4. 動的メモリ確保 (malloc/free)</h2>', unsafe_allow_html=True)
    st.markdown("""
    プログラム実行時までデータのサイズが分からない場合（例：読み込む画像の大きさが不明）、
    コンパイル時に固定サイズ配列 `int arr[100];` を用意するのは非効率である。

    ポインタを使えば、**実行時に必要な分だけメモリを借りる（動的確保）**ことができる。
    これにはヒープ領域が使われる。
    """)

    st.subheader("活用例 4.1: 実行時にサイズが決まる配列")
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.code("""
#include <stdlib.h>

int n;
scanf("%d", &n); // 実行時にサイズnを入力

// n個分のint型メモリを確保！
// mallocは確保した場所の「先頭ポインタ」を返す
int *arr = (int*)malloc(sizeof(int) * n);

if (arr == NULL) { /* エラー処理 */ }

// 普通の配列のように使える
for(int i=0; i<n; i++) {
    arr[i] = i * 10;
}

// 使い終わったら必ず返却（解放）!
free(arr);
arr = NULL; // 安全のため
        """, language="c")
    with col2:
        st.markdown("""
        <div class="use-case-box">
        <div class="use-case-title">ここがポイント</div>
        <ul>
            <li><code>malloc</code> 関数は、指定バイト数のメモリをヒープ領域から探し出し、その<strong>先頭アドレス（ポインタ）</strong>を返す。</li>
            <li>受け取ったポインタ <code>arr</code> は、その後普通の配列と同じように添字 <code>arr[i]</code> で使える。</li>
            <li><strong>借りたメモリは必ず <code>free</code> で返すこと。</strong>忘れるとメモリリーク（メモリの食いつぶし）が発生する。</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # =================================================================
    # 5. 構造体とポインタ
    # =================================================================
    st.markdown('<h2 id="sec5">5. 構造体とアロー演算子 (->)</h2>', unsafe_allow_html=True)
    st.write("構造体（複数のデータをまとめたもの）を扱う場合も、サイズが大きくなりがちなのでポインタ経由で操作するのが一般的だ。")

    st.subheader("活用例 5.1: 構造体のメンバへのアクセス")
    st.write("構造体のポインタから、そのメンバ（中身）にアクセスするには、特別な**アロー演算子 `->`** を使う。")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("""
typedef struct {
    char name[20];
    int hp;
} Player;

int main() {
    Player hero = {"勇者", 100};
    // 構造体のポインタを作成
    Player *p = &hero;

    // 【重要】ポインタ経由でのアクセス
    // (*p).hp = 80; と同じ意味だが、
    // 通常は矢印(->)を使う。読みやすい。
    p->hp -= 20; // ダメージを受けた！

    printf("%sのHP: %d", p->name, p->hp);
    // 出力: 勇者のHP: 80
}
        """, language="c")
    with col2:
        mermaid_struct = """
        graph LR
        subgraph Memory
            subgraph struct_hero [構造体 hero]
                name[name: "勇者"]
                hp[hp: 100]
            end
            p_ptr[ポインタ p]
        end
        p_ptr -- "p->hp でアクセス" --> hp
        style p_ptr fill:#fdfd96
        style struct_hero fill:#daf5e9
        linkStyle 0 stroke:red,stroke-width:3px;
        """
        render_diagram(mermaid_struct, height=200, caption="図: アロー演算子で構造体の中身を指す")

    # =================================================================
    # 6. その他の活用例
    # =================================================================
    st.markdown('<h2 id="sec6">6. その他の重要活用例</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div class="use-case-box">
    <div class="use-case-title">文字列操作 (char*)</div>
    <p>C言語に「文字列型」は存在しない。文字列は<strong>「文字配列の先頭へのポインタ (`char *`)」</strong>として扱われる。</p>
    <ul>
        <li><code>char *str = "Hello";</code> は、メモリ上のどこかにある "Hello" という文字配列の先頭アドレスを <code>str</code> に入れている。</li>
        <li>文字列操作関数（<code>strcpy</code>, <code>strlen</code> など）は全てポインタを受け取って動作する。</li>
    </ul>
    </div>

    <div class="use-case-box">
    <div class="use-case-title">関数ポインタ（高度な応用）</div>
    <p>ポインタが指せるのはデータだけではない。<strong>「関数（処理コード）」のアドレス</strong>を指すこともできる。</p>
    <ul>
        <li>これを「関数ポインタ」と呼ぶ。</li>
        <li>関数の引数に「別の関数」を渡すことができるようになる（コールバック関数）。</li>
        <li>例：ボタンが押された時に実行する関数を登録しておく、など。GUIプログラミングでは必須の技術。</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.write("応用編は以上だ。ポインタが単なる「住所録」ではなく、C言語のあらゆる高度な機能の基盤となっていることが理解できただろうか。")
    st.info("これらの応用例は、今後の「配列」「構造体」の単元で、それぞれ専用の実験室を用意して深掘りしていく予定である。")