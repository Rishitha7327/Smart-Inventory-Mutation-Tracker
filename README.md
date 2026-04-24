### Day-9.py - Inventory Management & Copy Semantics

Demonstrates the differences between shallow and deep copying in Python through an inventory management system.

#### Features
- **Inventory Management**: Manages product information (laptops, phones)
- **Discount Application**: Applies percentage discounts and modifies stock
- **Copy Comparison**: Shows the difference between shallow and deep copies
- **Data Integrity Analysis**: Compares original vs modified data

#### Key Functions
- `create_inventory()`: Initializes product inventory
- `apply_discount(data, roll_number)`: Applies discounts and modifies stock
- `compare_data(original, modified)`: Counts changes between datasets

#### Usage
```bash
python Day-9.py
```
When prompted, enter your roll number for discount calculations.

#### Learning Outcome
This script illustrates:
- **Shallow Copy**: References nested objects; modifications affect both original and copy
- **Deep Copy**: Creates independent copies; modifications don't affect the original

---

## Installation

### Requirements
- Python 3.7+
- pip (Python package manager)

### Dependencies
Install required packages:
```bash
pip install numpy pandas matplotlib
```

Or install from requirements file (if available):
```bash
pip install -r requirements.txt
```

---

## How to Run

1. Navigate to the project directory:
```bash
cd path/to/python
```

2. Run any script:
```bash
python Day-6.py
python Day-9.py
```

3. Follow the on-screen prompts to provide input values.

---

## Technologies Used

- **NumPy**: Numerical computing and array operations
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **Python Standard Library**: `random`, `math`, `copy`

---

## Notes

- All student/inventory data is randomly generated
- Visualizations are displayed using Matplotlib
- Both scripts demonstrate fundamental Python concepts in data handling and object copying
