from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core import Environment
from azureml.core import ScriptRunConfig

if __name__ == "__main__":
    #Connect to Azure ML WorkSpace
    ws = Workspace.from_config(path='./.azureml',_file_name='config.json')

    #Experiment
    experiment = Experiment(workspace=ws, name='day2-experiment-train-titanic')
    config = ScriptRunConfig(source_directory='./src',
                             script='titanic-model.py',
                             compute_target='cpu-cluster')

    # set up pytorch environment
    env = Environment.from_conda_specification(
        name='sklearn-env',
        file_path='./.azureml/sklearn-env-aml.yml'
    )

    config.run_config.environment = env

    #Execute experiment
    run = experiment.submit(config)

    #Print url
    aml_url = run.get_portal_url()
    print(aml_url)