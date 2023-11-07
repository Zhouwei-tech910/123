import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
# 尝试不同编码
encodings_to_try = ['utf-8', 'gbk', 'latin-1']

for encoding in encodings_to_try:
    try:
        train_data = np.loadtxt('训练集抗饱和.xlsx', delimiter=',', encoding=encoding)
        print(f"Successfully read the file with encoding: {encoding}")
        break  # 如果成功读取文件，就退出循环
    except UnicodeDecodeError:
        print(f"Failed to read the file with encoding: {encoding}")
