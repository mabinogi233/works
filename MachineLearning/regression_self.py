import numpy as np


def sigmoid(x):
    """ 对数几率函数，用于将预测值映射到[0,1]区间上，返回[0,1]上的值 """
    return 1.0 / (1 + np.exp(-x))


def fit(X_train, y_train):
    """ 使用训练集训练模型，返回权重参数w """
    # 初始令权重参数w全1，其中添加最后一行常数b
    w = (np.ones((np.shape(X_train)[1] + 1, 1)))
    # 因为w最后一行增加了常数b，所以训练数据的最后一列添加一列1用于和b相乘
    X_train = np.c_[X_train, np.ones((np.shape(X_train)[0], 1))]
    # 定义步长，手动调参至0.0005，结果较佳
    step_len = 0.0005
    # 迭代次数
    iterations = 1
    # 开始迭代，使用梯度下降算法得出最佳参数，手动调整迭代次数为10000次较佳
    while iterations <= 10000:
        # 每次迭代先计算对数函数结果
        sigmoid_result = sigmoid(np.dot(X_train, w))
        # 计算结果和真实值的误差
        error = sigmoid_result - y_train
        # 得到增量
        delta = np.dot(np.transpose(X_train), error)
        # 权重参数更新为减去增量乘步长的值
        w = w - delta * step_len
        iterations = iterations + 1
    return w


def score(X_test, y_test, w):
    """ 使用测试集和模型参数测试模型并返回正确率 """
    # 计算预测值
    y_predict = sigmoid(np.dot(np.c_[X_test, np.ones((np.shape(X_train)[0], 1))], w))
    # 将预测值以0.5分界
    for i in range(np.shape(y_predict)[0]):
        if y_predict[i] >= 0.5:
            y_predict[i] = 1
        else:
            y_predict[i] = 0
    # 正确数量
    right = 0
    # 总测试集大小
    total = np.shape(y_test)[0]
    for i in range(total):
        if y_predict[i] == y_test[i]:
            right = right + 1
    print("[ true/predict ]")
    for i in range(total):
        print("[ " + str(y_test[i]) + " /" + str(y_predict[i]) + " ]")
    return right / total


def load_datasets(path):
    """ 用于从指定路径读出训练数据，并且对训练数据进行直接映射处理 """
    X = []
    y = []
    # 对文字信息做直接映射成数字处理
    with open(path, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            l = line.split()
            if l[0] == "青绿":
                l[0] = 0
            if l[0] == "乌黑":
                l[0] = 1
            if l[0] == "浅白":
                l[0] = 2
            if l[1] == "蜷缩":
                l[1] = 0
            if l[1] == "稍蜷":
                l[1] = 1
            if l[1] == "硬挺":
                l[1] = 2
            if l[2] == "浊响":
                l[2] = 0
            if l[2] == "沉闷":
                l[2] = 1
            if l[2] == "清脆":
                l[2] = 2
            if l[3] == "清晰":
                l[3] = 0
            if l[3] == "稍糊":
                l[3] = 1
            if l[3] == "模糊":
                l[3] = 2
            if l[4] == "凹陷":
                l[4] = 0
            if l[4] == "稍凹":
                l[4] = 1
            if l[4] == "平坦":
                l[4] = 2
            if l[5] == "硬滑":
                l[5] = 0
            if l[5] == "软粘":
                l[5] = 1
            if l[6] == "是":
                l[6] = 1
            if l[6] == "否":
                l[6] = 0
            X.append(l[0:6])
            y.append([l[6]])
    return X, y


if __name__ == "__main__":
    X, y = load_datasets(r"E:\文件\机器学习\watermelon.txt")
    X_train = np.array(X)
    y_train = np.array(y)
    w = fit(X_train, y_train)
    print(score(X_train, y_train, w))
