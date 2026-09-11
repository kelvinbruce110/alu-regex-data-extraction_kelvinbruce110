import re
import json
from pathlib import Path


# ---------------------------------------------------------
# REGEX PATTERNS
# ---------------------------------------------------------

EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

URL_PATTERN = r'https?://(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?'

PHONE_PATTERN = (
    r'(?<!\d)'
    r'(?:\+250[\s-]?(?:7\d{2})[\s-]?\d{3}[\s-]?\d{3}'
    r'|0(?:7\d{2})[\s-]?\d{3}[\s-]?\d{3})'
    r'(?!\d)'
)

CREDIT_CARD_PATTERN = r'(?<!\d)(?:\d{4}[- ]?){3}\d{4}(?!\d)'

CURRENCY_PATTERN = (
    r'(?:USD|RWF|\$|€|£)\s?'
    r'\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
)


# ---------------------------------------------------------
# ALU EMAIL VALIDATION
# ---------------------------------------------------------

ALU_OFFICIAL_PATTERN = (
    r'^[A-Za-z0-9._%+-]+@alueducation\.com$'
)

ALU_ALUMNI_PATTERN = (
    r'^[A-Za-z0-9._%+-]+@alumni\.alueducation\.com$'
)

ALU_SI_PATTERN = (
    r'^[A-Za-z0-9._%+-]+@si\.alueducation\.com$'
)


# ---------------------------------------------------------
# SECURITY CHECK
# ---------------------------------------------------------

SUSPICIOUS_PATTERNS = [
    r'<script\b',
    r'javascript:',
    r'onerror\s*=',
    r'onload\s*='
]


def contains_unsafe_content(text):
    """Check for common injection-like or unsafe content."""
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True

    return False


# ---------------------------------------------------------
# CREDIT CARD MASKING
# ---------------------------------------------------------

def mask_credit_card(card):
    """Keep only the final four digits visible."""
    digits = re.sub(r'\D', '', card)

    return '*' * (len(digits) - 4) + digits[-4:]


# ---------------------------------------------------------
# ALU EMAIL CLASSIFICATION
# ---------------------------------------------------------

def classify_alu_email(email):
    """Determine which ALU email domain the address belongs to."""

    if re.fullmatch(ALU_OFFICIAL_PATTERN, email, re.IGNORECASE):
        return "official"

    if re.fullmatch(ALU_ALUMNI_PATTERN, email, re.IGNORECASE):
        return "alumni"

    if re.fullmatch(ALU_SI_PATTERN, email, re.IGNORECASE):
        return "si"

    return None


# ---------------------------------------------------------
# MAIN EXTRACTION
# ---------------------------------------------------------

def extract_data(text):

    emails = re.findall(EMAIL_PATTERN, text)
    urls = re.findall(URL_PATTERN, text)
    phones = re.findall(PHONE_PATTERN, text)
    credit_cards = re.findall(CREDIT_CARD_PATTERN, text)
    currencies = re.findall(CURRENCY_PATTERN, text)

    alu_emails = {
        "official": [],
        "alumni": [],
        "si": []
    }

    for email in emails:
        category = classify_alu_email(email)

        if category:
            alu_emails[category].append(email)

    masked_cards = [
        mask_credit_card(card)
        for card in credit_cards
    ]

    return {
        "emails": emails,
        "alu_email_validation": alu_emails,
        "urls": urls,
        "phone_numbers": phones,
        "credit_cards": masked_cards,
        "currency_amounts": currencies,
        "security": {
            "unsafe_content_detected":
                contains_unsafe_content(text),
            "credit_card_numbers_masked": True
        }
    }


# ---------------------------------------------------------
# PROGRAM ENTRY POINT
# ---------------------------------------------------------

def main():

    input_file = Path("input/raw-text.txt")
    output_file = Path("output/sample-output.json")

    text = input_file.read_text(
        encoding="utf-8",
        errors="replace"
    )

    results = extract_data(text)

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file.write_text(
        json.dumps(results, indent=4),
        encoding="utf-8"
    )

    print("Data extraction completed successfully.")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()
