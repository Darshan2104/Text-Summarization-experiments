# Text-Summarization-experiments On News Data
This repo contains the experiments that I did as a part of my research work on Abstractive Text Summarization.

- [Hear](https://github.com/Darshan2104/Text-Summarization-experiments/tree/main/Scripts) is a script I used for training.
- [Here](https://github.com/Darshan2104/Text-Summarization-experiments/blob/main/Presentation%20of%20Research%20paper/CE137_Darshan_Tank_Reporting_Final.pdf) is a detailed report of the whole experiment.

**Tech stack:**
````
* Huggingface
* Adapter
* Datasets
````


## Experiments:


## **[1. Fine-tuning of PEGASUS model](PEGASUS)**

```
1. PEGASUS model is used for Abstractive summarization. This model was pre-trained with semi-supervised learning techniques like Gap Sentence Generation(GSG) and Mask Language modeling (MLM).
2. We fine-tuned it on the news dataset for the downstream task- Abstractive text summarization.
3. For only 100 records and that was also with a base model, it gave us a ROUGE score of ~21 (state of the art ~46 with the entire dataset).
```
- This was a part of my final year project [here](https://github.com/Darshan2104/Text-Summarization-experiments/tree/main/Presentation%20of%20Research%20paper) presentation. 


## **[2. Fine-tuning of T5 model and trained adapter](https://github.com/Darshan2104/Text-Summarization-experiments/tree/main/T5-small%20%2BAdapter(CNN))**

```
1. We fine-tuned T5-small and T5-base model on the supercomputer (param shavak).
2. Also we Trained Adapter for the same model and with the same dataset.
3. We also experimented summary to headline and text to headline generation.

- When both results were compared, it was almost similar, the thing was, for base model fine-tuning took around 22 days, and compared to the adapter took only 6 days!!
- text to headline was better compared to summary to headline.
```


