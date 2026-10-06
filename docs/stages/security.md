---
title: LLM security
description: The ways LLM applications get attacked, and how to limit the damage.
---

# LLM security

<p class="rm-lede">The traineeship covered security in general. LLMs add new problems: text in a document can become an instruction, and a model can leak what it was shown. This stage covers the risks interviewers expect you to name.</p>

<div class="rm-meta" markdown>
<span>Stage 6 of 9</span>
<span>About 2.5 hours</span>
<span>Builds on: the traineeship security module</span>
</div>

!!! curating "This stage is being curated"
    Course sections and exercises are being selected.

## Learn

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/){ .rm-item .rm-refresh data-source="Reference · OWASP" data-time="30 min" } The standard list of LLM risks. Skim all ten, read prompt injection in detail.

## Interview questions

??? interview rm-refresh "What is prompt injection?"
    Text that the model treats as instructions even though it came from an untrusted source: a user message, a web page, an email, or a retrieved document. "Ignore your previous instructions and…" is the classic example. *Indirect* prompt injection, hidden in content the application retrieves, is the harder case, because the user never typed it.

??? interview rm-refresh "How do you defend against prompt injection?"
    There is no complete fix, so limit what a successful attack can do: give the model and its tools **least privilege**, require **human approval** for risky actions, keep untrusted content clearly separated from instructions, **validate outputs** before acting on them, and monitor for unusual behaviour. Say plainly that filtering prompts alone is not enough.

??? interview rm-refresh "What data protection issues come with sending data to an LLM provider?"
    Personal or confidential data leaves your environment, so you need to know where it is processed (EU region?), whether the provider stores it or trains on it, and whether that fits the GDPR and your client's contracts. Mitigations: enterprise agreements with no training on your data, EU hosting, and removing personal data before it is sent.
