# 🎓 C Learning Hub (Vol.1: Deep Dive Lecture)

> **"Stop guessing, Start visualizing."**
> C言語の「ポインタ」や「メモリ」の挙動を、完全に可視化する学習プラットフォーム。

![Status](https://img.shields.io/badge/Status-Alpha-orange) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)

## 🧐 Why this project?
C言語のポインタで挫折した経験はありませんか？
教科書の「箱のイメージ」だけでは、実際のメモリ動作（スタック、L値/R値など）は理解できません。

この **C Learning Hub** は、高専生である私が「過去の自分が欲しかったツール」として開発しているWebアプリです。
AIを活用してコードを生成し、Mermaid.js でメモリ構造を図解します。

## 🚀 Features (現在の機能)

### ✅ Vol.1: Deep Dive Lecture (徹底解説)
- 「なんとなく」を許さない詳細講義。
- **L-value / R-value**, **Stack Memory**, **Address Logic**.
- 教科書の隙間を埋める、深いメモリの理屈を解説。

### 🚧 Vol.2: Pointer Lab (Coming Soon)
- ポインタの接続や書き換えを実験できるシミュレーター機能を開発中。
- *Work in Progress...*

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Visualization**: Mermaid.js
- **Language**: Python

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/afmicreates-c-learning.git
cd afmicreates-c-learning
pip install -r requirements.txt
streamlit run Home.py
