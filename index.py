from kfp import dsl
from kfp.components import func_to_container_op, load_component_from_file
from kfp.compiler import Compiler

@dsl.pipeline(name='v=black-friday-v2')
def pipeline():
    copy_data = load_component_from_file("components/copydata/copydata.yml")

    # component tasks
    copy_data_task = copy_data()

Compiler().compile(pipeline, 'black-friday-v2.yml')