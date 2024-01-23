import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取Excel文件
file_path = 'Hamitonian_MAE.xlsx'  # 请替换为你的文件路径
df = pd.read_excel(file_path, index_col=0)

# 使用seaborn库绘制热力图
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(df, annot=True, cmap='viridis', fmt='.2f', cbar_kws={'label': 'Values'})
plt.title('MAE')  # 修改标题为"MAE"
plt.xlabel('Alpha')
plt.ylabel('Beta')

# 保存图像为高分辨率文件（300ppi）
output_file_path = 'Hamitonian_MAE_output.png'  # 请替换为你的输出文件路径
heatmap.get_figure().savefig(output_file_path, dpi=300)
plt.show()
