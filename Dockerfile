# ベースイメージを指定（Python 3.11.1）
FROM python:3.11.0-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係インストールのためにrequirements.txtをコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションファイルをコピー
COPY . .

# アプリケーションを実行
CMD ["python", "flask_lottery/app.py"]