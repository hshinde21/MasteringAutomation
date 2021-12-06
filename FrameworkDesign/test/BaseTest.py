import pytest


@pytest.mark.usefixtures("log_on_failure", "beforeClass")
class BaseTest:
    pass
