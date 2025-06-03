# learn-OpenShift-AI
This repository documents a hands-on learning project for OpenShift AI.  
The goal is to build and deploy a lightweight machine learning workflow using **Tekton Pipelines** on OpenShift AI.

## 🚀 Project Overview

The project demonstrates a basic ML pipeline with the following stages:

1. **Data Preprocessing** (CSV-based tabular data)
2. **Model Training** (Scikit-learn classifier)
3. **(Optional) Model Evaluation**
4. **Model Testing via a Frontend** (planned: Streamlit)
5. **CI/CD with Tekton Pipelines** (no GitHub Actions involved)

Due to sandbox limitations, lightweight data and models are used.

## 📦 ML Pipeline Logic

### 🧼 Preprocessing
- Clone the repo into a subfolder in the shared workspace.
- Run `data/preprocess.py`, which:
  - Loads a seaborn dataset (e.g. Titanic)
  - Prepares `X_train`, `X_test`, `y_train`, `y_test`
  - Saves them as CSVs to `data/`

### 🧠 Training
- Loads the CSVs from `data/`
- Trains a basic classifier (e.g., `RandomForestClassifier`)
- Saves the model artifact to `models/`

---

## 🔁 Tekton Pipeline Details

### Tasks:
- **`preprocess-task`**:  
  Clones the repo and runs the preprocessing script.

- **`train-task`**:  
  Installs dependencies and runs the training script.

### Pipeline:
- Defined in `openshift/pipeline.yaml`
- Uses a shared PVC (`volumeClaimTemplate`) for communication between tasks.
- Tasks are chained: `preprocess → train`

### PipelineRun:
- Defined in `openshift/pipelinerun.yaml`
- Includes:
  - Reference to the pipeline
  - Shared workspace using `volumeClaimTemplate`
  - Service account: `pipeline`

---

## 🧪 How to Run

> Prerequisite: Logged in to OpenShift CLI, using the correct project.
chmod -x oc_apply.sh
bash oc_apply.sh


## ✅ Next Steps
Finalize and deploy a Streamlit frontend (app/) to visualize predictions
Expose it via OpenShift Route
Add a Tekton step to build and push the model or app image to Quay.io
Tag and version models for reproducibility