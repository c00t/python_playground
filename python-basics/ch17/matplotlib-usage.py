from matplotlib import pyplot as plt
import numpy as np

# 1. plot costumed color-style plot
# plt.plot([-1, 0, 1, 2, 3, 4], [1, 2, 3, 5, 4, 2], "g-o")
# plt.show()

# 2.
# days = np.arange(0, 21)
# other_sites, real_python = days, days ** 2
# plt.plot(days, other_sites, "g-o")
# plt.plot(days, real_python, "r-^")
# # use `plt.xticks()` to costumed x axis
# plt.xticks([0, 5, 10, 15, 20])
# # 指定x, y轴标签说明
# plt.xlabel("days")
# plt.ylabel("what you know")
# plt.legend(["other_sites", "real_python"])
# plt.show()

# hist
plt.hist(np.random.randn(10000), 20)
#
plt.savefig("result.png")
plt.show()