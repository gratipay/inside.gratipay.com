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
*   Use the identified communication channels to report vulnerability information to us;
*   Report vulnerabilities as soon as you discover them; and
*   Keep information about any vulnerabilities you’ve discovered confidential between yourself and Gratipay until we’ve had 90 days to resolve the issue.

If you follow these guidelines when reporting an issue to us, we commit to:

*   Not pursue or support any legal action related to your research;
*   Work with you to understand and resolve the issue quickly (including an initial confirmation of your report within 72 hours of submission).

Additionally, if you are the first to report the issue, and we make a code or configuration change based on the issue, we commit to:

*   Recognize your contribution on HackerOne;
*   Reward you with a bounty:

  * $100 if you identified a **severe** risk.
  * $40 if you identified a **moderate** risk.
  * $10 if you identified a **mild** risk.
  * $1 if you identified a **theoretical** risk.

Please note that our policy is to fully disclose all resolved issues, in the interest of openness and transparency for our customers.

## Scope

* [https://gratipay.com](https://gratipay.com)
* [https://grtp.co](https://grtp.co) (not in scope for clickjacking)
* any other [software we publish](https://github.com/gratipay)

## Out of scope

Any services hosted by 3rd party providers and services are excluded from scope.

In the interest of the safety of our users, staff, the Internet at large and you as a security researcher, the following test types are excluded from scope:

*   Findings from physical testing such as office access (e.g. open doors, tailgating)
*   Findings derived primarily from social engineering (e.g. phishing, vishing)
*   Findings from applications or systems not listed in the ‘Scope’ section
*   UI and UX bugs and spelling mistakes
*   Network level Denial of Service (DoS/DDoS) vulnerabilities

Things we do not want to receive:

*   Personally identifiable information (PII)
*   Credit card holder data

## How to Report a Security Vulnerability

If you believe you’ve found a security vulnerability in one of our products or platforms, please [send it to us on HackerOne](https://hackerone.com/gratipay/reports/new).

### Email

We prefer that you file reports on HackerOne, but we also accept reports via email to security@gratipay.com. Please include the following details with your report:

*   Description of the location and potential impact of the vulnerability;
*   A detailed description of the steps required to reproduce the vulnerability (POC scripts, screenshots, and compressed screen captures are all helpful to us); and
*   Your name/handle and a link for recognition in our legacy [Hall of Fame](https://gratipay.com/about/security/hall-of-fame) (if reporting via email and not willing to join HackerOne).

To encrypt your message, you may use [our PGP key](https://gratipay.com/about/security/pgp.asc):

```sh
$ curl https://gratipay.com/about/security/pgp.asc | gpg --import
gpg: key 7A5F6B30: "Gratipay Security <security@gratipay.com>" imported
gpg: Total number processed: 1
gpg:               imported: 1
$
```

We only use PGP to decrypt messages, never to encrypt messages or authenticate our identity. Instead, we'll create a ticket on HackerOne to track your report, which we'll invite you to join (see our [internal policy document](http://inside.gratipay.com/howto/handle-security-issues) for more details). If you do not wish to join HackerOne, we can acknowledge you instead on our legacy [Hall of Fame](https://gratipay.com/about/security/hall-of-fame).
