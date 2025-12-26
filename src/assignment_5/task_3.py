"""Function for numpy array value mapping."""

import math

import numpy as np
from sklearn.datasets import load_iris  # type: ignore


def get_dictionary_mapping(
    data: np.ndarray, feature_names: list[str]
) -> list[dict[str, np.float64]]:
    """Map the normalized value to the features.

    Args:
        data: 2D numpy array data.
        feature_names: Feature names for the numpy array.

    Returns:
        The normalized value mapped to the feature.
    """
    means = {i: sum(data[:, i]) / len(data) for i in range(data.shape[1])}  # type: ignore

    std_deviations = {
        i: math.sqrt((sum([(x - means.get(i)) ** 2 for x in data[:, i]])) / (len(data) - 1))  # type: ignore
        for i in range(data.shape[1])  # type: ignore
    }

    dict_map = [
        {
            feature_names[i]: ((item[i] - means[i]) / std_deviations[i])
            for i in range(data.shape[1])  # type: ignore
        }
        for item in data
    ]
    return dict_map


if __name__ == "__main__":
    iris = load_iris()
    data = iris.data  # type: ignore
    feature_names = iris.feature_names  # type: ignore
    print(type(data))
    print(get_dictionary_mapping(data, feature_names))
