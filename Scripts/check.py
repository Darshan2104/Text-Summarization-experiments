from transformers import AutoModelForSeq2SeqLM
import pickle

# add path of the 't5-base-finetuned' model
PATH = ''
model = AutoModelForSeq2SeqLM.from_pretrained(PATH)
pickle.dump(model, open("t5-base.pkl","wb"))
