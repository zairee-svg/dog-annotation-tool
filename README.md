# Zaire's Python Portfolio

Aspiring Data Annotator & Python Developer focused on AI training data, data labeling, and annotation workflows.

Building practical Python tools to practice real-world workflows used by leading AI training companies like CloudFactory and Scale AI.

## 🛠️ Skills

- **Python** - CLI tools, input validation, file handling
- **Data Annotation** - Image labeling, bounding boxes, occlusion, attributes
- **CSV Handling** - Saving, structuring, and validating labeled data
- **Attention to Detail** - Consistent labels, clean data, quality checks
- **GitHub** - Repos, README documentation, version control

---

## 🐶 Project 1: Dog Annotation Tool

A CLI tool that collects dog annotations and saves them to CSV.

**File:** `dog_annotator.py`

**How to run:** `python dog_annotator.py`

**What it does:**
- Asks for Dog ID, Breed, Color, Size
- Helper function `get_input()` validates every answer - won't accept empty input
- Validates Size must be small / medium / large
- Appends to `dogs.csv` - never wipes previous annotations
- Creates `dogs.csv` with headers only if the file doesn't exist yet
- Type `quit` to stop
- ---

## 🚗 Project 2: Car Detection Annotation

- **Project:** Car Detection Annotation
- **Tool:** MakeSense.ai
- **Task:** Drew bounding boxes around every car in 4 street images
- **Output:** Exported in YOLO format (.txt files) ready for AI model training
- **Skills:** Attention to detail, bounding box annotation, quality check

Note: Annotations were created in MakeSense.ai. YOLO export files are included in this repo.
---

## 🧮 Bonus Project: Python Calculator

A simple CLI calculator to practice Python basics - input handling, validation, and functions.

**File:** `calc.py`

**How to run:** `python calc.py`

**What it does:**
- Addition, subtraction, multiplication, division
- Handles invalid input without crashing
