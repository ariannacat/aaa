# 🧬 Single-Cell RNA-Seq Classifier Pipeline for Hypoxia Detection

This repository contains the code for a thesis project evaluating the effectiveness and cost-efficiency of two single-cell RNA-Sequencing (scRNA-Seq) platforms—**Smart-Seq** and **Drop-Seq**—in detecting hypoxia, a clinically significant cancer phenotype.

## 📁 Repository Structure

- `Pipeline.ipynb` — Full workflow: preprocessing, binning, classification.
- `classifier.py` — Classifier tuning and evaluation functions.
- `data_utils.py` — Custom functions for dataset parsing and condition labeling.
- `preliminary_functions.py` — Early-stage preprocessing utilities.
- `requirements.txt` — Python packages with exact versions used.

## ⚠️ Data Privacy Notice

This project uses proprietary or confidential single-cell datasets, which **cannot be shared publicly** due to licensing and privacy restrictions.

To use this pipeline:
- Prepare your own Smart-Seq or Drop-Seq formatted data.
- Replace references to `df` or `clean_data_*` in the code with your own datasets.
- Structure your data similarly (see comments in `Pipeline.ipynb`).

## 🧠 Project Overview

Hypoxia detection in tumors could personalize cancer treatment and improve outcomes. This project compares:
- Two scRNA-Seq technologies (Smart-Seq, Drop-Seq)
- Two preprocessing methods (filtered-normalized vs raw-binned)
- Two classifiers (Elastic Net, XGBoost)

Results suggest that raw-binned data, particularly with Drop-Seq, can provide strong performance while significantly lowering costs.

## 📦 Installation

```bash
git clone https://github.com/ariannacat/scRNA-hypoxia-classifier.git
cd scRNA-hypoxia-classifier
pip install -r requirements.txt

