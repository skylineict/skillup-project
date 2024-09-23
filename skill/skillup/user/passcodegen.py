import pyotp


def generate_passcode():
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    otp = totp.now()
    return f"PASS-{otp[-4:]}"
