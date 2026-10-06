---
title: AI Engineer Roadmap
hide:
  - navigation
  - toc
---

<section class="rm-hero">
  <p class="rm-eyebrow">For data science trainees</p>
  <h1 class="rm-hero-title">From data scientist<br>to <em>AI Engineer</em></h1>
  <p class="rm-hero-text">The topics Junior AI Engineer vacancies ask for that the traineeship doesn't cover yet: what to learn, where to learn it, and the interview questions to practise. Your progress is saved in this browser.</p>

  <div class="rm-hero-actions">
    <a id="rm-continue" class="rm-button rm-button--primary" href="stages/llm-foundations/">Start with stage 1</a>
    <div class="rm-route-toggle" role="group" aria-label="Choose a route">
      <button type="button" data-route="full" aria-pressed="true">Full route <span>25–30 h</span></button>
      <button type="button" data-route="refresh" aria-pressed="false">Refresh <span>half a day</span></button>
    </div>
  </div>

  <dl class="rm-stats">
    <div><dt>Stages done</dt><dd id="rm-stages-done">0</dd></div>
    <div><dt>Items ticked off</dt><dd id="rm-items-done">0</dd></div>
    <div><dt>Questions to review</dt><dd id="rm-review-count">0</dd></div>
  </dl>
</section>

<section class="rm-roadmap" aria-label="Roadmap stages">
  <a class="rm-stage-card" href="stages/llm-foundations/" data-stage="stages/llm-foundations/">
    <span class="rm-stage-number">01</span>
    <span class="rm-stage-body">
      <span class="rm-stage-title">LLM foundations</span>
      <span class="rm-stage-text">Tokens, prompting, structured output and embeddings: what you are actually calling.</span>
    </span>
    <span class="rm-stage-side"><span class="rm-stage-hours">3 h</span><span class="rm-stage-progress">–</span></span>
  </a>
  <a class="rm-stage-card rm-stage-card--key" href="stages/rag/" data-stage="stages/rag/">
    <span class="rm-stage-number">02</span>
    <span class="rm-stage-body">
      <span class="rm-stage-title">RAG and vector databases <span class="rm-tag">Biggest gap</span></span>
      <span class="rm-stage-text">Answer questions about your own documents by retrieving the right passages first.</span>
    </span>
    <span class="rm-stage-side"><span class="rm-stage-hours">4 h</span><span class="rm-stage-progress">–</span></span>
  </a>
  <a class="rm-stage-card" href="stages/agents/" data-stage="stages/agents/">
    <span class="rm-stage-number">03</span>
    <span class="rm-stage-body">
      <span class="rm-stage-title">Agents and tool calling</span>
      <span class="rm-stage-text">Let the model choose tools in a loop, and know when a fixed workflow is better.</span>
    </span>
    <span class="rm-stage-side"><span class="rm-stage-hours">4 h</span><span class="rm-stage-progress">–</span></span>
  </a>
  <a class="rm-stage-card" href="stages/evaluation/" data-stage="stages/evaluation/">
    <span class="rm-stage-number">04</span>
    <span class="rm-stage-body">
      <span class="rm-stage-title">Evaluation and observability</span>
      <span class="rm-stage-text">Turn "it looked fine" into numbers, and trace what happens in production.</span>
    </span>
    <span class="rm-stage-side"><span class="rm-stage-hours">3 h</span><span class="rm-stage-progress">–</span></span>
  </a>
  <a class="rm-stage-card" href="stages/deployment/" data-stage="stages/deployment/">
    <span class="rm-stage-number">05</span>
    <span class="rm-stage-body">
      <span class="rm-stage-title">Docker and deployment</span>
      <span class="rm-stage-text">From notebook to an API in a container that runs the same everywhere.</span>
    </span>
    <span class="rm-stage-side"><span class="rm-stage-hours">3.5 h</span><span class="rm-stage-progress">–</span></span>
  </a>
  <a class="rm-stage-card" href="stages/security/" data-stage="stages/security/">
    <span class="rm-stage-number">06</span>
    <span class="rm-stage-body">
      <span class="rm-stage-title">LLM security</span>
      <span class="rm-stage-text">Prompt injection, data leakage and how to limit the damage.</span>
    </span>
    <span class="rm-stage-side"><span class="rm-stage-hours">2.5 h</span><span class="rm-stage-progress">–</span></span>
  </a>
  <a class="rm-stage-card" href="stages/mcp-skills/" data-stage="stages/mcp-skills/">
    <span class="rm-stage-number">07</span>
    <span class="rm-stage-body">
      <span class="rm-stage-title">MCP and skills <span class="rm-tag rm-tag--muted">Less urgent</span></span>
      <span class="rm-stage-text">Standard ways to plug tools, data and instructions into any agent.</span>
    </span>
    <span class="rm-stage-side"><span class="rm-stage-hours">3 h</span><span class="rm-stage-progress">–</span></span>
  </a>
  <a class="rm-stage-card" href="stages/multi-agent/" data-stage="stages/multi-agent/">
    <span class="rm-stage-number">08</span>
    <span class="rm-stage-body">
      <span class="rm-stage-title">Multi-agent systems</span>
      <span class="rm-stage-text">Several agents working together, and why that is often not the answer.</span>
    </span>
    <span class="rm-stage-side"><span class="rm-stage-hours">2 h</span><span class="rm-stage-progress">–</span></span>
  </a>
  <a class="rm-stage-card rm-stage-card--final" href="stages/final-project/" data-stage="stages/final-project/">
    <span class="rm-stage-number">09</span>
    <span class="rm-stage-body">
      <span class="rm-stage-title">Final project <span class="rm-tag rm-tag--muted">To be decided</span></span>
      <span class="rm-stage-text">One project that brings everything together, to demo in an interview.</span>
    </span>
    <span class="rm-stage-side"><span class="rm-stage-hours">TBD</span><span class="rm-stage-progress">–</span></span>
  </a>
