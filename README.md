# Healthcare Data Validation Framework

## 📌 Overview

This project simulates a real-world ETL pipeline and implements a data validation framework to ensure data quality before loading into downstream systems.

The framework validates healthcare data using Python, Pandas, and Pytest with a scalable, config-driven approach.

---

## 🧠 Problem Statement

In real-world data pipelines, poor data quality (nulls, duplicates, invalid values) can lead to incorrect analytics and business decisions.

This project ensures:

- Clean and reliable data
- Automated validation before data consumption

---

## 🏗️ Architecture

Raw Data (CSV) → Transformation → Processed Data → Validation (Pytest) → CI/CD Pipeline

---

## ⚙️ Tech Stack

- Python
- Pandas
- Pytest
- Pytest Fixtures
- GitHub Actions (CI/CD)

---

## 🔄 Workflow

1. Load raw healthcare dataset
2. Perform transformation:
   - Remove null values
   - Remove duplicates
   - Apply business rules

3. Save processed dataset
4. Run automated validation tests
5. Execute pipeline via CI/CD

---

## 🧪 Validation Checks

- Null value validation
- Duplicate record validation
- Business rule validation (e.g., age > 0)
- Config-driven validation using JSON

---

## 📂 Project Structure

```
healthcare-data-validation-framework/
│
├── config/
├── data/
│   ├── raw/
│   ├── processed/
├── src/
│   ├── transformation/
│   ├── validation/
├── tests/
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
python src/transformation/transform_data.py
pytest
```

---

## ⚡ CI/CD Integration

- Automated pipeline using GitHub Actions
- Runs on every code push
- Executes:
  - Dependency installation
  - Data transformation
  - Validation tests

---

## 💡 Key Highlights

- Config-driven validation framework
- Reusable pytest fixtures
- End-to-end ETL testing simulation
- CI/CD integration for automated testing

---

## 🚀 Future Enhancements

- Integration with PostgreSQL / Snowflake
- Data reconciliation (source vs target)
- Dashboard for validation reports

---

## 👤 Author

Surendra Kumar
