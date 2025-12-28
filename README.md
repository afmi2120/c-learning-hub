# 🎓 C Learning Hub (Interactive Pointer visualizer)

> **"Stop guessing, Start visualizing."**
> C言語の「ポインタ」や「メモリ」の挙動を、完全に可視化する学習プラットフォーム。

![Status](https://img.shields.io/badge/Status-Alpha-orange) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)

## 🧐 Why this project? (なぜ作ったか)
C言語のポインタで挫折した経験はありませんか？
「箱のイメージ」や「住所」という比喩だけでは、実際のメモリ動作は理解できません。

この **C Learning Hub** は、教科書を読むだけでなく、**実際にメモリ操作をシミュレーションし、その内部挙動をリアルタイムで図解（Mermaid.js）する** ためのツールです。
高専で情報工学を学ぶ学生（私）が、「過去の自分が欲しかったツール」として開発しました。

Have you ever struggled with C pointers?
Metaphors like "boxes" or "addresses" aren't enough.
This tool visualizes the **actual memory behavior** in real-time using Mermaid.js interactive diagrams.

## 🚀 Features (特徴)

### 1. 🧪 Pointer Lab (ポインタ実験室)
- `int *p = &a;` といったコードを実行すると、メモリ図がどう変化するかをアニメーション表示。
- Interactive buttons to simulate pointer allocation and dereferencing.

### 2. 🧠 Deep Dive Lecture (深層解説)
- 「なんとなく」を許さない詳細講義。
- **L-value / R-value**, **Stack Memory**, **Bit-level representation**.

## 🛠️ Tech Stack
- **Frontend/Backend**: [Streamlit](https://streamlit.io/)
- **Visualization**: [Mermaid.js](https://mermaid.js.org/)
- **Language**: Python

## 📦 Installation

```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/afmicreates-c-learning.git](https://github.com/YOUR_USERNAME/afmicreates-c-learning.git)
cd afmicreates-c-learning

# Create virtual environment
python -m venv .venv
# Activate (Windows)
.\.venv\Scripts\Activate
# Activate (Mac/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run Home.py

#🚧 Roadmap
[x] Basic Variables & Memory (Vol.1)

[x] Pointer Visualization Lab (Vol.2)

[ ] Arrays & Address Arithmetic (Vol.3) - Coming Soon

[ ] Quiz Mode with AI feedback

#🤝 Contribution
バグ報告、機能提案、大歓迎です！ Pull requests are welcome.

Created by afmi

