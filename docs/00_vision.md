# Lisa Vision

Lisa is a chat-native, self-improving agentic assistant.

Lisa exists to help the user plan, reason, build, test, learn, and improve projects through controlled chat-based automation.

Lisa must feel powerful, but it must not become reckless.

---

## 1. Product Identity

```txt
Name: Lisa
Type: Chat-native agentic assistant
Primary channel: Telegram
Secondary channels: Slack and WhatsApp
Interface model: Chat only
Dashboard: None
Execution style: Policy-controlled, sandboxed, auditable
```

Lisa is not a chatbot wrapper around tools. Lisa is an agentic operating core that communicates through chat.

---

## 2. What Lisa Should Become

Lisa should become a long-term assistant that can:

- Understand user goals.
- Break goals into practical plans.
- Re-evaluate plans for feasibility.
- Rank and refine plans until they cross a quality threshold.
- Use RAG memory to recall project context.
- Run sandboxed DevShell sessions.
- Propose code patches.
- Run tests and evals.
- Discover MCPs and tools.
- Quarantine risky external tools.
- Create candidate skills.
- Learn from mistakes.
- Send morning reports.
- Notify the user through Telegram about every meaningful update.

---

## 3. What Lisa Must Never Become

Lisa must not become:

- An unrestricted shell agent.
- A hidden automation bot.
- A tool installer that trusts random MCPs.
- A memory system that stores unverified internet content as truth.
- A self-modifying runtime without approval.
- A production deployment bot without validation.
- A web-dashboard SaaS project.

Lisa is chat-native and governance-first.

---

## 4. Interface Philosophy

The user should not need to open a dashboard.

Everything should happen through:

```txt
Telegram
Slack
WhatsApp
```

Telegram is the primary live-control channel.

Every meaningful action must be reported to Telegram.

---

## 5. Build Philosophy

Lisa is also a learning project.

Every implemented module should teach the developer:

- What the concept is.
- Why it exists.
- How it works.
- What can go wrong.
- How tests prove safety.

This means the repository must include both production code and deep documentation.

---

## 6. First Build Objective

The first implementation milestone is not tool execution.

The first milestone is the planning core:

```txt
Chat command
→ Unified Chat Gateway
→ Intent Firewall
→ Planner Brain
→ Universal Plan Tokenizer
→ Feasibility Brain
→ Ranker Brain
→ Threshold check
→ Re-loop if needed
→ Final plan returned through Telegram
```

This proves Lisa can think, compress, evaluate, and explain before it touches real systems.
