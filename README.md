# 🧠 AdaptGOT

## ⚙️ Environment Setup

Before running the project, please ensure that all dependencies are installed.  
We recommend creating a new virtual environment first:

```bash
conda create -n adaptgot python=3.10
conda activate adaptgot

Then install the required packages:
pip install requirement.txt

## 🚀 Reproduction Steps

To reproduce the full process, please follow these steps carefully (using **`yelp_la`** as an example):

### 🧩 Step 1. Preprocess the Raw Data

Run **`preprocess.py`**.  

Ensure your directories are organised as follows before execution:

model/
├── clean_data/
│   └── yelp/
│       └── yelp_la/
│           └── ...
├── raw_data/
│   └── yelp/
│       └── yelp_la/
│           └── (raw Yelp dataset files)
└── ...

Step 2: Load and Construct Graph Data

Run **`load.py`**.  

Step 3: Train the AdaptGOT Model

python ourModel.py --emb_size 500 --vocab_size 30522 --num_epoch 100 --edge_feature_size 32