</section>

<section class="rm-about" markdown>

## Why this site exists { #why }

<!-- PLACEHOLDER: rewrite this section in your own words. -->

After interviewing for a Junior AI Engineer role, it became clear that the traineeship covers a lot of what these roles need (Python, Git, cloud, data pipelines, working with stakeholders) but not the LLM-specific parts: RAG, agents, evaluation and deployment. This roadmap collects the best resources for those gaps in one place, in a sensible order, together with the questions interviewers actually ask.

## How to use it { #how }

<div class="rm-steps" markdown>

1. **Pick a route.** The *full route* touches every topic in about 25–30 hours. The *refresh* shows only the essentials, about half a day, for just before an interview.
2. **Work through the stages in order.** Each stage lists what to learn, exercises to practise, and optional resources to go deeper. Tick items off as you go.
3. **Practise the interview questions.** Try to answer out loud first, then open the answer. Mark each question *could answer* or *need to review*, and use the filter to revisit the ones you struggle with.
4. **Back up your progress.** Progress lives in this browser only. Use *export* below now and then, and *import* on another laptop to continue there.

</div>

Courses on Udemy and DataCamp are covered by the traineeship subscriptions. Some exercises call an LLM from code; read [Setup and costs](setup.md) before you start those.

</section>

<section class="rm-backup" aria-label="Back up your progress">
  <div>
    <h2>Your progress</h2>
    <p>Saved in this browser only. Export a backup file to keep it safe or to move it to another laptop.</p>
    <p class="rm-backup-status" id="rm-backup-status" role="status"></p>
  </div>
  <div class="rm-backup-actions">
    <button type="button" class="rm-button" id="rm-export">Export progress</button>
    <label class="rm-button rm-button--ghost">Import progress<input type="file" id="rm-import" accept="application/json,.json"></label>
  </div>
</section>
