# ALU Regex Data Extraction & Secure Validation

## Project Description

This project was developed as part of the ALU Data Extraction & Secure Validation Assignment.

The purpose of the project is to extract structured information from raw text using Python and Regular Expressions (Regex), while also validating the extracted data and handling potentially unsafe input.

The program processes realistic customer support data and extracts different types of information including email addresses, URLs, phone numbers, credit card numbers, and currency amounts.

It also performs security checks to identify suspicious input and protects sensitive credit card information by masking it in the output.

---

## Project Structure

```text
alu-regex-data-extraction_kelvinbruce110/
│
├── input/
│   ├── raw-text.txt
│   └── security-test.txt
│
├── src/
│   └── main.py
│
├── output/
│   ├── sample-output.json
│   └── security-test-output.json
│
└── README.md
```

---

## Features

The program can:

* Extract email addresses from raw text.
* Validate ALU email addresses.
* Classify ALU emails into official, alumni, and SI addresses.
* Extract URLs.
* Extract Rwandan phone numbers in different formats.
* Extract and validate credit card numbers.
* Mask credit card numbers to protect sensitive information.
* Extract currency amounts.
* Detect suspicious or potentially malicious input.
* Handle malformed and invalid data safely.
* Accept different input and output files from the command line.

---

## Data Types Extracted

### 1. Email Addresses

The program extracts properly formatted email addresses such as:

```text
alice.mukamana@gmail.com
alice.mukamana@alueducation.com
jean.mutesi@alumni.alueducation.com
student.records@si.alueducation.com
```

### 2. ALU Email Addresses

The program specifically validates ALU email addresses using the following domains:

```text
@alueducation.com
@alumni.alueducation.com
@si.alueducation.com
```

The addresses are classified as:

* `official`
* `alumni`
* `si`

### 3. URLs

The program extracts HTTP and HTTPS URLs.

Examples:

```text
https://www.alueducation.com/support
https://portal.alueducation.com/login
```

### 4. Phone Numbers

The program supports common Rwandan phone number formats, including:

```text
+250 788 123 456
0788 123 456
+250-722-555-901
```

### 5. Credit Card Numbers

The program detects credit card numbers written using different formats, including:

```text
4111 1111 1111 1111
4111-1111-1111-1111
4111111111111111
```

Credit card numbers are validated before being included in the output.

For security, the complete card number is never exposed in the output.

Example:

```text
4111 1111 1111 1111
```

is displayed as:

```text
**** **** **** 1111
```

### 6. Currency Amounts

The program extracts currency values such as:

```text
$1,250.50
RWF 45,000
```

---

## Security Validation

Security is an important part of the project.

The program checks the raw input for suspicious patterns that could represent malicious content.

Examples include:

```text
<script>
javascript:
onerror=
onload=
onclick=
```

If suspicious content is detected, the program handles the input safely instead of treating the malicious content as normal structured data.

The program also includes protection for sensitive payment information by masking credit card numbers.

---

## Input Files

### `input/raw-text.txt`

This is the normal test file.

It contains realistic customer support information, valid examples, formatting variations, and invalid examples.

It does not contain malicious input so that the normal extraction process can be tested successfully.

### `input/security-test.txt`

This file is used to test the security validation functionality.

It contains suspicious or malicious-looking input to verify that the program can detect unsafe content.

Keeping the normal and security tests in separate files makes it easier to demonstrate both parts of the assignment.

---

## Running the Program

The program accepts the input file and output file through command-line arguments.

First, navigate to the project root:

```bash
cd /alu-regex-data-extraction_kelvinbruce110
```

### Run the normal extraction test

```bash
python3 src/main.py input/raw-text.txt output/sample-output.json
```

This processes:

```text
input/raw-text.txt
```

and saves the results to:

```text
output/sample-output.json
```

### Run the security test

```bash
python3 src/main.py input/security-test.txt output/security-test-output.json
```

This processes:

```text
input/security-test.txt
```

and saves the results to:

```text
output/security-test-output.json
```

The input file is therefore selected by the command used to run the program.

---

## Example Output

The program produces JSON output containing the extracted and validated information.

Example:

```json
{
    "emails": [
        "alice.mukamana@gmail.com",
        "alice.mukamana@alueducation.com"
    ],
    "alu_email_validation": {
        "official": [
            "alice.mukamana@alueducation.com"
        ],
        "alumni": [],
        "si": []
    },
    "urls": [
        "https://www.alueducation.com/support"
    ],
    "phone_numbers": [
        "+250 788 123 456"
    ],
    "credit_cards": [
        "**** **** **** 1111"
    ],
    "currency_amounts": [
        "$1,250.50",
        "RWF 45,000"
    ]
}
```

The actual output depends on the input file being processed.

---

## Edge Cases Tested

The project includes different realistic variations and invalid inputs, including:

* Valid and invalid email addresses.
* Different ALU email domains.
* Phone numbers with spaces.
* Phone numbers with hyphens.
* Phone numbers beginning with `0`.
* Phone numbers beginning with `+250`.
* Credit card numbers with spaces.
* Credit card numbers with hyphens.
* Credit card numbers without separators.
* Valid and invalid credit card numbers.
* Different currency formats.
* Invalid URLs.
* Malformed input.
* Suspicious JavaScript or HTML input.

---

## Technologies Used

* Python 3
* Regular Expressions (`re`)
* JSON
* Pathlib
* Argparse

No external Python packages are required.

---

## Security and Privacy Considerations

The program treats all input as untrusted data.

Sensitive payment information is protected by masking credit card numbers before they are written to the output.

The program also detects suspicious patterns that could indicate malicious input and prevents unsafe content from being processed as normal structured information.

The project demonstrates basic secure input-handling practices while still allowing legitimate structured information to be extracted.

---

## Conclusion

This project demonstrates how Python Regular Expressions can be used to extract structured information from realistic raw text.

It combines:

* Regex-based extraction
* Data validation
* Edge-case handling
* Security checks
* Sensitive-data protection
* JSON output

The project is designed to show that data extraction should not only focus on finding patterns, but should also consider validation, security, and realistic input variations.

