---
title: Evaluation and observability
description: Know whether your LLM application actually works, and see what it does in production.
---

# Evaluation and observability

<p class="rm-lede">"It looked good when I tried it" is not evaluation. This stage is about turning quality into numbers you can track, and logging enough to understand a bad answer after the fact.</p>

<div class="rm-meta" markdown>
<span>Stage 4 of 9</span>
<span>About 3 hours</span>
<span>Builds on: RAG, agents</span>
</div>

!!! curating "This stage is being curated"
    Course sections and exercises are being selected.

## Learn

- [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/){ .rm-item .rm-refresh data-source="Article · Hamel Husain" data-time="25 min" } A practical case for building evaluations early, from someone who does it for a living.

## Interview questions

??? interview rm-refresh "How do you evaluate an LLM application?"
    Build a **test set** of realistic inputs with expected outcomes, ideally taken from real usage. Score outputs with a mix of **code checks** (valid JSON, contains a citation), **LLM-as-judge** for fuzzy qualities like helpfulness, and **human review** on a sample. Run it on every change, so you can see whether a new prompt or model makes things better or worse.

??? interview rm-refresh "What is LLM-as-judge, and what are its risks?"
    Using a (usually strong) LLM to grade another model's output against criteria you write down. It scales far better than human review. Risks: the judge has its own biases (favouring longer answers, or its own style), and its scores drift when you change the judge prompt. Check the judge against a set of human-labelled examples before trusting it.

??? interview rm-refresh "What would you log for an LLM application in production?"
    Every request as a **trace**: the input, the full prompt sent, retrieved documents, tool calls and results, the output, latency, token counts and cost, and the model version. Plus user feedback where you have it. Mind privacy: personal data in prompts needs the same care as any other personal data.
