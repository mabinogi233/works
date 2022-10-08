import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data
import numpy as np

#线性回归方程 y = w * x + b

#2000个 特征值为3
x_data=np.random.randn(2000,3)

W = [1,5,8]
B = -10

#高斯噪声 ？
nosie = np.random.randn(1,2000)*0.1

y_data = np.matmul(x_data,W) + B + nosie

g=tf.Graph()

with g.as_default():
    x=tf.placeholder(tf.float32,[None,3])
    # y的真实值
    y_true=tf.placeholder(tf.float32,shape=None)

    with tf.name_scope('inference'):
        # 3 * 1矩阵
        w = tf.Variable([[0,0,0]],dtype=tf.float32,name='weight')
        b = tf.Variable(0,dtype=tf.float32,name='bias')
        #  W 点乘 X 加 b
        y_pred = tf.add(tf.matmul(w,tf.transpose(x)),b)

    with tf.name_scope('loss'):
        # 均方误差
        loss = tf.reduce_mean(tf.square(tf.subtract(y_pred,y_true)))

    with tf.name_scope('train'):
        # 随机梯度下降优化器,参数为学习率
        optimizer=tf.train.GradientDescentOptimizer(0.5)

        train=optimizer.minimize(loss)

    # 变量初始化
    init = tf.global_variables_initializer()

    #对变量进行优化
    with tf.Session() as sess:
        # 运行变量初始化程序
        sess.run(init)

        # 运行随机梯度下降优化器，传入数据集
        sess.run(train,{x:x_data,y_true:y_data})

        print(sess.run([w,b]))#优化变量
