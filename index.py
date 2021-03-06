from kfp import dsl
from kfp.components import load_component_from_file, load_component_from_url
from kfp.compiler import Compiler

@dsl.pipeline(name='v=black-friday-v2')
def pipeline():
    copy_data = load_component_from_file("components/copy-data/copy-data.yml")
    clean_data = load_component_from_file("components/clean-data/clean-data.yml")
    feature_scale = load_component_from_file("components/feature-engineering/feature-engineering.yml")
    linear_regression = load_component_from_file("components/linear-regression/train/linear-regression.yml")
    linear_regression_test = load_component_from_file("components/linear-regression/test/linear-regression-test.yml")
    linear_regression_predict = load_component_from_file("components/linear-regression/predict/linear-regression-predict.yml")

    # component tasks
    copy_data_task = copy_data()
    clean_data_task = clean_data(copy_data_task.outputs["Dataset"])
    feature_scale_task = feature_scale(clean_data_task.outputs["Data"])
    linear_regression_task = linear_regression(feature_scale_task.outputs["X Train"], feature_scale_task.outputs["Y Train"])
    linear_regression_test_task = linear_regression_test(feature_scale_task.outputs["X Test"], feature_scale_task.outputs["Y Test"], linear_regression_task.outputs["Linear Regression Model"])
    linear_regression_predict_task = linear_regression_predict(clean_data_task.outputs["Label Encoder Object"], clean_data_task.outputs["Column Transformer Object"], feature_scale_task.outputs["Standard Scaler Object"], linear_regression_task.outputs["Linear Regression Model"])

Compiler().compile(pipeline, 'black-friday-v2.yml')