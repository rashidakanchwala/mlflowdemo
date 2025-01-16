from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model, split_data, train_model, calculate_mae, calculate_max_error, calculate_r2_score


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["model_input_table", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="regressor",
                name="train_model_node",
            ),
            node(
                func=lambda regressor, X_test: regressor.predict(X_test),
                inputs=["regressor", "X_test"],
                outputs="y_pred",
                name="predict_node",
            ),
            node(
                func=calculate_r2_score,
                inputs=["y_test", "y_pred"],
                outputs="r2_score",
                name="calculate_r2_score_node",
            ),
            node(
                func=calculate_mae,
                inputs=["y_test", "y_pred"],
                outputs="mae",
                name="calculate_mae_node",
            ),
            node(
                func=calculate_max_error,
                inputs=["y_test", "y_pred"],
                outputs="max_error",
                name="calculate_max_error_node",
            ),
            node(
                func=evaluate_model,
                inputs=["regressor", "X_test", "y_test"],
                name="evaluate_model_node",
                outputs="metrics",
            ),
        ]
    )
