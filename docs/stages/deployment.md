---
title: Docker and deployment
description: Turn a notebook into a service that runs the same way everywhere.
---

# Docker and deployment

<p class="rm-lede">Vacancies ask for applications, not notebooks. This stage takes a working prototype and wraps it in an API, puts it in a container, and gets it running somewhere other than your laptop.</p>

<div class="rm-meta" markdown>
<span>Stage 5 of 9</span>
<span>About 3.5 hours</span>
<span>Builds on: your Azure and Git experience</span>
</div>

!!! curating "This stage is being curated"
    Course sections and exercises are being selected.

## Learn

- [Docker: Get started](https://docs.docker.com/get-started/){ .rm-item .rm-refresh data-source="Docs · Docker" data-time="30 min" } What images and containers are, and how to build and run your first one.
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/){ .rm-item data-source="Docs · FastAPI" data-time="1 hour" } Turn a Python function into a web API with automatic documentation.

## Interview questions

??? interview rm-refresh "What problem does Docker solve?"
    "It works on my machine." A container packages your code together with its exact dependencies and runtime, so it runs the same on your laptop, in CI, and in the cloud. It also makes deployments repeatable: you ship an image, not a list of installation steps.

??? interview rm-refresh "How would you serve an LLM application to other teams?"
    Wrap it in an **API** (for example FastAPI) with a clear request and response schema, put it in a **container**, and run it on a managed platform such as Azure Container Apps. Add authentication, rate limiting, timeouts for slow model calls, and logging. Keep API keys in a secret store, never in the image.

??? interview rm-refresh "LLM calls are slow. How do you keep the application responsive?"
    **Stream** the response so users see text immediately; make calls **asynchronous** so one slow request doesn't block others; **cache** answers to repeated questions; and use a smaller, faster model for simple steps. Long-running agent tasks can run as background jobs that the user checks on later.
