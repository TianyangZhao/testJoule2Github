"""Statistics tool for computing statistical measures over a list of numbers."""

import statistics as stats
from typing import List

from langchain_core.tools import tool


@tool
def statistics_calculator(numbers: List[float], measure: str) -> str:
    """Compute a statistical measure over a list of numbers.

    Args:
        numbers: List of numeric values (must have at least one element)
        measure: One of 'mean', 'median', 'mode', 'variance', 'stdev', 'min', 'max'

    Returns:
        Result as a descriptive string.
    """
    if not numbers:
        return "Error: The list of numbers is empty. Please provide at least one number."

    measure = measure.strip().lower()

    try:
        if measure == "mean":
            result = stats.mean(numbers)
            return f"Mean of {numbers} = {result}"
        elif measure == "median":
            result = stats.median(numbers)
            return f"Median of {numbers} = {result}"
        elif measure == "mode":
            result = stats.mode(numbers)
            return f"Mode of {numbers} = {result}"
        elif measure == "variance":
            if len(numbers) < 2:
                return "Error: Variance requires at least 2 numbers."
            result = stats.variance(numbers)
            return f"Variance of {numbers} = {result}"
        elif measure in ("stdev", "std", "standard_deviation"):
            if len(numbers) < 2:
                return "Error: Standard deviation requires at least 2 numbers."
            result = stats.stdev(numbers)
            return f"Standard deviation of {numbers} = {result}"
        elif measure == "min":
            result = min(numbers)
            return f"Minimum of {numbers} = {result}"
        elif measure == "max":
            result = max(numbers)
            return f"Maximum of {numbers} = {result}"
        else:
            return (
                f"Error: Unknown measure '{measure}'. "
                "Supported: mean, median, mode, variance, stdev, min, max."
            )
    except stats.StatisticsError as e:
        return f"Error: {e}"
