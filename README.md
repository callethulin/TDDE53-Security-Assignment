# TDDE53 Security Assignment – HTTPS & Certificate Analysis

This repository contains results from a security assignment on HTTPS, TLS, X.509 certificates, and analysis using Wireshark, OpenSSL, and crt.sh.

## Key Concepts
- **HTTPS/TLS** – Encrypted communication using certificates.
- **X.509 certificates** – Digital identities with issuer, validity, public key.
- **BadSSL tests** – Expired, wrong host, self-signed, revoked, etc.
- **Wireshark + SSL key log** – Decrypt TLS traffic.
- **OpenSSL** – Inspect certificates.

## Domains Tested
| Case | Domain |
|------|--------|
| 2.1 | expired.badssl.com |
| 2.2 | wrong.host.badssl.com |
| 2.3 | self-signed.badssl.com |
| 2.4 | untrusted-root.badssl.com |
| 2.5 | revoked.badssl.com |
| 2.6 | liu.se |
| 2.7 | tsn.ca |
| 2.8 | seb.se |
| 2.9 | scholar.google.com |
| 2.10 | facebook.com |
| 2.11 | badssl.com |
| 2.12 | crt.sh |

## Results Summary

### Certificates from Traces
| Domain | Issuer | Validity | Size (B) |
|--------|--------|----------|----------|
| expired | COMODO RSA | 2015-04-09 – 2015-04-12 | 1359 |
| wrong.host | Let's Encrypt (R11) | 2025-01-07 – 2025-04-07 | 1271 |
| self-signed | *.badssl.com | 2025-02-11 – 2027-02-11 | 893 |
| untrusted-root | BadSSL Untrusted Root | 2025-02-11 – 2027-02-11 | 1181 |
| revoked | Let's Encrypt (E6) | 2024-12-19 – 2025-03-19 | 904 |
| liu.se | Let's Encrypt (R11) | 2025-02-10 – 2025-05-11 | 1531 |
| tsn.ca | Entrust L1F | 2024-06-06 – 2025-07-05 | 1920 |
| seb.se | DigiCert Global G2 | 2024-10-22 – 2025-10-21 | 1835 |
| scholar.google.com | Google Trust Services | 2025-02-03 – 2025-04-28 | 3599 |
| facebook.com | DigiCert SHA2 High | 2024-11-27 – 2025-02-25 | 1691 |
| badssl.com | Let's Encrypt (R11) | 2025-01-07 – 2025-04-07 | 1271 |
| crt.sh | Sectigo RSA Org Validation | 2025-01-20 – 2025-04-20 | 1861 |

### Expired vs Non-expired (from crt.sh)
| Domain | Non-expired | Expired |
|--------|-------------|---------|
| expired.badssl.com | 12 | 12 |
| wrong.host.badssl.com | 12 | 12 |
| revoked.badssl.com | 12 | 12 |
| liu.se | 4324 | 3781 |
| tsn.ca | 251 | 24 |
| seb.se | 1248 | 115 |
| scholar.google.com | 1152 | 1351 |
| facebook.com | 2093 | 2037 |
| badssl.com | 12 | 12 |
| crt.sh | 104 | 8 |

> Self-signed & untrusted-root not logged in CT.

### PEM vs Human-Readable Size (bytes)
| Domain | PEM | OpenSSL text |
|--------|-----|--------------|
| liu.se | 2130 | 4997 |
| tsn.ca | 2654 | 3924 |
| seb.se | 2045 | 4211 |
| scholar.google.com | 4929 | 6132 |
| facebook.com | 2126 | 4259 |
| badssl.com | 1777 | 3868 |
| crt.sh | 2577 | 5404 |

Human-readable is larger due to descriptive labels.
