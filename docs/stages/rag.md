---
title: RAG and vector databases
description: Let an LLM answer questions about your own documents by retrieving the relevant parts first.
---

# RAG and vector databases

<p class="rm-lede">Retrieval-augmented generation is asked about in almost every AI Engineer vacancy. Instead of hoping the model knows the answer, you search your own documents first and give the model the relevant passages to answer from.</p>

<div class="rm-meta" markdown>
<span>Stage 2 of 9</span>
<span>About 4 hours</span>
<span>Builds on: LLM foundations</span>
</div>

!!! curating "This stage is being curated"
    The biggest gap from the traineeship, so it will get the most depth. Resources are being selected, including how to create embeddings for free on your own laptop.

## Interview questions

??? interview rm-refresh "Explain RAG to a non-technical stakeholder."
    The model is like a smart new colleague who has never seen our documents. RAG means: before answering, they first look up the most relevant pages in our archive and answer based on those pages, ideally citing them. That keeps answers grounded in our own information and up to date without retraining the model.

??? interview rm-refresh "How do you choose a chunk size?"
    There is no universal best size; it is a trade-off. Small chunks match questions precisely but lose context; large chunks keep context but dilute the match and use more of the prompt. Start from the document structure (paragraphs, sections), add some overlap, and then **measure** retrieval quality on real questions with a few sizes instead of guessing.

??? interview rm-refresh "Your RAG system gives wrong answers. How do you find out why?"
    Split the problem in two. First check **retrieval**: for the failing questions, were the right passages retrieved at all? If not, look at chunking, the embedding model, or add keyword search (hybrid) and reranking. If the right passages *were* retrieved, the problem is **generation**: the prompt, the model, or too much irrelevant context. Build a small set of test questions with known answers so you can measure each fix.
