# AdaptGOT

To reproduce the full process, please follow these steps: first, run preprocess.py before execution, make sure to create the directories model/clean_data/yelp/yelp_la and model/raw_data/yelp/yelp_la (taking yelp_la as an example), and place the raw dataset files into model/raw_data/yelp/yelp_la/; this step will generate occ_mat.npy. 

Next, run load.py to process the cleaned data and produce data.pt, which is required for training. 

Finally, train the model by running the following command:

python ourModel.py --emb_size 500 --vocab_size 30522 --num_epoch 100 --edge_feature_size 32
