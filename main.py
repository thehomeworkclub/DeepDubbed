from elevenlabs import generate, stream, set_api_key
import os

set_api_key(os.environ['ELEVENLABS_API_KEY'])
