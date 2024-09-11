# coding: utf-8

# Author: Du Mingzhe (mingzhe@nus.edu.sg)
# Date: 2024/09/11

import os
import streamlit as st

# Hello from IDS
st.title(":blue[IDS] Inference Engine")

# Load Model
model_path = st.text_input("Model Path", "meta-llama/Meta-Llama-3.1-8B-Instruct")
go = st.button("Go 🚀")
if go:
  os.system("docker stop $(docker ps -a -q)")
  os.system("docker rm $(docker ps -a -q)")
  docker_command = f'docker run  -d --runtime nvidia --gpus all     -v /mnt/disks/vllm_cache:/root/.cache/huggingface     --env "HUGGING_FACE_HUB_TOKEN=<your token>"     -p 8000:8000     --ipc=host     vllm/vllm-openai:latest     --model {model_path}     --dtype auto     --api-key yyids'
  os.system(docker_command)
  st.write("Model is deploying... You may grab a coffee and wait for a few (3-5) minutes.")

st.header("Model Usage")
# Model Usage
code = """
from openai import OpenAI
client = OpenAI(
    base_url="http://35.198.210.48:8000/v1",
    api_key="<token>",
)

completion = client.chat.completions.create(
  model="meta-llama/Meta-Llama-3.1-8B-Instruct",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
"""
st.code(code, language="python")
