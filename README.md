# ADC Representation and Conversion

This repository contains a Python program for simulating an Analog-to-Digital Converter (ADC). The program allows you to specify the ADC resolution, define a voltage range, and simulate the ADC’s behavior, including quantization and digital value representation.

## Features
- **Voltage Representation**: Display all possible voltage levels and their corresponding binary representations based on the specified ADC resolution.
- **Voltage Conversion**: Convert a user-input voltage to its closest digital equivalent, showing the corresponding voltage reference and quantization error.

## How It Works
1. The user inputs the number of bits for the ADC resolution.
2. The user defines the minimum and maximum voltage range for the ADC.
3. The program calculates the step size and displays all possible voltage levels and their binary representations.
4. The user provides an input voltage to be converted, and the program outputs the corresponding binary value, the closest voltage reference, and the quantization error.

## Screenshots

### Display Voltage Levels and Conversion Results
![Voltage Representation](https://github.com/user-attachments/assets/8a617f26-271e-48af-ad17-a1e592b89feb)
### Conversion of Input Voltage
![Input Voltage Conversion](https://github.com/user-attachments/assets/b55e2f86-7e66-4833-b43f-92b927a12ab2)

## Code Snippet
```python
adc.display_voltages()  # Display voltage levels and their binary equivalents
adc.convert_voltage()   # Convert user-input voltage and display results
```

## How to Run
1. Clone this repository.
2. Ensure you have Python 3.11 or later installed.
3. Run the script using the command:
   ```bash
   python3 Representation.py
   ```
4. Follow the prompts to provide the required inputs.

## Requirements
- Python 3.11+
