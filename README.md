# tnbc-kg-app-1
first version
# 🧬 TNBC Clinical Trials Knowledge Graph (Subunit)

Welcome to the **TNBC Clinical Trials Subunit**, part of the larger **TNBC Knowledge Graph (KG Genie)** platform. This Streamlit app allows researchers, clinicians, and data scientists to explore **clinical trials**, **biotech/chemical drug classes**, **biomarkers**, and **targeted therapies** related to **Triple-Negative Breast Cancer (TNBC)**.

🔗 **Live App**: [tnbc-clinical-trial-subunit.streamlit.app](https://tnbc-clinical-trial-subunit.streamlit.app)
📦 **Source Code**: [GitHub Repo](https://github.com/Tamil1818/tnbc-kg-app-1)
---

## 🧠 What This App Does

- ✅ Visualizes TNBC-related clinical trial data as a **knowledge graph**
- ✅ Categorizes trials into **biotech**, **chemical**, and **other therapeutic classes**
- ✅ Links trials to:
  - Drug types
  - Biomarkers (e.g., BRCA1, PD-L1, TROP2)
  - Clinical phases and outcomes
- ✅ Supports interactive filtering by:
  - Drug category
  - Trial phase
  - Biomarker
- ✅ Exports graph images or filtered datasets 📦

---

## 📂 Files in This Repository

| File                          | Description                                             |
|-------------------------------|---------------------------------------------------------|
| `tnbc_clean.py`               | Main Streamlit app script                               |
| `tnbc_kg_triplets_*.csv`      | Preprocessed triplet-formatted knowledge graph data     |
| `requirements.txt`            | List of dependencies (for Streamlit Cloud deployment)   |
| `README.md`                   | This documentation file                                 |

---

## 📊 Dataset Overview

- **Trials Source**: [clinicaltrials.gov](https://clinicaltrials.gov)
- **Drug Categories**: Biotech, Chemical, Immuno, ADC, Antibody, RNA, etc.
- **Nodes**: Clinical Trials, Drugs, Conditions, Biomarkers
- **Relations**: USES, TARGETS, MEASURES, CLASSIFIED_AS

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/Tamil1818/tnbc-kg-app-1.git
cd tnbc-kg-app-1

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run tnbc_clean.py

