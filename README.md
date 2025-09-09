# Precision and Recall

This repository contains a simple Python script to calculate **precision** and **recall** for information retrieval tasks.
It demonstrates how to evaluate query results against a set of relevant documents.

---

## 📌 Features

* Calculates **precision** and **recall** for multiple queries.
* Uses Python sets for efficient intersection of answer and relevant sets.
* Provides a clear, formatted output for each query.

---

## 📂 File Structure

```
.
├── precisionrecall.py   # Main script to run precision & recall calculations
```

---

##⚙️ How It Works

The script:

1. Defines a `calculate_metrics()` function that computes precision and recall:

   * **Precision** = TP / (TP + FP)
   * **Recall** = TP / (TP + FN)
     where TP = true positives, FP = false positives, FN = false negatives.
2. Runs a set of example queries with pre-defined answer and relevant sets.
3. Prints results for each query.

---

## ▶️ Usage

### Run the script

```bash
python precisionrecall.py
```

### Example Output

```
Multiple Queries

Query: q1
    Precision:  0.25
    Recall:     0.50

Query: q2
    Precision:  0.67
    Recall:     0.50

Query: q3
    Precision:  1.00
    Recall:     0.50
```

---

## 🛠️ Requirements

* Python 3.6+
  (No external libraries required.)

---
