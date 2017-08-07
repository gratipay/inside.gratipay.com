####################################################################################
#                                                                                  #
#   This gets copied and pasted into a textarea on hackerone.com/gratipay whenever #
#   it changes.                                                                    #
#                                                                                  #
####################################################################################


Thank you for helping us keep Gratipay users safe! We ask that all researchers:

*   Make every effort to avoid privacy violations, degradation of user experience, disruption to production systems, and destruction of data during security testing;
*   Perform research only within the scope set out below;
*   Review [our Severity: None disclosures](http://inside.gratipay.com/appendices/disclosures) to avoid filing unwanted reports;
*   Use the identified communication channels to report vulnerability information to us;
*   Report vulnerabilities as soon as you discover them; and
*   Keep information about any vulnerabilities you’ve discovered confidential between yourself and Gratipay until we’ve had 90 days to resolve the issue.

If you follow these guidelines when reporting an issue to us, we commit to:

*   Not pursue or support any legal action related to your research;
*   Work with you to understand and resolve the issue quickly (including an initial confirmation of your report within 72 hours of submission).

Please note that, as an [open organization](http://inside.gratipay.com/big-picture/welcome), our policy is to [fully disclose](http://inside.gratipay.com/appendices/disclosures) all resolved, informative, and not applicable issues, in the interest of openness and transparency for our customers.


## Scope

* [https://gratipay.com](https://gratipay.com)
* [https://grtp.co](https://grtp.co) (not in scope for clickjacking)
* [gratipay-bot](https://github.com/gratipay/bot)
* [postgres.py](https://github.com/gratipay/postgres.py)
* [environment.py](https://github.com/gratipay/environment.py)

We target an "A" grade on SSLLabs for both [grtp.co](https://www.ssllabs.com/ssltest/analyze.html?d=grtp.co) and [gratipay.com](https://www.ssllabs.com/ssltest/analyze.html?d=gratipay.com), and consider it a low risk if we drop below that.


### Out of Scope

In the interest of the safety of our users, staff, the Internet at large and you as a security researcher, the following test types and issues are excluded from scope:

* Findings from physical testing such as office access (e.g. open doors, tailgating)
* Findings derived primarily from social engineering (e.g. phishing, vishing)
* Findings from applications or systems not listed in the ‘Scope’ section
* UI and UX bugs and spelling mistakes
* Network level Denial of Service (DoS/DDoS) vulnerabilities
* Low severity issues that can be detected with tools such as [Hardenize](https://www.hardenize.com/) and [SecurityHeaders.io](https://securityheaders.io/).
* Vulnerability reports with video only PoCs
* Reports that state that software is out of date/vulnerable without a proof of concept.
* Host header issues without an accompanying proof-of-concept demonstrating vulnerability.
* XSS issues that affect only outdated browsers.
* Stack traces that disclose information. We are open source so most of this information is already out there.
* Highly speculative reports about theoretical damage. Be concrete.
* Vulnerabilities as reported by automated tools without additional analysis as to how they're an issue.
* Reports from automated web vulnerability scanners (Acunetix, Vega, etc.) that have not been validated.
* Content injection issues.
* Cross-site Request Forgery (CSRF) with minimal security implications (Logout CSRF, etc.)
* Missing cookie flags on non-security-sensitive cookies.
* Banner grabbing issues (figuring out what web server we use, etc.).
* Open ports without an accompanying proof-of-concept demonstrating vulnerability.
* Recently disclosed 0day vulnerabilities. We need time to patch our systems just like everyone else - please give us 30 days before reporting these types of issues.
* Issues in third-party services should be reported to the respective team. Please take a look at the "Third-party Services" section for more information.

Things we do not want to receive:

*   Personally identifiable information (PII)
*   Credit card holder data
*   Duplicates of reports we've already [identified as Severity: None](http://inside.gratipay.com/appendices/disclosures)


## Reporting

If you believe you’ve found a security vulnerability in one of our products or platforms, please [send it to us on HackerOne](https://hackerone.com/gratipay/reports/new).

Please provide detailed reports with reproducible steps. If a report is not detailed enough to reproduce the issue, it will not be eligible for a bounty. We also ask you to cite references and not to copy/paste entire reports. Reports copied entirely or mostly from elsewhere will not be eligible for a bounty.

We especially appreciate reports containing the affected code from our [GitHub repository](https://github.com/gratipay), and possibly even patches, and we encourage you to test our platform by [setting up Gratipay locally](https://github.com/gratipay/gratipay.com#quick-start). That way you can test all sorts of payloads to your heart's content.


## Awards

If you are the first to report an issue, and we make a code or configuration change based on the issue, we will award you:

| Severity | CVSS       | Example       | Award |
|:---------|:----------:|:--------------|:------|
| Critical | 9.0 - 10.0 | RCE           | $500\* + [heart coin](http://inside.gratipay.com/big-picture/brand#heart-coins) + sticker\*\* + thanks |
| High     | 7.0 - 8.9  | SQLi          | $100\* + sticker\*\* + thanks |
| Medium   | 4.0 - 6.9  | Reflected XSS | sticker\*\* + thanks |
| Low      | 0.1 - 3.9  | Self-XSS      | [thanks](https://hackerone.com/gratipay/thanks) |
| None     | 0          | ¯\\\_(ツ)\_/¯ | ¯\\\_(ツ)\_/¯ |

\* For `gratipay.com`; for other components we award $50/$10.

\*\* Awarded for your first qualifying report.


## Third-party Services

Gratipay uses the following third-party services. If you discover an issue make sure to report it to the service's security team.

- gratipay.freshdesk.com - Freshdesk (security@freshworks.com)
- assets.gratipay.com - MaxCDN (security@maxcdn.com)
- gratipay.slack.com - Slack (https://hackerone.com/slack)


## security@

If you have any questions concerning our program, feel free to send us an email at security@gratipay.com. Please do not send reports by email and make sure **not** to disclose sensitive information in the email.
