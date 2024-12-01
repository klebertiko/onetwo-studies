from onetwo import ot
from onetwo.builtins import llm
from onetwo.backends import openai_api
import os

# Confirm the currently installed OneTwo version.
print(f'Running OneTwo v{ot.__version__}.')

backend.register()
print('Backend registered.')
