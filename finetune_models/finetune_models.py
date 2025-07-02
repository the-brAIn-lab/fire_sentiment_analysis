import numpy as np
from datasets import DatasetDict, Dataset
from transformers import (AutoTokenizer, AutoModelSequenceClassification,
                          TrainingAruments, Trainer, DataCollatorWithPadding)
import evaluate
array = np.array([0,1])

print(array)