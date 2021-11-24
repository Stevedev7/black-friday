from kfp import dsl
from kfp.components import func_to_container_op, load_component_from_file
from kfp.compiler import Compiler

@dsl.pipeline(name='v=black-friday-v2')
def pipeline():
    copy_data = load_component_from_file("components/copydata/copydata.yml")
    clean_data = load_component_from_file("components/clean-data/clean_data.yml")

    # component tasks
    copy_data_task = copy_data()
    clean_data_task = clean_data(copy_data_task.outputs["Dataset"])
    print(copy_data_task.outputs["Dataset"])
Compiler().compile(pipeline, 'black-friday-v2.yml')