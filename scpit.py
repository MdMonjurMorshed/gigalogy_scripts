import requests

user_credentials = {
    "email": "monjur.morshed@gigalogy.com",
    "password": "!*TAhi111275*!"
}

BACKEND_URL = "http://localhost:8080"
PERSONALIZE_URL = "http://localhost:8092"

models = [
    {
        "name": "gpt-4o-2024-08-06",
        "provider": "openai",
        "supported_token_size": 128000,
        "max_output_token_size": 16384,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "Control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": True,
        "is_vision_supported": True
    },
    {
        "name": "gpt-4o-2024-05-13",
        "provider": "openai",
        "supported_token_size": 128000,
        "max_output_token_size": 4096,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "Control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": True,
        "is_vision_supported": True
    },
    {
        "name": "gpt-4o-mini-2024-07-18",
        "provider": "openai",
        "supported_token_size": 128000,
        "max_output_token_size": 16384,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "Control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": True,
        "is_vision_supported": True
    },
    {
        "name": "gpt-4o-mini",
        "provider": "openai",
        "supported_token_size": 128000,
        "max_output_token_size": 16384,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "Control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": True,
        "is_vision_supported": True
    },
    {
        "name": "gpt-4-turbo-2024-04-09",
        "provider": "openai",
        "supported_token_size": 128000,
        "max_output_token_size": 4096,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "Control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": True,
        "is_vision_supported": True
    },
    {
        "name": "gpt-4-vision-preview",
        "provider": "openai",
        "supported_token_size": 128000,
        "max_output_token_size": 4096,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "top_p",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": False,
        "is_vision_supported": True
    },
    {
        "name": "gpt-4-0125-preview",
        "provider": "openai",
        "supported_token_size": 128000,
        "max_output_token_size": 4096,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "Control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": False,
        "is_vision_supported": False
    },
    {
        "name": "gpt-4-1106-preview",
        "provider": "openai",
        "supported_token_size": 128000,
        "max_output_token_size": 4096,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "Control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": False,
        "is_vision_supported": False
    },
    {
        "name": "gpt-3.5-turbo-1106",
        "provider": "openai",
        "supported_token_size": 16385,
        "max_output_token_size": 4096,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "Control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": True,
        "is_vision_supported": False
    },
    {
        "name": "gpt-3.5-turbo-16k-0613",
        "provider": "openai",
        "supported_token_size": 16385,
        "max_output_token_size": 16385,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "Control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": False,
        "is_vision_supported": False
    },
    {
        "name": "gpt-3.5-turbo-instruct",
        "provider": "openai",
        "supported_token_size": 4096,
        "max_output_token_size": 4096,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "Control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": False,
        "is_vision_supported": False
    },
    {
        "name": "gpt-3.5-turbo-0613",
        "provider": "openai",
        "supported_token_size": 4096,
        "max_output_token_size": 4096,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "Control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": False,
        "is_vision_supported": False
    },
    {
        "name": "gpt-3.5-turbo-0125",
        "provider": "openai",
        "supported_token_size": 16385,
        "max_output_token_size": 4096,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "Control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": True,
        "is_vision_supported": False
    },
    {
        "name": "gpt-4-0613",
        "provider": "openai",
        "supported_token_size": 8192,
        "max_output_token_size": 8192,
        "hyperparams": {
            "temperature": {
                "type": "float",
                "default": 0.0,
                "example": 0.0,
                "description": "control randomness",
                "required": True,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            },
            "top_p": {
                "type": "float",
                "default": 1.0,
                "example": 1.0,
                "description": "Nucleus sampling probability",
                "required": False,
                "min": None,
                "max": None,
                "min_items": None,
                "max_items": None
            }
        },
        "inference_api": None,
        "is_json_supported": False,
        "is_vision_supported": False
    }
]



def get_access_token():
    url = "/v1/oauth2/token?grant_type=password"
    payload = user_credentials
    headers = {
        "X-Client-Id": "rl159dZdf2SSuGwamUW7dJHs",
        "X-Client-Secret": "PgcQfywapbUfARniX0cHiZoxtivt26AGv340tNcMWJ7bQPwJ"
    }
    response = requests.post(f"{BACKEND_URL}{url}", headers=headers, json=payload)
    print(response.json()["access_token"])
    return response.json()["access_token"]


def create_models():
    token = get_access_token()
    url = "/v1/gpt/models"
    headers = {
        "Auth-token": f"{token}",
        "X-Client-Id": "rl159dZdf2SSuGwamUW7dJHs",
        "X-Client-Secret": "PgcQfywapbUfARniX0cHiZoxtivt26AGv340tNcMWJ7bQPwJ"
    }
    for model in models:
        response = requests.post(url=f"{PERSONALIZE_URL}{url}", headers=headers, json=model)
        if response.status_code != 201:
            print(response.status_code)
            print(response.json())
        else:
            print(f"model created {model['name']}")


print("Start creating models")
create_models()
print("Finished creating models")