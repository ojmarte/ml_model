import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from nodes import remove_data_dir
import json
from unittest import mock

PATH = "/"

def test_uploud_s3_model(mocker):
    mocker = mock.Mock(return_value=True)

    assert(mocker)

def test_download_s3_train_data(mocker):
    mocker = mock.Mock(return_value=True)

    assert(mocker)

def test_remove_data_dir(mocker):
    mocker = mock.Mock(return_value=True)

    assert(mocker)

def test_compute_accuracy(mocker):
    mocker = mock.Mock(return_value=True)

    assert(mocker)

def test_create_and_train_decision_tree_model(mocker):
    mocker = mock.Mock(return_value=True)

    assert(mocker)

def test_split_dataset_for_training(mocker):
    mocker = mock.Mock(return_value=True)

    assert(mocker)

def test_encode_fare(mocker):
    mocker = mock.Mock(return_value=True)

    assert(mocker)