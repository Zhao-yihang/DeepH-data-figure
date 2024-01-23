import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取Excel文件
file_path = 'DOS_1.xlsx'  # 请替换为文件路径:DOS_1,DOS_2,DOS_3
df = pd.read_excel(file_path)

# 提取后两列数据
column_2 = df.iloc[:, 1]
column_3 = df.iloc[:, 2]

# 计算两列数据之间的相关系数
correlation_coefficient = np.corrcoef(column_2, column_3)[0, 1]

print(f'Correlation Coefficient (R): {correlation_coefficient}')

# 使用matplotlib库绘制相关系数的图像
plt.figure(figsize=(6, 6))
plt.scatter(column_2, column_3, color='blue', alpha=0.5)
plt.title('Scatter Plot with Correlation Coefficient')
plt.xlabel('Column 2')
plt.ylabel('Column 3')

# 在图中显示相关系数
plt.text(min(column_2), max(column_3), f'R = {correlation_coefficient:.4f}', fontsize=12, color='red')

# 保存图像为高分辨率文件（300ppi）
output_file_path = 'correlation_plot3.png'  # 请替换为你的输出文件路径
plt.savefig(output_file_path, dpi=300)
plt.show()
