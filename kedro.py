from kedro.pipeline import Pipeline, node
from kedro.runner import SequentialRunner
from kedro.io import DataCatalog

# 1. Node function
def create_messages():
    import pandas as pd
    return pd.DataFrame({"message": ["hello", "world"]})

# 2. Pipeline definition
pipeline = Pipeline([
    node(
        func=create_messages,
        inputs=None,  # No inputs
        outputs="msgs_df",
        name="create_messages_node"
    )
])

# 3. Run it
catalog = DataCatalog()
runner = SequentialRunner()
result = runner.run(pipeline=pipeline, catalog=catalog)

print(result["msgs_df"])


"""
proba = model.predict_proba(X)          # shape: (n_samples, 2)
p1 = proba[:, 1]                        # probability of class 1 (if classes_ = [0,1])
y_pred = (p1 >= 0.7).astype(int)        # threshold = 0.7 (example)
"""
