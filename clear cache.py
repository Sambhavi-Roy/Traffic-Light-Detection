import gc
import torch

# Clear cache memory
gc.collect()
torch.cuda.empty_cache()
