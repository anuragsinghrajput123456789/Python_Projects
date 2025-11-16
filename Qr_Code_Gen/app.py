# import qrcode
# import os


# def generate_upi_qr():
#     print("🧾 UPI QR Code Generator")
#     upi_id = input("Enter your UPI ID (e.g., username@bank): ").strip()

#     if not upi_id or "@" not in upi_id:
#         print(
#             "❌ Invalid UPI ID. Please enter a valid one like example@upi or username@bank."
#         )
#         return

#     # Create folder to save QR codes (optional)
#     os.makedirs("UPI_QR", exist_ok=True)

#     # Define payment URLs
#     phonepe_url = f"upi://pay?pa={upi_id}&pn=PhonePe&cu=INR"
#     gpay_url = f"upi://pay?pa={upi_id}&pn=GooglePay&cu=INR"

#     # Generate QR codes
#     phonepe_qr = qrcode.make(phonepe_url)
#     gpay_qr = qrcode.make(gpay_url)

#     # File paths
#     phonepe_path = os.path.join("UPI_QR", "phonepe_qr.png")
#     gpay_path = os.path.join("UPI_QR", "gpay_qr.png")

#     # Save QR codes
#     phonepe_qr.save(phonepe_path)
#     gpay_qr.save(gpay_path)

#     print("\n✅ QR Codes generated successfully!")
#     print(f"📁 Saved at:\n  - {phonepe_path}\n  - {gpay_path}\n")

#     # Display QR codes
#     phonepe_qr.show()
#     gpay_qr.show()


# if __name__ == "__main__":
#     generate_upi_qr()





import qrcode
import os
import base64
from datetime import datetime


# -----------------------------
# CREATE FOLDER FOR QRs
# -----------------------------
QR_FOLDER = "Generated_QR"
os.makedirs(QR_FOLDER, exist_ok=True)


# -----------------------------
# GENERIC QR MAKER
# -----------------------------
def generate_qr(data, filename_prefix="qr"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(QR_FOLDER, f"{filename_prefix}_{timestamp}.png")

    qr = qrcode.make(data)
    qr.save(file_path)

    print(f"\n✅ QR Code Generated Successfully!")
    print(f"📁 Saved at: {file_path}")
    qr.show()


# -----------------------------
# 1️⃣  UPI QR
# -----------------------------
def upi_qr():
    upi_id = input("Enter your UPI ID (username@bank): ").strip()
    name = input("Enter Payee Name: ").strip()
    amount = input("Enter Amount (optional): ").strip()

    url = f"upi://pay?pa={upi_id}&pn={name}&cu=INR"
    if amount:
        url += f"&am={amount}"

    generate_qr(url, "UPI")


# -----------------------------
# 2️⃣  TEXT / NOTES QR
# -----------------------------
def text_qr():
    text = input("Enter your text/notes to convert into QR:\n> ")
    generate_qr(text, "TEXT")


# -----------------------------
# 3️⃣  URL QR
# -----------------------------
def url_qr():
    url = input("Enter URL (https://...): ").strip()
    generate_qr(url, "URL")


# -----------------------------
# 4️⃣  Wi-Fi QR
# -----------------------------
def wifi_qr():
    ssid = input("Enter Wi-Fi SSID: ")
    password = input("Enter Wi-Fi Password: ")
    encryption = input("Enter Encryption (WPA/WEP/NONE): ").upper()

    wifi_string = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
    generate_qr(wifi_string, "WIFI")


# -----------------------------
# 5️⃣  vCard Contact QR
# -----------------------------
def contact_qr():
    name = input("Full Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")

    vcard = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD
"""
    generate_qr(vcard, "CONTACT")


# -----------------------------
# 6️⃣  FILE → QR
# Stores file as base64 and generates a QR
# -----------------------------
def file_qr():
    file_path = input("Enter file path (pdf, image, txt, etc.): ").strip()

    if not os.path.exists(file_path):
        print("❌ File does not exist.")
        return

    with open(file_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")

    print("\n⚠ Large files may produce larger QR codes.")
    generate_qr(encoded, "FILE_BASE64")

    print("\nℹ Decode with any Base64 → File converter.")


# -----------------------------
# MAIN MENU
# -----------------------------
def main_menu():
    while True:
        print("""
===================================================
🔹 UNIVERSAL QR CODE GENERATOR
===================================================
Choose an option:

1. Generate UPI Payment QR
2. Convert Text / Notes to QR
3. Convert URL to QR
4. Generate Wi-Fi Login QR
5. Generate Contact (vCard) QR
6. Convert Any File to QR
7. Exit
===================================================
""")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            upi_qr()
        elif choice == "2":
            text_qr()
        elif choice == "3":
            url_qr()
        elif choice == "4":
            wifi_qr()
        elif choice == "5":
            contact_qr()
        elif choice == "6":
            file_qr()
        elif choice == "7":
            print("👋 Exiting. Thank you!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


# -----------------------------
if __name__ == "__main__":
    main_menu()
