import tensorflow as tf
data1 = tf.constant(2,dtype=tf.int32)
session = tf.Session()
print(data1)
print(session.run(data1))
