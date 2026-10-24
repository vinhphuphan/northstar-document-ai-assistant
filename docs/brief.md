# Brief — Vietnamese Equity Research System

## Summary

**Vietnamese Equity Research System** is a fictional AI-powered research platform for Vietnamese investors and equity analysts.

The system helps users search Vietnamese financial reports, extract financial data, compare company performance across multiple years, and ask questions in natural language with grounded answers and source citations.

## The problem

Investors and analysts often spend significant time manually working through annual reports and financial statements:

- Finding relevant financial information
- Copying figures into spreadsheets
- Calculating year-over-year and multi-year growth
- Comparing companies and business segments
- Reviewing disclosures and risk factors
- Repeating the same process across multiple years

This repetitive work takes time away from actual investment research.

## What they want

An AI assistant that allows users to:

- Ask questions about Vietnamese companies and financial reports in natural language
- Find relevant information across multiple years
- Compare financial performance between companies or periods
- Calculate and explain relevant financial metrics
- Identify multi-year growth trends
- Evaluate evidence related to CANSLIM factors
- Cite the source report and page
- Show the supporting passage
- Refuse to answer when the available evidence is insufficient
- Sign in and view their conversation history

## Example questions

1. How did FPT's revenue and net profit grow from 2021 to 2025?
2. What was FPT's revenue growth rate over the last four years?
3. Compare MWG's revenue, gross profit, and net profit across 2021–2025.
4. Which business segments contributed most to MWG's revenue growth?
5. How did VCB's profitability and asset quality change over the available years?
6. Which companies show the strongest multi-year earnings growth?
7. What do the reports disclose about major risks, competitive advantages, or changes in business conditions?
8. What evidence in the reports supports or weakens specific CANSLIM factors?
9. Compare the financial performance of FPT, MWG, VCB, and VIC across the available years.
10. When the reports do not provide enough evidence, what conclusions should the assistant refuse to make?

## Initial corpus

The initial corpus contains Vietnamese financial reports for selected Vietnamese public companies across multiple years.

The initial demo is limited to four tickers (FPT, VCB, MWG, and VIC) from 2021 through 2025, with annual reports (BCTN) and consolidated annual financial statements (BCTC). Other tickers are out of scope until their reports are added to the corpus.

Current sample companies:

- FPT
- VCB
- MWG
- VIC

Target reporting period:

- 2021–2025

## Trust requirements

This is an investment research application, so **accuracy and traceability are critical**.

The assistant must:

- Never invent financial data or facts
- Only use information available in the document corpus
- Cite the source report and page
- Show the supporting passage
- Clearly distinguish reported figures from calculated metrics
- Refuse to make unsupported conclusions

A confident but unsupported answer is worse than no answer.

## Constraints

- **Corpus:** Vietnamese financial reports and annual reports
- **Companies:** Vietnamese public companies
- **Period:** 2021–2025
- **Language:** Vietnamese
- **Users:** Investors and equity analysts
- **Authentication:** Email-based authentication
- **Hosting:** Small/medium cloud footprint

## Out of scope

- Real-time stock prices
- News and social media data
- External alternative data
- Automated trading
- Personalized financial advice
- Unsubstantiated investment recommendations
- Multi-tenant support
- Mobile application

## Definition of done

The system should allow a user to:

1. Search and retrieve relevant information from the financial-report corpus.
2. Ask multi-year financial questions in natural language.
3. Receive answers grounded in the source documents.
4. Verify answers through page-level citations and supporting passages.
5. Calculate relevant financial metrics from the available data.
6. Compare companies and identify multi-year trends.
7. Refuse unsupported conclusions rather than hallucinate.