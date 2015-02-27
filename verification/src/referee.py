from checkio_referee import RefereeBase
from checkio_referee.covercode import py_unwrap_args

import settings
import settings_env
from tests import TESTS


unwrap_str_cover = """def cover(func, data):
    return func(*[str(x) for x in data])
"""


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "count_reports"
    ENV_COVERCODE = {
        "python_2": unwrap_str_cover,
        "python_3": py_unwrap_args,
        "javascript": None
    }
