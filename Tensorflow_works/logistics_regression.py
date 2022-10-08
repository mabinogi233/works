import tensorflow as tf
import numpy as np

#逻辑回归

def sigmoid(x):
    return 1/(1+np.exp(-x))

x_data = np.random.randn(20000,3)
w_real = [[-5],[-4],[3]]
b_real = 5
wxb = np.matmul(x_data,w_real) + b_real

#加入噪声 ？
y_noise = sigmoid(wxb)
y_data = np.random.binomial(1,y_noise)

print(y_data)

with tf.Graph().as_default():
    x = tf.placeholder(tf.float32,[None,3])
    y_true = tf.placeholder(tf.float32,None)

    with tf.name_scope('inference'):
        w = tf.Variable([[0,0,0]],dtype=tf.float32)
        b = tf.Variable(0,dtype=tf.float32)
        wb = tf.matmul(x,tf.transpose(w)) + b
        y_pred = tf.sigmoid(wb)

    with tf.name_scope('loss'):
        loss=tf.nn.sigmoid_cross_entropy_with_logits(labels=y_true,logits=y_pred)
        loss=tf.reduce_mean(loss)

    with tf.name_scope('train'):
        train=tf.train.GradientDescentOptimizer(0.5).minimize(loss)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(3000):
            sess.run(train,{x:x_data,y_true:y_data})
            print(i,sess.run([w,b]))
