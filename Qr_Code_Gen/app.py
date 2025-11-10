import qrcode
import os


def generate_upi_qr():
    print("🧾 UPI QR Code Generator")
    upi_id = input("Enter your UPI ID (e.g., username@bank): ").strip()

    if not upi_id or "@" not in upi_id:
        print(
            "❌ Invalid UPI ID. Please enter a valid one like example@upi or username@bank."
        )
        return

    # Create folder to save QR codes (optional)
    os.makedirs("UPI_QR", exist_ok=True)

    # Define payment URLs
    phonepe_url = f"upi://pay?pa={upi_id}&pn=PhonePe&cu=INR"
    gpay_url = f"upi://pay?pa={upi_id}&pn=GooglePay&cu=INR"

    # Generate QR codes
    phonepe_qr = qrcode.make(phonepe_url)
    gpay_qr = qrcode.make(gpay_url)

    # File paths
    phonepe_path = os.path.join("UPI_QR", "phonepe_qr.png")
    gpay_path = os.path.join("UPI_QR", "gpay_qr.png")

    # Save QR codes
    phonepe_qr.save(phonepe_path)
    gpay_qr.save(gpay_path)

    print("\n✅ QR Codes generated successfully!")
    print(f"📁 Saved at:\n  - {phonepe_path}\n  - {gpay_path}\n")

    # Display QR codes
    phonepe_qr.show()
    gpay_qr.show()


if __name__ == "__main__":
    generate_upi_qr()
