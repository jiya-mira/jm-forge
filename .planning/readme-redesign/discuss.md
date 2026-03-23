# discuss.md: readme-redesign

**Source:** discuss-log.md

---

## Decisions

### Q1: Target Audience

**结论：** Any user who wants to make their Agent smarter.

- Not limited to developers
- Include hot terms: "Agent Orchestration", "Harness Engineering"
- Appeal to both technical and non-technical users who work with AI agents

### Q2: Narrative Structure

**结论：** Follow suggested structure, but concise.

重点（按优先级）：
1. **Theory/Methodology** — D→P→E, self-bootstrapping, iterative improvement
2. **Design Philosophy** — Maps, not rules; structure, not templates
3. **Academic References** — Cite influential papers (see below)
4. **Practice** — How to install and use (brief)
5. **Architecture** — PROJECT-MAP / RESOURCE-MAP design

**Academic References to Consider:**
- Herbert A. Simon: ["Sciences of the Artificial"](https://hwheelerlab.github.io/How-Advisors-Code/downloads/Simon-Sciences-of-the-Artificial.pdf) — design science methodology
- Allen Newell & Herbert A. Simon: ["Human Problem Solving"](https://www.google.com/books?id=mKZZAAAAMAAJ) — problem solving as search
- Donald Schön: ["The Reflective Practitioner"](https://scholar.google.com/scholar?q=The+Reflective+Practitioner+Donald+Sch%C3%B6n) — reflection-in-action
- Kent Beck: ["Incremental Development"](https://en.wikipedia.org/wiki/Incremental_development_model) — iterative improvement
- John Boyd: ["OODA Loop"](https://en.wikipedia.org/wiki/OODA_loop) — observe-orient-decide-act cycle
- Stuart Russell & Peter Norvig: ["AI: A Modern Approach"](https://aima.cs.berkeley.edu/) — agent architecture

### Q3: Style

**结论：** 偏方法论/有深度

- Self-installation is a feature: let Agent read the repo and decide how to install
- Documentation should be compelling enough that Agent can bootstrap itself
- No废话，文字精炼

### Q4: Architecture Diagrams

**结论:** Mermaid diagrams

### Q5: Language

**结论:** 中英对照（一段英+一段中）

### Q6: Development Environment & Testing

**结论:**

**Development:**
- Tools we actually use: Claude Code, uv, git
- The framework is self-documenting and self-bootstrapping

**Testing:**
- Cross-agent: Test on different AI agents (Claude Code, Codex, etc.)
- Cross-model: Test with different models (Claude Opus, Sonnet, Haiku, GPT-4, etc.)
- The framework should work regardless of which agent executes it

### Q7: Roadmap

**结论:**

Potential future directions:
- Cross-agent resource sharing
- Automated testing harness
- Integration with more agent platforms
- Plugin system for specialized workflows
- Visualization tools for map navigation

### Q8: Contributing

**结论:**

- Open to contributions of all kinds (ideas, code, docs, feedback)
- Provide clear contribution guidelines
- Link to issue tracker / discussion forum
- Emphasize that even non-code contributions (methodology discussions) are welcome

---

## Summary

| # | Decision |
|---|----------|
| 1 | Target: Anyone using AI agents, not just developers |
| 2 | Structure: Theory first, concise practice |
| 3 | Style: 方法论/有深度 + self-install by Agent |
| 4 | Diagrams: Mermaid |
| 5 | Language: 中英对照 |
| 6 | Dev/Testing: Claude Code + uv + git; Cross-agent/model testing |
| 7 | Roadmap: Multiple future directions documented |
| 8 | Contributing: Open guidelines + issue tracker |
