from kfp import dsl
from kfp.components import func_to_container_op, load_component_from_file
from kfp.compiler import Compiler

@func_to_container_op
def sample_output(output):
    print(output)

@dsl.pipeline(name='v=black-friday-sales-prediction')
def pipeline():
    copy_data = load_component_from_file("components/copy-data/copy-data.yml")
    # clean_data = load_component_from_file("components/clean-data/clean-data.yml")
    # feature_scale = load_component_from_file("components/feature-engineering/feature-engineering.yml")

    # component tasks
    copy_data_task = copy_data(output_data_uri="gs://black-friday-demo-bucket/demo/train/train.csv", output_sample_uri="gs://black-friday-demo-bucket/demo/sample/sample.csv")
    # clean_data_task = clean_data(copy_data_task.outputs["Dataset"])
    # feature_scale_task = feature_scale(clean_data_task.outputs["Data"])

Compiler().compile(pipeline, 'test.yml')