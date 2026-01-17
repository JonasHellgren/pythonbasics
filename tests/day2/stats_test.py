import math
import pytest
from src.day_two.Stats import Stats  # ändra importväg efter din fil

def test_summary_returns_expected_keys_and_values():
    s = Stats((1, 2, 3, 4))
    summary = s.summary()

    assert set(summary.keys()) == {"min", "avg", "max", "std"}
    assert summary["min"] == 1
    assert summary["max"] == 4
    assert summary["avg"] == 2.5

    # std (population): sqrt(((1-2.5)^2 + ...)/4) = sqrt(1.25)
    assert math.isclose(summary["std"], math.sqrt(1.25), rel_tol=1e-12, abs_tol=1e-12)

def test_raises_on_empty_tuple():
    with pytest.raises(ValueError):
        Stats(())

def test_raises_on_non_tuple():
    with pytest.raises(TypeError):
        Stats([1, 2, 3])

def test_raises_on_non_numeric():
    with pytest.raises(TypeError):
        Stats((1, "2", 3))
