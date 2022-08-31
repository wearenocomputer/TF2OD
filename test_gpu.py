#https://stackoverflow.com/questions/71000120/colab-0-unimplemented-dnn-library-is-not-found
#https://practicaldatascience.co.uk/machine-learning/how-to-test-your-keras-cuda-cudnn-tensorflow-install

import tensorflow as tf
tf.test.is_built_with_cuda()
tf.config.list_physical_devices('GPU')
