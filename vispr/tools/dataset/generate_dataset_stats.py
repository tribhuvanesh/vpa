#!/usr/bin/python
"""Generate Dataset statistics.

Given a file containing a list of annotation paths, generate:
  a. general statistics Table 1
  b. data for Figure 2
"""
import json
import time
import pickle
import sys
import csv
import argparse
import os
import os.path as osp
import shutil

from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from scipy.misc import imread

from tools.common.utils import load_attributes
from tools import DS_ROOT

__author__ = "Tribhuvanesh Orekondy"
__maintainer__ = "Tribhuvanesh Orekondy"
__email__ = "orekondy@mpi-inf.mpg.de"
__status__ = "Development"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("anno_list", type=str, help="path to file containing annotation filepaths")
    parser.add_argument("out_tsv_path", type=str, help="path to write stats and extras")
    args = parser.parse_args()

    params = vars(args)
    # print 'Input parameters: '
    # print json.dumps(params, indent=2)

    attr_id_to_name, attr_id_to_idx = load_attributes()
    idx_to_attr_id = {v: k for k, v in attr_id_to_idx.iteritems()}
    attr_id_set = set(attr_id_to_idx.keys())
    attr_list = sorted(attr_id_set, key=lambda x: int(x.split('_')[0][1:]))

    image_labels_counts = []   # No. of labels per image
    n_images = 0

    attr_id_to_file_ids = defaultdict(list)
    with open(params['anno_list']) as anno_file:
        for line in anno_file:
            n_images += 1
            anno_path = osp.join(DS_ROOT, line.strip())

            with open(anno_path) as jf:
                anno = json.load(jf)

            image_labels_counts.append(len(anno['labels']))

            for attr_id in anno['labels']:
                assert attr_id in attr_id_set
                attr_id_to_file_ids[attr_id].append(anno['id'])

    print '# Images = ', n_images
    print '# Labels = ', np.sum(image_labels_counts)
    print 'Mean labels per image = ', np.mean(image_labels_counts)
    print 'Max images/label = ', np.max([len(v) for v in attr_id_to_file_ids.values()])
    print 'Min images/label = ', np.min([len(v) for v in attr_id_to_file_ids.values()])
    print 'Max label/image = ', np.max(image_labels_counts)
    print 'Min label/image = ', np.min(image_labels_counts)

    with open(params['out_tsv_path'], 'w') as outf:
        outf.write('{}\t{}\t{}\t{}\n'.format('idx', 'attribute_id', 'attribute_name', 'label_count'))
        for attr_id in attr_list:
            outf.write('{}\t{}\t{}\t{}\n'.format(attr_id_to_idx[attr_id], attr_id,
                                                 attr_id_to_name[attr_id], len(attr_id_to_file_ids[attr_id])))


if __name__ == '__main__':
    main()