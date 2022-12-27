Experiment -1

Model : T5-small + Adapter(trained on CNN-Dailymail datasets)
Dataset : XLSum (english) test dataset(11,535)

Text  : Summary
Lable : Headline

Result : 

{'predict_gen_len': 17.9924,
 'predict_loss': 11.921663284301758,
 'predict_rouge1': 34.6128,
 'predict_rouge2': 13.1016,
 'predict_rougeL': 29.4834,
 'predict_rougeLsum': 29.6201,
 'predict_runtime': 1151.3351,
 'predict_samples_per_second': 10.019,
 'predict_steps_per_second': 2.505
 }

Observation : Reasult is good but in headline it is directly feaching sentences from the given text(in our case summary) as a headline output :(

