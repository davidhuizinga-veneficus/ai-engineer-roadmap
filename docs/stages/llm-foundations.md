---
title: LLM foundations
description: How large language models work from the outside, and how to call one from code.
---

# LLM foundations

<p class="rm-lede">Before building anything on top of an LLM, you need to know what you are calling: what a token is, why the same prompt can give different answers, how to get reliable structured output, and what an embedding is.</p>

<div class="rm-meta" markdown>
<span>Stage 1 of 9</span>
<span>About 3 hours</span>
<span>Builds on: your data science background</span>
</div>

!!! curating "This stage is being curated"
    Course sections and exercises are being selected. The essentials below are enough for the half-day refresh.

## Learn

- [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g){ .rm-item .rm-refresh data-source="Video · Andrej Karpathy" data-time="1 hour" } A one-hour tour of what LLMs are, how they are trained and where they fail.

## Interview questions

??? interview rm-refresh "What is a token, and why does it matter for cost and limits?"
    A token is a chunk of text the model reads and writes, often part of a word; in English roughly four characters on average. Models are billed per input and output token, and the context window (how much text fits in one request) is measured in tokens. So long prompts and long answers cost more and can hit the limit.

??? interview rm-refresh "What does temperature do?"
    It controls randomness when the model picks the next token. Low temperature (near 0) makes the most likely token win almost every time, which gives consistent answers: good for extraction and classification. Higher temperature spreads the choice out, which gives more varied output: useful for brainstorming. It does not make the model more or less "correct".

??? interview rm-refresh "How do you get reliable JSON out of an LLM?"
    Use the provider's **structured output** feature with a JSON schema (for example via Pydantic), so the response is constrained to that shape. Then still validate it in code, and decide what happens on failure: retry, or fall back. Asking for JSON in the prompt alone works most of the time, which is not good enough for production.
