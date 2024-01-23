import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取Excel文件
file_path = 'test3.xlsx'  # 请替换为你的文件路径
df = pd.read_excel(file_path)

# 使用matplotlib库绘制折线图
plt.figure(figsize=(10, 6))

# 绘制第二列为红色实线（调整线宽和颜色亮度）
plt.plot(df.iloc[:, 0], df.iloc[:, 1], color='red', linewidth=5,label='Column 2 (Red Solid)')

# 绘制第三列为绿色虚线（调整线宽和颜色亮度）
plt.plot(df.iloc[:, 0], df.iloc[:, 2], color=sns.light_palette("green", as_cmap=True)(0.8),
         linewidth=8, linestyle='--', dashes=(1, 1), label='Column 3 (Green Dashed)')

# 设置图例
plt.legend()

# 设置标题和坐标轴标签
plt.title('Line Chart')
plt.xlabel('Energy')
plt.ylabel('Density')

# 保存图像为高分辨率文件（300ppi）
output_file_path = 'bold_line_chart3.png'  # 请替换为你的输出文件路径
plt.savefig(output_file_path, dpi=300)
plt.show()
