# Mobile App Launcher — Operational Playbook

All reference data, tool specs, step-by-step sequences, and benchmark figures for the mobile-app-launcher skill.

## Table of Contents

1. [Core Thesis](#1-core-thesis)
2. [Phase 1: Idea Validation](#2-phase-1-idea-validation)
   - Five Money Markets
   - Validation Toolkit
   - Validation Checklist
3. [Phase 2: MVP Build](#3-phase-2-mvp-build)
   - Design Workflow
   - Development Options
   - Hiring Gaps
4. [Phase 3: Five-Step Funnel](#4-phase-3-five-step-funnel)
5. [Phase 4: Organic Content](#5-phase-4-organic-content)
   - Content Formula
   - Market Research Workflow
6. [Phase 5: App Store, Onboarding, Paywall](#6-phase-5-app-store-onboarding-paywall)
   - App Store Requirements
   - Onboarding Sequence (7 Steps)
   - Paywall Priming Sequence
7. [Phase 6: Scaling](#7-phase-6-scaling)
   - Organic-to-Paid Pipeline
   - Influencer Strategy
   - Key Metrics
8. [Benchmark Data](#8-benchmark-data)
9. [Exit Strategy](#9-exit-strategy)

---

## 1. Core Thesis

In 2026, AI has made app building trivially accessible via vibe coding tools. The differentiation no longer lives in the build; it lives in distribution. Two apps with identical features will have radically different revenue curves based entirely on marketing execution.

**Structural implication:** Every resource allocation decision — time, money, attention — should be evaluated against whether it improves distribution before it improves product.

**Corollary:** A bad app with excellent marketing beats a perfect app with no marketing. Validated example from the field: an app called "Taller" that claims to physically increase height generated $10,000 in a single month on marketing alone, despite the core premise being physiologically impossible.

---

## 2. Phase 1: Idea Validation

### Five Money Markets

Target ideas within markets where people willingly, repeatedly pay for solutions:

| Market | Driver | Example App |
|---|---|---|
| Health | Remove pain, extend life | PuffCount (quit vaping), MyFitnessPal |
| Wealth | Make or save money | Any finance/budgeting app |
| Relationships | Find or improve connection | Tinder, Hinge, Bumble |
| Status | Look good, signal value | Instagram, BeReal |
| Convenience | Save time, reduce friction | Spotify, Uber |

An idea that doesn't fit any of these five markets is not invalid — but the burden of proof is higher. Default to these markets when uncertain.

### Validation Toolkit

**Sensor Tower**
- Input: any app name
- Output: monthly installs, monthly revenue estimates
- Use to: confirm competitors are making real money in your niche
- Reference benchmarks: MyFitnessPal ~$12M/month; Carb Manager ~$200k/month; Body Fast ~$100k/month

**Viral Ad Library**
- Browse by app category
- Filter to see most-viral organic and paid video content per competitor
- Use to: identify content formats that work *before* you create anything
- If a competitor's content is consistently going viral, the format is validated; replicate it for your product

**Flippa / Acquire**
- Marketplaces where founders sell app businesses
- Use to: confirm real revenue exists in your category (and get detailed P&L if a listing includes financials)
- Reference data: QR code scanner listed at $25M on $14M/year revenue; storage cleaner app at $12M on $5M/year revenue
- Secondary use: see tech stacks and business models of operating apps in your niche

**Google Trends**
- Input: core keyword(s) for your niche
- Output: search volume direction (rising / flat / declining)
- Validated example: "quit vaping" was at all-time high search volume at PuffCount's launch
- January spike pattern: Health apps reliably see massive volume during New Year's resolution window — factor this into launch timing
- New angle signal: if "[niche] + AI" is trending sharply upward, that keyword combination is a differentiation opportunity

**TikTok / Instagram Social Search**
- Search your niche keywords on both platforms
- Sort results by likes
- If viral content already exists in your niche (multiple videos at 20k+ likes), distribution is proven
- If no viral content exists, distribution is unproven — higher risk even if demand data looks good

### Validation Checklist (minimum threshold)

Before committing to build, confirm all four:

- [ ] Niche fits one of the five money markets
- [ ] At least one competitor has confirmed revenue via Sensor Tower (or Flippa listing)
- [ ] Viral content for the niche keyword exists on TikTok or Instagram
- [ ] Google Trends shows stable or rising search volume

Fail on two or more: REJECTED. Fail on one: INCONCLUSIVE — do more research before building. Pass all four: VALIDATED.

---

## 3. Phase 2: MVP Build

### Core Principle

Ship the minimum viable product as fast as possible. Bugs are acceptable at launch. Real user feedback and revenue data are more valuable than a polished product nobody has seen.

**Anti-pattern to avoid:** Endless development cycles (building for months or years without launching). Development is never "done." The correct order is: launch → revenue → iterate, not: perfect → launch.

Validated data point: Posted's first version (FlutterFlow) had broken icons and messed-up images. Launched anyway. Revenue and feedback came in immediately.

### Design Workflow

Execute in this exact sequence — do not skip steps:

1. **Brain dump (paper only):** Write down the problem statement, a list of competitors, a feature list with a one-sentence explanation for each feature, and a note on the marketing potential of each feature. Marketing potential matters during feature planning; features that cannot be shown in a 15-second video are lower priority.

2. **Hand-sketch screens:** Rough wireframes of the core screens. Keep on file — these sketches are the canonical record of the original intent.

3. **Screens.design:** Browse the full UI library for top apps (Airbnb, MyFitnessPal, Duolingo, and others). These companies spent millions optimizing UX. Copy screen designs into Figma as inspiration. This is not plagiarism — this is compression of millions in UX research.

4. **99designs contest:** Post a design brief with your hand-sketches and Screens.design references. Hundreds of professional designers submit fully built custom UIs. Pay only for the winner; reject everything else. Cost: a few hundred dollars. Output: a complete, professional UI design in Figma. Design phase ends here.

### Development Options

**Base44 (primary recommendation)**
- Chat-based AI vibe coding; iterative back-and-forth feature building
- Figma import: upload your Figma designs as the base layer; Base44 builds on top
- GitHub sync: push full codebase to GitHub, then continue in Cursor or Claude Code
- Direct App Store publishing: generates App Store files and submits from within the platform
- Plan mode: available for structured feature building sessions
- Partnership note: if enrolling in the App Accelerator program, Base44 is the required platform (yearly Starter plan ~$200/year after 30% discount)

**Other vibe coding tools (secondary)**
- Roark
- Emergent
- Cursor
- Claude Code

**Honest ceiling on vibe coding:** Gets you 70-90% of the way. Complex backend features and security-sensitive logic may require a human developer. Do not abandon the project at this point — hire to finish the last 10-20%.

### Hiring Gaps (Upwork Protocol)

When vibe coding hits its ceiling:
- Post a job on Upwork
- Target Eastern Europe: top-quality code at roughly half US cost
- Mandatory pre-hire step: run a 5-10 minute screening call before releasing any work
- Payment: Upwork holds funds in escrow — do not pay outside the platform

---

## 4. Phase 3: Five-Step Funnel

Every user passes through all five steps sequentially. A leak at any step blocks scaling. Identify the first leak before touching anything downstream.

| Step | Name | Job | Leak symptom |
|---|---|---|---|
| 1 | Organic content | Drive traffic | Views but no App Store visits |
| 2 | App Store listing | Convert views to downloads | App Store views but no installs |
| 3 | Onboarding | Engage and prime for purchase | Installs but no paywall views |
| 4 | Paywall | Convert free to paying | Paywall views but no conversions |
| 5 | Scaling | Amplify proven funnel | Profitable but slow growth |

**Diagnostic rule:** Do not run paid ads until steps 1-4 are confirmed working. Paid ads amplify the existing funnel — they cannot fix a broken one.

---

## 5. Phase 4: Organic Content

### Context

80% of Posted's $100k+/month revenue came from organic content (Instagram, TikTok, YouTube, X) before any paid spending. Organic content is the validation layer for paid; it is not a preliminary phase to skip.

### Core Content Rule

**Do not talk about your app.**

Nobody cares about features, price, or where to download. Talking about the app signals "advertisement" to the viewer's brain — the algorithm detects low engagement and suppresses distribution.

The correct model: sell the transformation, not the product.

### Content Formula

```
HOOK (0-3 seconds):
  Present the problem in the most visceral or surprising format possible.
  The hook's only job is to prevent the viewer from scrolling.

MIDDLE (3 seconds to ~25 seconds):
  Deepen the problem, show the lifestyle the viewer wants, or document
  the transformation. Do not mention the app. Build emotional investment.

REVEAL (last 2 seconds):
  Show the product on a home screen or in natural use. No voiceover.
  No feature list. No download CTA. Zero hard sell.
  The viewer's brain makes the connection. That's the mechanism.
```

**Validated example — PuffCount:**
- Video shows creator taking apart a vape: coil, cotton, battery visible
- Viewer confronts what they are physically inhaling
- App shown on home screen for 2 seconds at the end
- Result: 476k likes, 8M organic views, tens of thousands of installs
- No product pitch. No CTA. Just a problem, made visceral.

**Validated example — CalAI ($3M/month):**
- Shows dream healthy lifestyle footage
- 2-second product placement at the end
- 70k likes on the validated format
- No feature pitch whatsoever

### Market Research Workflow (run before creating any content)

1. Search niche keywords on TikTok and Instagram
2. Sort results by likes; pull the top 5-10 most viral videos
3. Log each video in a spreadsheet: topic, hook type, middle structure, format (talking-head / B-roll / tutorial / reaction), platform
4. Recreate those formats adapted to your product
5. Post volume (multiple formats, multiple angles) until one hits
6. Once a format goes viral, replicate it indefinitely — do not rotate away from a winning format prematurely

**Key insight:** PuffCount's mega-viral videos were based on formats already validated by other creators. The creative insight was adaptation, not origination. Do not invent when you can adapt.

**Creator delegation:** You do not need to appear on camera. You can write a brief, send reference videos, and have a creator execute. This is the default operating model once content volume exceeds what the founder can produce solo.

---

## 6. Phase 5: App Store, Onboarding, Paywall

### App Store Requirements (three non-negotiable elements)

1. **Rating:** 5 stars or as close as possible. Below 4.5 and download conversion drops measurably.
2. **Screenshots:** Show the value and transformation, not the feature list. Every top-grossing app (Duolingo $30M/month, MyFitnessPal $12M/month, Posted $150k+/month) uses transformation-first screenshots.
3. **Written reviews:** Strong social proof in text reviews. Solicit these aggressively via onboarding.

### Onboarding Sequence (7 Steps)

This is the structure used by CalAI, Flow ($10M/month), Duolingo, and every major app. Deviate from it only with A/B test evidence.

| Step | Screen | Purpose |
|---|---|---|
| 1 | Welcome screen | Reaffirm the download decision. "Congratulations, you're on your way to a healthier lifestyle." Reduce cognitive dissonance immediately. |
| 2 | Sign-in screen | Capture identity. Required before personalization. |
| 3 | Value screens | Show features they're about to access. Build anticipation. |
| 4 | Rating prompt | Ask for a review BEFORE the user has left the app the first time. Cheat code for App Store ratings. Most users will rate 5 stars if prompted while still in the positive decision frame from download. |
| 5 | Social proof screen | Add after 500k installs. Optional for early stage. |
| 6 | Long user survey | This is the highest-leverage screen in the onboarding. Ask deep questions about the specific problem your app solves. The survey is not data collection — it is a pain activation mechanism. |
| 7 | Hard paywall | No X button. No free access without commitment. Free trial option only. |

**Survey design principle (Step 6):**
Questions should make the user think deeply about their problem. Each question increases the psychological distance between their current state and their desired state — making the paywall feel like the logical solution, not an obstacle.

PuffCount survey examples:
- "How long have you been vaping?"
- "Have you tried to quit before?"
- "Which side effects have you noticed?"
- "How much do you spend per month on vaping?"
- [Calculated output]: "You spend $X per year on vaping." (shows the number — triggers urgency)

The calculation reveal at the end of the survey is the single most effective conversion trigger in the onboarding flow.

**Step 7 — Paywall mechanics:**
- No X button: the user must engage with the paywall, not dismiss it
- Free trial is the only path to free access — requires commitment (email, payment method)
- No free tier without any commitment

**PuffCount post-implementation conversion rate: 30%.**

### Paywall Priming Screens

Insert these three screens BEFORE the actual paywall (between Step 6 and Step 7):

| Screen | Content | Mechanism |
|---|---|---|
| Priming 1 | "We want you to try [App] for free." | Soft commitment framing. Removes adversarial dynamic. Builds trust before asking for payment info. |
| Priming 2 | "We'll send you a reminder before your free trial ends." | Opt-in for push notifications (retention mechanism). Surfaces as consent, not as a marketing grab. |
| Priming 3 | Actual paywall | User arrives in a cooperative frame. |

**CalAI paywall tactic:** Free trial is only available on the yearly plan. The monthly plan requires immediate payment. This forces any user who wants to try free to commit to the annual subscription. Duolingo uses the same mechanic ("We'll remind you 2 days before your trial ends" → pushes yearly plan).

Operational implication: if your conversion rate is below 20%, the priming screens are the first place to audit.

---

## 7. Phase 6: Scaling

### Organic-to-Paid Pipeline

**The rule:** Take the organic videos that proved themselves (high views, measurable installs) and run them as paid ads. Do not create new creative for paid until organic creative is exhausted.

Logic: if a format works organically, it will work on paid. The only variable you're adding is money. Zero guesswork, zero wasted spend on unvalidated creative.

**PuffCount paid ad benchmark data:**
- Cost per install (CPI): $0.16 to $0.50 depending on campaign
- One campaign result: 30,000 installs
- LTV per install (via RevenueCat): $0.90 to $1.50 depending on month
- Effective return: doubling money on every dollar spent at $0.50 CPI / $1.00 LTV

**Campaign types to AB test:**
- Install campaigns (optimize for download volume)
- Free trial start campaigns (optimize for trial activation)

### Key Metrics (must know before scaling paid)

| Metric | Definition | Source | Decision rule |
|---|---|---|---|
| CAC | Cost per install from ad platform | Ad platform dashboard | Target: as low as possible |
| LTV | Revenue per install over lifetime | RevenueCat | Must exceed CAC before scaling |
| MRR | Monthly recurring revenue | RevenueCat or Stripe | Primary business health metric |
| Conversion rate | Free installs → paying customers | RevenueCat | Target: 20-30% with optimized onboarding |

**RevenueCat** is the default tool for LTV tracking. It integrates directly with both iOS and Android and tracks subscription state, churn, and lifetime value per install cohort.

**Scale decision rule:** If LTV > CAC, scale. If not, fix the funnel first. Scaling a negative-LTV funnel accelerates losses.

### Influencer and Creator Strategy

**Old model (broken):**
- Manually DM or email hundreds of creators
- ~50% non-response rate
- Survivors frequently overcharge
- Content often lazy and misaligned with the niche

**New model (current standard):**
- Creators apply to work with you — you select and pay only for results or for content you want to boost
- Find creators already making content in your niche: their audience is pre-qualified (they already have the problem your app solves)
- When that creator posts about your app, it feels like a recommendation, not an ad — conversion rate difference is material
- Brief: provide reference videos (from your viral format research), a one-page product brief, and the transformation narrative. Creators execute.

**Validated result:** Steven Grabada received 5,000 installs in a single day from one influencer video.

### Ongoing Scaling Loop

- Always be AB testing: content formats, ad creatives, onboarding flows, paywall structures
- Build processes and systems that let the business run without the founder's daily involvement
- Once the business operates on autopilot, it becomes an acquirable asset

---

## 8. Benchmark Data

| App | Revenue | Source / Notes |
|---|---|---|
| CalAI | $3M/month | Calorie tracking, AI features |
| Duolingo | $30M/month | Language learning |
| MyFitnessPal | $12M/month | Fitness / calorie tracking |
| Flow (period tracking) | $10M/month | Women's health |
| Body Fast | $100k/month | Fasting |
| Carb Manager | $200k/month | Keto / low-carb diet tracking |
| PuffCount (pre-exit) | $45k/month | Quit vaping |
| Posted | $150k+/month | At time of webinar; $823k trailing 6 months |
| Recime | $2M/month | Recipe app (used as Base44 live demo) |

**Student outcome data (Grabada cohort):**
- Vince (software dev, no marketing background): $20k/month, first $1k day
- Simon (software dev): $0 → $20k+/month in 5 months; now >$100k MRR
- Key (non-developer): $10k MRR from idea only
- Multiple others (Rick, Alan, Attila, Jesus, Aleem, Kevin): all operating 6-figure app businesses

**PuffCount organic content metrics:**
- Top video: 476k likes, 8M organic views
- TikTok following built: 120k followers, 50M organic views total
- Exit: well over 7 figures; reached #1 in Lifestyle charts above Pinterest, Tinder, Bumble, Hinge

---

## 9. Exit Strategy

**Who buys:**
- Larger companies looking for validated user bases and autopilot revenue streams
- Strategic acquirers who can inject their own budget to scale an already-proven funnel

**Valuation basis:** Multiple of annual recurring profit. Apps doing $5-10k/month with good retention and documented systems are already worth 6 figures.

**What buyers want:**
1. Autopilot operations (no founder-dependency)
2. Proven CAC/LTV ratio
3. Strong retention data
4. Documented systems and processes

**Build for exit from Day 1:** Document processes, build systems, ensure the business can run without you. This discipline also prevents founder burnout and enables the business to scale past the founder's personal capacity.

**Marketplaces:** Flippa, Acquire (secondary use — also useful for competitive research during validation).

---

*Reference data sourced from Steven Grabada webinar, 2026. All revenue figures are reported figures, not independently verified. Use as directional benchmarks, not guarantees.*
