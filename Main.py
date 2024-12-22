from typing import Tuple


class ADCRepresentation:
    def __init__(self):
        """
        Initializes the ADCRepresentation instance with user-defined bit resolution and voltage range.
        Asks user to input the number of bits (bit_depth) and the minimum and maximum voltages.
        Computes the voltage step size (step_voltage) based on these inputs.
        """
        self.bit_depth: int = int(input("Enter number of bits for ADC resolution: "))

        # Ensuring that voltage inputs are captured and processed correctly
        try:
            voltage_range: Tuple[float, float] = tuple(
                map(float, input("Enter Minimum and Maximum Voltage Range (separated by space): ").split()))
            if len(voltage_range) != 2:
                raise ValueError("You must enter exactly two float numbers separated by a space.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            exit(1)

        self.max_voltage, self.min_voltage = max(voltage_range), min(voltage_range)

        # Calculate the voltage resolution step size
        self.step_voltage: float = (self.max_voltage - self.min_voltage) / (2 ** self.bit_depth)

    def display_voltages(self):
        """Displays the voltage references and their corresponding binary codes for all possible ADC output values."""
        current_step: float = 0
        for index in range(2 ** self.bit_depth):
            print(f"Index: {index}, Voltage Reference: {current_step + self.min_voltage:.2f} V, Binary: {index:0{self.bit_depth}b}")
            current_step += self.step_voltage
        print(f"Max Quantization Error is {self.step_voltage / 2:} V")
        print('-' * 100)

    def convert_voltage(self):
        """Converts an input voltage to its closest digital representation based on the ADC resolution."""
        try:
            input_voltage: float = float(input("Enter the input voltage: "))
        except ValueError:
            print("Invalid input! Please enter a valid floating-point number.")
            return

        if input_voltage < self.min_voltage or input_voltage > self.max_voltage:
            print("Error: Input voltage is out of range. ADC simulation failed.")
            return

        # Calculating digital value more accurately by rounding to the nearest code
        digital_value: int = round((input_voltage - self.min_voltage) / self.step_voltage)
        digital_value = min(digital_value, 2 ** self.bit_depth - 1)  # Cap the value to the maximum representable value
        corresponding_voltage: float = self.min_voltage + digital_value * self.step_voltage
        quantization_error: float = abs(input_voltage - corresponding_voltage)  # Using absolute value for error

        print(f"Digital Representation: {digital_value:0{self.bit_depth}b}")
        print(f"Closest Voltage Reference: {corresponding_voltage} V")
        print(f"Quantization Error: {quantization_error} V")


def main():
    """Main function to create an instance of ADCRepresentation and invoke its methods."""
    adc = ADCRepresentation()
    # adc.display_voltages()  # (Optional) Display all possible voltage levels and their corresponding binary representations
    adc.convert_voltage()  # Convert a user-input voltage to its nearest digital equivalent and display the result


if __name__ == '__main__':
    main()
