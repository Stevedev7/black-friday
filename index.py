import kfp
from kfp import dsl
from kfp.components import func_to_container_op

@func_to_container_op
def show_results(var):
    print(var)

@dsl.pipeline(name="Black Friday Sales Prediction")
def pipeline():
    download = kfp.components.load_component_from_file("download_data/download_data.yml")
    clean_data = kfp.components.load_component_from_file("clean_data/clean_data.yml")


    download_component = download()
    clean_data_component = clean_data(download_component.outputs["Sample"], download_component.outputs["Dataset"])
    show_results(clean_data_component.outputs["Data"])    

kfp.compiler.Compiler().compile(pipeline, 'black-friday-sales-prediction.yml')

