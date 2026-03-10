#!/bin/bash
set -e
 
cd /home/ec2-user/janken-app
 
# 既存プロセスを停止（初回は何もないのでエラーを無視）
pkill -f "streamlit run" || true
sleep 2
 
# streamlitのフルパスで起動
nohup /home/ec2-user/.local/bin/streamlit run app.py \
  --server.port=8501 \
  --server.address=0.0.0.0 \
  > /home/ec2-user/streamlit.log 2>&1 &
 
sleep 3
echo "Streamlit started!"
