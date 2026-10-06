---
title: Multi-agent systems
description: Several agents working together, and why that is often not the answer.
---

# Multi-agent systems

<p class="rm-lede">Multi-agent systems split a task over several specialised agents. They can handle large, parallel research tasks, but they also multiply cost and failure points. Interviewers mostly want to hear that you know when <em>not</em> to use them.</p>

<div class="rm-meta" markdown>
<span>Stage 8 of 9</span>
<span>About 2 hours</span>
<span>Builds on: agents, evaluation</span>
</div>

!!! curating "This stage is being curated"
    Course sections and exercises are being selected.

## Learn

- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system){ .rm-item .rm-refresh data-source="Article · Anthropic" data-time="25 min" } An honest account of where multiple agents help, and what they cost.
- [Don't build multi-agents](https://cognition.ai/blog/dont-build-multi-agents){ .rm-item data-source="Article · Cognition" data-time="15 min" } The counter-argument: why sharing context between agents is hard.

## Interview questions

??? interview rm-refresh "When would you use multiple agents instead of one?"
    When a task splits into **independent parts that can run in parallel**, such as researching several topics at once, or when one agent's context would overflow. Each sub-agent works in its own context and returns a short summary to an orchestrator. For tasks where every step depends on the previous one, a single agent is simpler and more reliable.

??? interview rm-refresh "What are the downsides of multi-agent systems?"
    Much higher **token cost** (each agent has its own context), more **failure points**, agents working from **inconsistent information**, and much harder **debugging** and evaluation. Many problems that look multi-agent are better solved by one agent with good tools, or by a fixed workflow.

??? interview rm-refresh "Describe the orchestrator–worker pattern."
    An **orchestrator** agent breaks the task into sub-tasks, hands each to a **worker** agent (often in parallel), and combines their results. Workers only get the context they need for their piece. The orchestrator decides whether the combined result is good enough or whether more work is needed.
