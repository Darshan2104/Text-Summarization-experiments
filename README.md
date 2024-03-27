# Text-Summarization-experiments On News Data
This repo contains the experiemensts which i did as a part of my research work on Abstractive Text Summarization.

**Tech stack:**
````
* Huggingface
* Adapter
* Datasets
````


## Experiments:


## **(1. Fine-tuning of PEGASUS model)[]**

```
1. PEGASUS model is used for Abstractive summarization. This model was pre-trained with semi-supervised learning technique like Gap Sentence Generation(GSG) and Mask Language Modelinng(MLM).
2. We fine-tuned it on news dataset for the down stream task- Abstractive text summarization.
3. For only 100 records and that was also with base model, it gave us ROUGE score of ~21 (state of the art ~46 with entire dataset).

This for a part of my final year project (here)[] is presentation. 
```

## **(2. Fine-tuning of T5 model and trained adapter)[]**

```
1. We fine-tuned T5-small and T5-base model on super computer (param shavak).
2. Also we Trained Adapter for the same model and with the same dataset.

- When both results were compared, it was almost simmiler, thing was, for base model fine-tuning took around 22days and compared to that adapter took only 6 days!!1

(Here)[] is a script I used for training.
(Here)[] is a detailed report of whole experiment.
```