
# 🧠 AdaptGOT:

This repository provides the full workflow to reproduce the **AdaptGOT** model, including data preprocessing, graph construction, and model training. Please follow the instructions below to set up the environment and run the end-to-end pipeline.

---

### ⚙️ Environment Setup

Before running the project, please ensure that all required dependencies are correctly installed.  
We **strongly recommend** creating a clean virtual environment to avoid package conflicts.

### 🧮 Create and Activate a Virtual Environment

```bash
conda create -n adaptgot python=3.10 -y
conda activate adaptgot
```

### 🧱 Install the required packages:

```bash
pip install requirement.txt
```

### 🚀 Reproduction Steps

```bash
To reproduce the full process, please follow these steps carefully (using **`yelp_la`** as an example):
```

### 💡 Step 1. Preprocess the Raw Data

```bash
Run python3 preprocess.py.  
```

### ✨ Step 2: Load and Construct Graph Data

```bash
Run python3 load.py.  
```

### 🧩 Step 3: Train the AdaptGOT Model

```bash
python ourModel.py --emb_size 500 --vocab_size 30522 --num_epoch 100 --edge_feature_size 32
```
