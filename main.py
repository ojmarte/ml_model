import pickle
import os

from pipeline import create_preprocessing_pipeline, create_feature_engineering_pipeline, create_ml_pipeline, prepare_submission
from nodes import download_s3_train_data, uploud_s3_model

BUCKET_NAME = 'titanic-models-bucket' # replace with your bucket name
KEY = 'data/'
KEY_MODEL = 'models/'

download_s3_train_data(BUCKET_NAME, KEY, "train.csv")

path = '/home/ec2-user/environment/ml_model/data'

train_path = path.split('/')
train_path.append('train.csv')
train_path = '/'.join(train_path)

# test_path = path.split('/')
# test_path.append('test.csv')
# test_path = '/'.join(test_path)

# submission_path = path.split('/')
# submission_path.append('submission.csv')
# submission_path = '/'.join(submission_path)

os.chdir(path)

train_df = create_preprocessing_pipeline(train_path, True)

features_df = create_feature_engineering_pipeline(train_df)

model, training_acc = create_ml_pipeline(features_df)

print('Model trained successfully, acc: ', training_acc)

pickle.dump(model, open(f'dt_classifier_acc_{round(training_acc)}', 'wb'))

uploud_s3_model(BUCKET_NAME, KEY_MODEL)

#submission_df = prepare_submission(model, test_path, submission_path)
#submission_df.head()
