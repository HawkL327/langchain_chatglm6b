import os

import torch
import torch_mlu

# device config
EMBEDDING_DEVICE = "mlu" if torch.mlu.is_available(
) else "mps" if torch.backends.mps.is_available() else "cpu"
LLM_DEVICE = "mlu" if torch.mlu.is_available(
) else "mps" if torch.backends.mps.is_available() else "cpu"
num_mlus = torch.mlu.device_count()

# model cache config
MODEL_CACHE_PATH = os.path.join(os.path.dirname(__file__), 'model_cache')


# vector storage config
VECTOR_STORE_PATH='./vector_store'
COLLECTION_NAME='my_collection'


# init model config
#init_llm = "ChatGLM-6B-int8"
init_llm = "ChatGLM-6B"
init_embedding_model = "text2vec-base"

# model config
embedding_model_dict = {
    "ernie-tiny": "nghuyong/ernie-3.0-nano-zh",
    "ernie-base": "nghuyong/ernie-3.0-base-zh",
    "ernie-medium": "nghuyong/ernie-3.0-medium-zh",
    "ernie-xbase": "nghuyong/ernie-3.0-xbase-zh",
    "text2vec-base": "path to/text2vec-large-chinese",
    'simbert-base-chinese': 'WangZeJun/simbert-base-chinese',
    'paraphrase-multilingual-MiniLM-L12-v2': "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
}


llm_model_dict = {
    "chatglm": {
        "ChatGLM-6B": "path to/langchain/chatglm-6b",
        "ChatGLM-6B-int4": "THUDM/chatglm-6b-int4",
        "ChatGLM-6B-int8": "THUDM/chatglm-6b-int8",
        "ChatGLM-6b-int4-qe": "THUDM/chatglm-6b-int4-qe"
    },
    "belle": {
        "BELLE-LLaMA-Local": "/pretrainmodel/belle",
    },
    "vicuna": {
        "Vicuna-Local": "/pretrainmodel/vicuna",
    }
}