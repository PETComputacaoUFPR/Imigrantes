# Inventory System GUI

This project is a simple inventory management system with a graphical user interface (GUI). It allows users to register products, list available products, and sell products while maintaining the original logic for inventory management.

## Project Structure

```
inventory-system-gui
├── src
│   ├── main.py               # Entry point for the application
│   ├── inventory_logic.py     # Contains the logic for managing inventory
│   ├── gui.py                 # Implements the graphical user interface
│   └── utils.py               # Contains utility functions
├── assets
│   └── generic.png            # Placeholder image for the GUI
├── README.md                  # Documentation for the project
└── requirements.txt           # Lists project dependencies
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd inventory-system-gui
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Use the GUI to:
   - Register new products
   - View the list of products
   - Sell products from the inventory

## Dependencies

This project requires the following Python libraries:
- Tkinter (or PyQt, depending on the implementation in `gui.py`)
- Any other libraries specified in `requirements.txt`

## License

This project is licensed under the MIT License. See the LICENSE file for more details.