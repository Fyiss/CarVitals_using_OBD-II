#!/usr/bin/env python3

import obd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

connection = obd.OBD("/dev/ttyUSB0")  # Replace with your actual port


commands = [
    
    obd.commands.RPM,
    obd.commands.SPEED,
    obd.commands.ENGINE_LOAD,
    obd.commands.COOLANT_TEMP,
    obd.commands.THROTTLE_POS,
    obd.commands.TIMING_ADVANCE,
    obd.commands.SHORT_FUEL_TRIM_1,
    obd.commands.LONG_FUEL_TRIM_1,
    obd.commands.O2_SENSORS,
    obd.commands.GET_DTC,
    
]

pdf_filename = "car_diagnostic_report.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)
c.setFont("Helvetica", 12)


c.drawString(100, 750, "Complete Car Diagnostic Report")
c.drawString(100, 735, "=============================")

y_position = 700
for cmd in commands:
    try:
        response = connection.query(cmd)
        if response.is_null():
            c.drawString(100, y_position, f"{cmd.name}: No Data")
        else:
            c.drawString(100, y_position, f"{cmd.name}: {response.value}")
    except Exception as e:
      
        c.drawString(100, y_position, f"{cmd.name}: Command Not Supported")
    y_position -= 20


codes = connection.query(obd.commands.GET_DTC).value
if codes:
    c.drawString(100, y_position, f"Fault Codes: {codes}")
else:
    c.drawString(100, y_position, "Fault Codes: No Fault Codes Found")


c.save()
print(f"Complete diagnostic report generated: {pdf_filename}")


def send_email():
   
    recipient_email = "abc@example.com"
    
    
    command = f'echo "Please find the attached complete car diagnostic report." | mutt -s "Complete Car Diagnostic Report" -a {pdf_filename} -- {recipient_email}'
    os.system(command)

    print("Email sent successfully.")


send_email()

