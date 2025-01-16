# What is this for?

This folder should be used to store configuration files used by Kedro or by separate tools.

This file can be used to provide users with instructions for how to reproduce local configuration with their own credentials. You can edit the file however you like, but you may wish to retain the information below and add your own section in the section titled **Instructions**.

## Local configuration

The `local` folder should be used for configuration that is either user-specific (e.g. IDE configuration) or protected (e.g. security keys).

> *Note:* Please do not check in any local configuration to version control.

## Base configuration

The `base` folder is for shared configuration, such as non-sensitive and project-related configuration that may be shared across team members.

WARNING: Please do not put access credentials in the base configuration folder.

## Find out more
You can find out more about configuration from the [user guide documentation](https://docs.kedro.org/en/stable/configuration/configuration_basics.html).


Migration from Kedro-Viz Native Experiment Tracking to Kedro-Mlflow 

| **Kedro-Viz Dataset Type**           | **MLflow Dataset Type**        | **Configuration Details**                       |
|--------------------------------------|---------------------------------|------------------------------------------------|
| `tracking.MetricsDataset`           | `MlflowMetricDataset`          | No additional configuration needed.            |
| `tracking.JSONDataset`              | `MlflowArtifactDataset`        | Wrap within `MlflowArtifactDataset` and configure as `json.JSONDataset`. |
| `plotly.plotlyDataset`              | `MlflowArtifactDataset`        | Wrap within `MlflowArtifactDataset`.           |
| `plotly.JSONDataset`                | `MlflowArtifactDataset`        | Wrap within `MlflowArtifactDataset`.           |
| `matplotlib.MatplotlibWriter`       | `MlflowArtifactDataset`        | Wrap within `MlflowArtifactDataset`.           |
