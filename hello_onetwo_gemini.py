from onetwo import ot
from onetwo.builtins import llm
from onetwo.backends import gemini_api
import os

# Confirm the currently installed OneTwo version.
print(f'Running OneTwo v{ot.__version__}.')

if not 'GEMINI_API_KEY' not in os.environ:
  raise ValueError(
      'The api key must be specified either here or in the environment.')

model_name = 'GEMINI_PRO'  # Specify the model of your choice.

# Create and register a connection to the Gemini backend.
backend = gemini_api.GeminiAPI(
    api_key=os.environ["GEMINI_API_KEY"],
    temperature=0.0,
    max_retries=12,
    cache_filename=get_cache_path(model_name, temperature=0.0),
)
backends[model_name] = backend
backend.register()
print('Gemini API backend registered.')
