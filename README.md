# Sentence Clustering with BERT

This Python script reads text files, generates sentence embeddings using the BERT model, and clusters the sentences using the K-Means algorithm.

## Dependencies

The script requires several Python libraries including numpy, pandas, sentence_transformers, sklearn, matplotlib, and tkinter. Don't worry about manually installing these dependencies. When you run the script using the provided command, all necessary dependencies will be automatically installed.


Place your text files in a directory named "text" in the same location as the script. The script will read all the text files, split the text into sentences, and remove any sentences that are less than 5 characters long.


## Usage

Running the script is as simple as executing the following command in your terminal:

```bash

 git clone https://github.com/mendeltem/sentence_cluster.git
 cd sentence_cluster
 
 pip install -r requirements  or  pip3 install -r requirements

python sentence_tokenizer.py or python3 sentence_tokenizer.py

```

Once you execute the run command, the script will perform the following steps:

Read all text files in the "text" directory.
Split the text into sentences and filter out any sentences that are less than 5 characters long.
Generate embeddings for each sentence using the 'bert-base-nli-mean-tokens' model.
Determine the optimal number of clusters for the K-Means algorithm using the Elbow Method.
Display a plot of the inertia values for different numbers of clusters. You will be prompted to enter the optimal number of clusters in a text box. This is shown in the image below:

![Alt text](/image/cluster.png)

Perform K-Means clustering on the sentence embeddings and group the sentences by their cluster labels.
Save the sentences and their corresponding cluster labels to an Excel file named "clusters.xlsx".


The script uses the 'bert-base-nli-mean-tokens' model to generate embeddings for each sentence. It then uses the Elbow Method to determine the optimal number of clusters for the K-Means algorithm.


The script will display a plot of the inertia values for different numbers of clusters. Enter the optimal number of clusters in the text box and click "Submit".

The script will then perform K-Means clustering on the sentence embeddings and group the sentences by their cluster labels. The sentences and their corresponding cluster labels are saved to an Excel file named "clusters.xlsx".

## Author

This script was created by mendeltem on June 13, 2023.

## Lizenz
MIT, Apache2, GPL-3, oder keine angeben, dann ist All rights reserved.
