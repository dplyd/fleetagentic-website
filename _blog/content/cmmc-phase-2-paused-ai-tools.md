---
title: "CMMC Phase 2 is Paused For Now. Here's What What Means for CUI and AI Tools"
date: 2026-10-13T08:00:00-04:00
author: "Kendall Miller"
eyebrow: "Defense"
slug: "cmmc-phase-2-paused-ai-tools"
summary: "DoD suspended CMMC Phase 2 in July 2026. Your DFARS 7012 and NIST 800-171 obligations did not pause. What changed, what didn't, and how AI fits."
draft: false
---

*The November 10 deadline has shifted, but DFARS 7012 is still an expectation. CMMC Phase 2 will be back.*

**tl;dr**
- On July 13, 2026, the Department suspended CMMC Phase 2, which was due November 10, 2026, due to it's suspension, many people think they no longer need to worry about it.
- Phase 1 self-assessments are still enforced.
- Any AI tool that touches CUI (Controlled Unclassified Information) is within scope—including the index of that data you may be sharing with a frontier model.


### What changed

On July 13, 2026, the Department of War, maybe forever in our hearts and minds as DoD, suspended Phase 2 and launched a 60-day review. Phase 2 would have made a Level 2 certification from a third-party assessor (C3PAO) a pre-requisite for award for many contractors and contracting companies with access to CUI. Phases 3 and 4 are frozen for now, but make no mistake, these standards are going to come back. 

On September 3, new rules directed contracting officers to remove third-party CMMC requirements. Certificates already issued are still valid (congrats if you did one). We found the Cyber AB reported only 1,391 final Level 2 certificates as of May 2026 (meaning there are a LOT of places that haven't yet complied).

### What did not change

The certification date requirement is the only thing that _moved_ —it's not gone forever. You are still required to maintain adequate security and incident reporting even now, and you'll be expected to be back at CMMC level 2 when the standards return. Unless an assessor is involved, the affirmation is your own statement to the government, and if the controls aren't real, you'll still be in trouble.

### The precedent

You may recall there was a pause in 2021, so this isn't unprecidented. And when that pause ended it streamlined CMMC 2.0, and the program was reshaped, not removed/repealed. If you're a contractor spending this pause time fixing architecture you'll be ahead in every important outcome. Estimates of how many companies need Level 2 differ, roughly 80,000 by the Department's figures and 118,000 by figures other cite, but nobody disputes the fact that FAR more companies will require it.

### Where AI expands your scope

With AI, every AI tool that processes, stores, or indexes CUI is a part of the system you will need to assess: the model, the interface, the logs and, as we cover in {{< postlink "why-the-index-is-the-leak" "Why the Index Is the Leak" >}}, the search index. If those are uploaded to a frontier model's cloud, your "boundary" now includes that environment. Adding AI after you've documented your boundary means revisiting your system security plan, diagrams and data flows. Shadow IT use, like a browser tab to a consumer chatbot, is a data flow you wont be able to afford ({{< postlink "shadow-ai-regulated-firms" "Shadow AI" >}}). The easiest way to keep that from happening is to offer easily accessible AI inside the boundary you already defend.

### A no-regrets checklist for Q4

1. Define your CUI boundary in writing.
2. Create an inventory of every AI tool your company uses, shadow IT or not.
3. Decide where AI might touch CUI, and create an approved option.
4. Check every "implemented" control in your affirmations against evidence.
5. Ask each AI vendor to give you in writing where prompts, files, embeddings and logs are stored.
6. Put the report on your calendar and re-check regularly.

### How Fleet Agentic fits

Fleet Agentic was designed from the start to meet the standard of CMMC. The model, index, embeddings, and logs run inside your network, so adding AI won't add a third-party system or cloud to your "boundary." Sentinel produces exportable evidence for an assessor or to back your own affirmation. See our [defense case study](/case-studies/defense-cmmc/).

### Using the pause well

Plan your work. In the first 30 days, confirm the "boundary" and inventory your AI tools—including finding out what your people are truly using. In days 30 to 60, ensure you have no gaps: multi-factor authentication, logging, segmentation, and a written AI policy. In days 60 to 90, test you are collecting the right evidence well by asking someone outside the project to produce it for a week—this will dramatically speed up your audit time when it comes. If you wait, you will do the same work later but under pressure, with less say in how it's done and it will very likely cost you more.

### Frequently asked questions

**Is CMMC canceled?** No. Phase 2 is suspended _for now_ and third-party requirements are being removed from solicitations for now. The underlying clauses and standards aren't going anywhere.

**Do I need to act by November 10?** That date no longer triggers new requirements. Existing requirements continue.

**Is my Level 2 certificate still valid?** Issued certificates remain valid. Ask your assessor about maintenance as the review concludes. Also, pat yourself on the back. Well done.

### Get AI inside your boundary

**[Book a 30-minute walkthrough](https://cal.com/kdplyd/30min)** or visit our [defense page](/solutions/defense/).

**Sources:** Crowell & Moring (July 2026); Covington, Inside Government Contracts (September 2026); governmentcontractslaw.com; DoD CIO CMMC page; 32 CFR Part 170; Class Deviation 2026-O0025 Rev. 3.
