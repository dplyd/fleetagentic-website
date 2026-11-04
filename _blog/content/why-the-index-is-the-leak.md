---
title: "Why the Index Is the Leak: How AI Search Copies Sensitive Data Off-Site"
date: 2026-09-28
author: "Kendall Miller"
eyebrow: "Explainer"
slug: "why-the-index-is-the-leak"
summary: "Your files stayed put, but the AI index built from them did not. What it contains, what research shows it can reveal, and five vendor questions."
draft: false
---

*Your files never left the building. Their meaning did.*

**In short**
- An AI "index" is a second, searchable copy of your documents: keywords, snippets, embeddings and metadata.
- Published research shows embeddings can be turned back into the text they came from, so they need the same protection as the source.
- If a vendor hosts your index, where it lives decides your compliance boundary.

### The setup that looks safe

Picture a firm that buys an AI assistant that "works with your documents." The files stay on the local server, and the security questionnaire gets a clean answer: *data at rest remains on-premises.*

But to answer questions, the system has to break each document into chunks and turn each chunk into a list of numbers called an embedding. It stores those numbers, plus text snippets and metadata, in a search index, and in many products that index lives in the vendor's cloud. The files never moved. A queryable copy of what's in them did.

I think this is the most under-asked question in AI procurement, mostly because the answer on the questionnaire is technically true.

### What an AI index contains

An index usually holds five things: keywords that reveal what a document is about, verbatim snippets so the assistant can quote them, embeddings that encode meaning, metadata like file names, authors and access labels, and relationships between documents and entities. You couldn't safely publish it as a summary. It's a working copy built for retrieval, which is exactly what an attacker, a subpoena or a curious insider goes after.

### What the research shows

For years people assumed embeddings were opaque. That assumption hasn't held up. Cornell researchers Morris, Kuleshov, Shmatikov and Rush (arXiv 2310.06816) built Vec2Text, which reconstructs text from its embedding. Against GTR-base embeddings it recovered 92 percent of 32-token inputs exactly, and 89 percent of full names in pseudo-re-identified MIMIC-III clinical notes. The authors concluded that embeddings should be protected like raw text.

Later work goes further. ALGEN showed inversion with only a few examples. A 2026 method, Zero2Text, works black-box with no training, and a 2026 survey (arXiv 2607.01276) catalogs the growing family of attacks.

Accuracy depends on the embedding model, the text length and how much access the attacker has — and defenses like noise or secret scaling exist, usually at some cost to retrieval quality. Even so, "we only store vectors, not text" isn't a safety argument anymore.

### Why this becomes a compliance question

Regulated data stays regulated after you transform it. If a derived copy can disclose CUI, PHI, privileged material or student records, a careful assessor or counsel may treat it as in scope. We aren't lawyers, so ask yours: does our vendor's index sit inside the boundary we documented, and can we show evidence?

### Five questions for any AI vendor

1. Where are the embeddings stored? Ask for the location by name.
2. Where is the index queried? Queries run against your data.
3. Who holds the keys? If the vendor can read the index, so can anyone who compromises or compels the vendor.
4. What leaves in telemetry, logs and support bundles? Traces often carry the content you meant to protect.
5. What can you show an assessor? Look for exportable logs of who queried what, and when.

### How Fleet Agentic is built around this

We started from the index instead of the file. The model, retrieval index, embeddings and logs all run on hardware inside your network, and no third-party model API sees your prompts or retrieved passages. Lighthouse handles identity, isolation and segmentation. Sentinel is an immutable audit log with evidence export, so question five gets a report and not a promise. Air-gapped deployment is available, with updates by offline transfer.

### A 20-minute test you can run this week

Pick one AI tool your organization already uses and ask IT to trace a single document through it, on paper. Where is the file read? Where is it split into chunks? Which service turns those chunks into embeddings, and where are the results stored? Where does a question get matched against them? Ask the same about prompts, retrieved snippets and logs. Then draw it as a one-page data-flow diagram. If any box sits outside your network, or IT can't say where it sits, you've found the index. Most teams find at least one copy they didn't expect — and it's a lot cheaper to find it in a diagram than in an incident report.

### Frequently asked questions

**Are embeddings legally "CUI" or "personal data"?** There's no single answer. It depends on the data and the regulation. The research shows embeddings can leak the underlying text, so prudent programs treat them as sensitive. Ask counsel.

**Isn't encrypting the vector database enough?** Not if the vendor holds the keys, decrypts to query, or stores snippets and metadata next to the vectors.

**Does on-premises remove all AI risk?** No. It removes one category of third-party exposure and makes the boundary auditable. You still need access control, logging and policy.

### See where your index lives

Book a 30-minute walkthrough on your own data. **[Schedule it](https://cal.com/kdplyd/30min)**

**Sources:** Morris et al., arXiv 2310.06816; arXiv 2607.01276; [fleetagentic.ai/learn/the-index-is-the-leak](https://fleetagentic.ai/learn/the-index-is-the-leak/).
