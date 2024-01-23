import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
file_path = 'CON_3.xlsx'  # 请替换为文件路径:CON_1,CON_2,CON_3
df = pd.read_excel(file_path)

# 使用matplotlib库绘制折线图
plt.figure(figsize=(10, 6))

# 绘制第二列为红色实线
plt.plot(df.iloc[:, 0], df.iloc[:, 1], linewidth=5, color='red', label='Column 2 (Red Solid)')

# 绘制第三列为绿色虚线
plt.plot(df.iloc[:, 0], df.iloc[:, 2], linewidth=5, color='green', linestyle='--', label='Column 3 (Green Dashed)')

# 设置图例
plt.legend()

# 设置标题和坐标轴标签
plt.title('Conductivity Line Chart')
plt.xlabel('Energy (eV)')
plt.ylabel('Conductivity')

# 保存图像为高分辨率文件（300ppi）
output_file_path = 'conductivity_line_chart3.png'  # 请替换为你的输出文件路径
plt.savefig(output_file_path, dpi=300)
plt.show()
