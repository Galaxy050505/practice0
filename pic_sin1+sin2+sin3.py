import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体，防止标题乱码 (Windows一般用SimHei，Mac用Arial Unicode MS)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义 x 的取值范围，取 -3π 到 3π 以便观察周期性
x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)

# 定义三个函数
y1 = np.abs(np.sin(x))
y2 = np.sin(np.abs(x))
y3 = 2 * np.sin(x / 2)

# 创建一个 1 行 3 列的画布，尺寸为 15x4
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# ----------------- 图1：y = |sin x| -----------------
axes[0].plot(x, y1, color='blue', linewidth=2)
axes[0].set_title(r'\(y = |\sin x|\)', fontsize=14)
axes[0].grid(True, linestyle='--', alpha=0.6)
# 设置 x 轴刻度为 π 的倍数
axes[0].set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
axes[0].set_xticklabels([r'\(-2\pi\)', r'\(-\pi\)', '0', r'\(\pi\)', r'\(2\pi\)'])
axes[0].axhline(0, color='black', linewidth=1)
axes[0].axvline(0, color='black', linewidth=1)

# ----------------- 图2：y = sin|x| -----------------
axes[1].plot(x, y2, color='red', linewidth=2)
axes[1].set_title(r'\(y = \sin |x|\)', fontsize=14)
axes[1].grid(True, linestyle='--', alpha=0.6)
axes[1].set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
axes[1].set_xticklabels([r'\(-2\pi\)', r'\(-\pi\)', '0', r'\(\pi\)', r'\(2\pi\)'])
axes[1].axhline(0, color='black', linewidth=1)
axes[1].axvline(0, color='black', linewidth=1)

# ----------------- 图3：y = 2sin(x/2) -----------------
axes[2].plot(x, y3, color='green', linewidth=2)
axes[2].set_title(r'\(y = 2\sin(\frac{x}{2})\)', fontsize=14)
axes[2].grid(True, linestyle='--', alpha=0.6)
# 周期变成了 4π，所以刻度稍微放大一些
axes[2].set_xticks([-4*np.pi, -2*np.pi, 0, 2*np.pi, 4*np.pi])
axes[2].set_xticklabels([r'\(-4\pi\)', r'\(-2\pi\)', '0', r'\(2\pi\)', r'\(4\pi\)'])
axes[2].axhline(0, color='black', linewidth=1)
axes[2].axvline(0, color='black', linewidth=1)

# 调整布局并显示
plt.tight_layout()
plt.show()
