# CarVitals using OBD-II 🚗

**CarVitals using OBD-II** is a Python script designed to connect to a vehicle's OBD-II port, retrieve diagnostic data, generate a PDF report, and optionally send it via email.

---

## Features
- Retrieve real-time vehicle diagnostics:
  - RPM, speed, engine load, coolant temperature, throttle position, and more.
- Generate a detailed PDF diagnostic report.
- Send the generated report via email with one command.

---

## Pre-requisites
Before using this tool, ensure the following requirements are met:

1. **Hardware**:
   - An OBD-II adapter (e.g., ELM327) compatible with your vehicle.
   - A laptop or system running Linux with a USB port or Bluetooth connection.

2. **Software**:
   - Python 3.7 or higher installed.
   - The following Python libraries:
     - `obd`
     - `reportlab`
   - `mutt` email client for sending reports (optional).

3. **Permissions**:
   - Access to the OBD-II port, e.g., `/dev/ttyUSB0`.
   - Ensure the user has necessary permissions for serial ports:
     ```bash
     sudo chmod 666 /dev/ttyUSB0
     ```

---

## Installation
Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CarVitals-OBD-II.git
   cd CarVitals-OBD-II
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install `mutt` if you plan to use the email feature:
   ```bash
   sudo apt-get install mutt
   ```

---

## Usage
1. **Connect Your Hardware**:
   - Plug the OBD-II adapter into your vehicle's diagnostic port.
   - Connect your system to the adapter (via USB or Bluetooth).

2. **Run the Script**:
   ```bash
   python3 src/car_diagnostics.py
   ```

3. **Check the Report**:
   - The PDF report (`car_diagnostic_report.pdf`) will be generated in the project directory.

4. **Send the Report via Email (Optional)**:
   - Ensure your `mutt` configuration is set up correctly.
   - The script will automatically send the report to the specified email.

---

### Precautions:
1. **Vehicle Safety**:
   - Ensure the vehicle is stationary and on level ground before starting diagnostics.
   - Do not disconnect the OBD-II adapter during operation.

2. **System Compatibility**:
   - Verify that your OBD-II adapter is compatible with your vehicle.
   - Test the connection to `/dev/ttyUSB0` (or equivalent) before running the script.

3. **Email Configuration**:
   - Configure `mutt` for sending emails. Test it by sending a sample email to yourself before using the tool.

4. **Code and Environment**:
   - Avoid running the script as root unless necessary.
   - Ensure no sensitive data (e.g., email credentials) is hardcoded in the script.

---

## Output Example
A sample report includes details such as:
- **Engine RPM**: 1200
- **Speed**: 60 km/h
- **Engine Load**: 75%
- **Fault Codes**: None (or displayed if present)

---

## Troubleshooting
- **No Data from OBD-II Adapter**:
  - Ensure the adapter is correctly plugged into the vehicle.
  - Check the serial port permissions (`sudo chmod 666 /dev/ttyUSB0`).

- **Email Not Sent**:
  - Verify `mutt` is installed and configured:
    ```bash
    echo "Test email" | mutt -s "Test" recipient@example.com
    ```
