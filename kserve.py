
import kfp.compiler as compiler
import kfp.dsl as dsl
from kfp import components

kfserving_op = components.load_component_from_url('https://raw.githubusercontent.com/kubeflow/pipelines/master/components/kubeflow/kfserving/component.yaml')


@dsl.pipeline(
    name='KFServing pipeline',
    description='A pipeline for KFServing.'
)
def kfservingPipeline(
        action='apply',
        model_name='tensorflow-sample',
        model_uri='gs://black-friday-demo-bucket/model',
        namespace='anonymous',
        framework='sklearn'):
    kfserving_op(action=action,
                 model_name=model_name,
                 model_uri=model_uri,
                 namespace=namespace,
                 framework=framework)


if __name__ == '__main__':
    compiler.Compiler().compile(kfservingPipeline, __file__ + '.yml')