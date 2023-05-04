# Tensor

A tensor is an N-dimensional array of data

|Common name|Rank (Dimensions)|Example|Shape of example|
|-|-|-|-|
|Scalar|0|x = tf.constant(3)|()|
|Vector|1|x = tf.constant([3,5,7])|(3)|
|Matrix|2|x = tf.constant([[3,5,7],[4,6,8]])|(2,3)|
|3D Tensor|3|x = tf.constant([[[3,5,7],[4,6,8]],[[1,2,3],[4,5,6]]])|(2,2,3)|
|nD Tensor|n|x = tf.constant([3,5,7],[4,6,8])|(2,3)|
|||x1 = tf.constant([2,3,4])|(3)|
|||x2 = tf.stack([x1, x1])|(2,3)|
|||x3 = tf.stack([x2, x2, x2, x2])|(4,2,3)|
|||x4 = tf.stack([x3,x3])|(2,4,2,3)|

* tf.constant produces constant tensors
* tf.Variable produces tensors that can be modified

```py
import tensorflow as tf

x = tf.constant([3,5,7],
                [4,6,8])

# slice
y = x[:,1]
-> [5,6]

# reshape turn our 2x3 into a 3x2
y = reshape(x, [3,2])

-> [[3,5]
    [7,4]
    [6,8]]

```

variables can change in value during time, i.e. training, they typically hold model weights
```py
import tensorflow as tf

# x <- 2
x = tf.Variable(2.0, dtype=tf.float32, name='my_var')

# x <- 48.5
x.assign(45.8)

# x <- x+4
x.assign_add(4)

# x <- x-3
x.assign_sub(3)

```