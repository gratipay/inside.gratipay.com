####################################################################################
#                                                                                  #
#   This gets copied and pasted into a textarea on hackerone.com/gratipay whenever #
#   it changes.                                                                    #
#                                                                                  #
####################################################################################


## Guidelines

We ask that all researchers:

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


## Awards

If you are the first to report an issue, and we make a code or configuration change based on the issue, we will award you:

| Severity | CVSS       | Award       |
|----------|:----------:|--------------|
| Critical | 9.0 - 10.0 | $500 + heart coin + sticker\* + thanks |
| High     | 7.0 - 8.9  | $100 + sticker\* + thanks |
| Medium   | 4.0 - 6.9  | sticker\* + thanks |
| Low      | 0.1 - 3.9  | [thanks](https://hackerone.com/gratipay/thanks) |
| None     | 0          | ¯\\\_(ツ)\_/¯ |

<i>\* We only award a sticker for your first qualifying report.</i>


## Scope

* [https://gratipay.com](https://gratipay.com)
* [https://grtp.co](https://grtp.co) (not in scope for clickjacking)
* [gratipay-bot](https://github.com/gratipay/bot)
* [postgres.py](https://github.com/gratipay/postgres.py)
* [environment.py](https://github.com/gratipay/environment.py)

We target an "A" grade on SSLLabs for both [grtp.co](https://www.ssllabs.com/ssltest/analyze.html?d=grtp.co) and [gratipay.com](https://www.ssllabs.com/ssltest/analyze.html?d=gratipay.com), and consider it a low risk if we drop below that.


## Out of Scope

Any services hosted by 3rd party providers and services are excluded from scope.

In the interest of the safety of our users, staff, the Internet at large and you as a security researcher, the following test types are excluded from scope:

*   Findings from physical testing such as office access (e.g. open doors, tailgating)
*   Findings derived primarily from social engineering (e.g. phishing, vishing)
*   Findings from applications or systems not listed in the ‘Scope’ section
*   UI and UX bugs and spelling mistakes
*   Network level Denial of Service (DoS/DDoS) vulnerabilities
* Low severity issues that can be detected with tools such as [Hardenize](https://www.hardenize.com/) and [SecurityHeaders.io](https://securityheaders.io/).

Things we do not want to receive:

*   Personally identifiable information (PII)
*   Credit card holder data
*   Duplicates of reports we've already [identified as Severity: None](http://inside.gratipay.com/appendices/disclosures)


## How to Report a Security Vulnerability

If you believe you’ve found a security vulnerability in one of our products or platforms, please [send it to us on HackerOne](https://hackerone.com/gratipay/reports/new).

Please provide detailed reports with reproducible steps. If a report is not detailed enough to reproduce the issue, it will not be eligible for a bounty. We also ask you to cite references and not to copy/paste entire reports. Reports copied entirely or mostly from elsewhere will not be eligible for a bounty.

We especially appreciate reports containing the affected code from our [GitHub repository](https://github.com/gratipay), and possibly even patches, and we encourage you to test our platform by [setting up Gratipay locally](https://github.com/gratipay/gratipay.com#quick-start). That way you can test all sorts of payloads to your heart's content.


### History

Here is this program description's [version history](https://github.com/gratipay/inside.gratipay.com/commits/master/www/appendices/security-program.md).
