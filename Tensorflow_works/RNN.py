import tensorflow as tf
import numpy as np

from tensorflow.python.ops.rnn import dynamic_rnn

with tf.name_scope('ruu_w'):
    with tf.name_scope('wx'):
        # x向量权重矩阵
        # x向量大小 * 隐藏层向量大小
        wx = tf.Variable(tf.zeros([x_size , hidden_layer_size]))
    with tf.name_scope('wh'):
        # h 向量权重矩阵 ,h 向量为隐藏层向量
        # h 向量大小 * h向量大小
        wh = tf.Variable(tf.zeros([hidden_layer_size , hidden_layer_size]))
    with tf.name_scope('bias'):
        # 偏移量
        b = tf.Variable(tf.zeros([hidden_layer_size]))

def rnn_step(prev_h,x):
    # h(n) = tanh ( x(n) * wx + h(n-1) * wh + b )
    return tf.nn.tanh(
        tf.matmul(prev_h,wh)+
        tf.matmul(x,wx)+
        b
    )

init_hidden = tf.zeros([batch_size , hidden_layer_size])
all_hidden_states = tf.scan(rnn_step, input ,initializer=init_hidden,name='states')
# input 中 第一个轴表示时间轴



"""RNN ,too"""
input = tf.placeholder(tf.float32,[None , time_steps , element_size])
rnn_cell = tf.contrib.rnn.BasicRNNCell(hidden_layer_size)
outputs , last_states = dynamic_rnn(rnn_cell,inputs,dtype= tf.float32)


