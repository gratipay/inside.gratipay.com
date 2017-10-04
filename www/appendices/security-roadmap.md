# Gratipay Security Roadmap

## Table of contents

1) Introduction

2) Scope

3) Tools

4) Results

5) Notes

## Introduction

The following is a report on the general security of Gratipay. We hope by sharing this we can get more people involved in improving the security of the website and keep track of what is done and needs doing. On top of that, this should ensure we only get valuable reports on HackerOne, rather than ones demonstrating a theoretical risk.

_Note: None of these issues are security vulnerabilities._

## Scope

All of the following domains are within the scope of this report:
   
    *.gratipay.com
    grtp.co

## Tools

These are the tools that we use to evaluate Gratipay's overall security:
    
- SecurityHeaders (https://securityheaders.io/)
- Hardenize (https://www.hardenize.com/)
- SSLlabs (https://www.ssllabs.com/ssltest/)
    
## Results

### SecurityHeaders

Score is based on the following criteria:
    
- X-XSS-Protection
- X-Content-Type-Options
- X-Frame-Options
- Strict-Transport-Security
- Content-Security-Policy
- Public-Key-Pins
- Referrer-Policy

**gratipay.com:** https://securityheaders.io/?q=gratipay.com&hide=on&followRedirects=on

Score: **D**

- X-XSS-Protection (Yes)
- X-Content-Type-Options (Yes)
- X-Frame-Options (Yes)
- Strict-Transport-Security (No)
- Content-Security-Policy (No*)
- Public-Key-Pins (No)
- Referrer-Policy (No)

**inside.gratipay.com:** https://securityheaders.io/?q=inside.gratipay.com&hide=on&followRedirects=on

Score: **F**

- X-XSS-Protection (No)
- X-Content-Type-Options (No)
- X-Frame-Options (No)
- Strict-Transport-Security (No)
- Content-Security-Policy (No)
- Public-Key-Pins (No)
- Referrer-Policy (No)

**grtp.co:** https://securityheaders.io/?q=grtp.co&hide=on&followRedirects=on

Score: **E**

- X-XSS-Protection (Yes)
- X-Content-Type-Options (No)
- X-Frame-Options (No)
- Strict-Transport-Security (No)
- Content-Security-Policy (No)
- Public-Key-Pins (No)
- Referrer-Policy (No)

### Hardenize

Hardenize reports are always in the following format:
    
    Domain
    Email
    WWW
    
The results are graded as follows:

	✓ = good
	X = neutral
	i(n) = error (with reference number for additional information)

**gratipay.com:** https://www.hardenize.com/report/gratipay.com

---

**Domain**

| -            | : |
|--------------|---|
| Name servers | ✓ |
| DNSSEC       | X |
| CAA          | X |

---

**Email**

| SECURE TRANSPORT (SMTP)| : |
|------------------------|---|
| TLS                    | ✓ |
| Certificates           | X |
| DANE                   | X |

| AUTHENTICATION AND POLICY | : |
|---------------------------|---|
| SPF                       | i1 |
| DMARC                     | X |

**i1:** Policy DNS lookups over limit
Your policy exceeds the allowed number of DNS queries. As a result, parts of it may not be processed by implementations that enforce this limit. Please refer to the SPF specification Section 4.6.4. for more information. Lookups: 11

---

**WWW**

| PROTOCOLS   | : |
|-------------|---|
| HTTP (80)   | ✓ |
| HTTPS (443) | ✓ |

| SECURE TRANSPORT | : |
|------------------|---|
| TLS              | ✓ |
| Certificates     | ✓ |
| DANE             | X |
| Cookies          | ✓ |
| Mixed Content    | ✓ |

| MODERN SECURITY FEATURES  | : |
|---------------------------|---|
| Strict Transport Security | X |
| Public Key Pinning        | X |
| Content Security Policy   | ✓ |
| Subresource Integrity     | X |

| APPLICATION SECURITY  | : |
|-----------------------|---|
| Frame Options         | X |
| XSS Protection        | X |
| Content Type Options  | ✓ |

## Notes

* SecurityHeaders believes that no CSP is present on gratipay.com, because we have set the header to "Content-Security-Policy-Report-Only"