import tensorflow as tf
import numpy as np

with tf.Graph().as_default():
    # (a + b ) * c - ( e / f ) % g
    a = tf.constant([1,2,3,4,5],dtype=tf.int32)
    b = tf.constant([5,4,3,2,1],dtype=tf.int32)
    c = tf.constant([1,1,1,1,1],dtype=tf.int32)
    e = tf.constant([7,5,4,6,2],dtype=tf.int32)
    f = tf.constant([1,1,1,1,1],dtype=tf.int32)
    g = tf.constant([7,5,4,6,2],dtype=tf.int32)
    ab = tf.add(a,b)
    abc= tf.multiply(ab,c)
    ef = tf.divide(e,f)
    efx=tf.cast(ef,tf.int32)
    efg= tf.mod(efx,g)
    result = tf.subtract(abc,efg)

    with tf.Session() as sess:
        print(sess.run(result))
