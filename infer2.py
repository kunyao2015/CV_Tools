import sys
import os
sys.path.append('../../tensorflow_toolkit')

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import cv2
import numpy as np
from utils.helpers import load_module
from lpr.trainer import decode_beams


def load_graph(frozen_graph_filename):
    with tf.gfile.GFile(frozen_graph_filename, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def)
    return graph


if __name__ == "__main__":

    path = "weight/graph.pb.frozen"
    image_path = "data/000005.png"
    image_path = "E:/deepLearning/Synthetic_Chinese_License_Plates/crops/000191.png"
    config_path = "chinese_lp/config.py"

    graph = load_graph(path)
    config = load_module(config_path)

    image = cv2.imread(image_path)
    img = cv2.resize(image, (94, 24))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.float32(img)
    img = np.multiply(img, 1.0/255.0)

    input = graph.get_tensor_by_name("import/input:0")
    output = graph.get_tensor_by_name("import/d_predictions:0")

    with tf.Session(graph=graph) as sess:
        results = sess.run(output, feed_dict={input: [img]})
    print(results)
    print(config.r_vocab)

    pred = decode_beams(results, config.r_vocab)
    print(pred)