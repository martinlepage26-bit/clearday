# Clearday Progress Tracker

Last updated: 2026-06-29 (run 1)

## 1. Documentation

| Item | Status | Notes |
|------|--------|-------|
| Web repo README | Done | Created with stack, structure, brand, safety notes |
| Mobile repo README | Not started | Separate repo (clearday-mobile) |
| API documentation | Not started | Backend is Base44 cleardayCore2 |

## 2. Theme / Brand Consistency

| Item | Status | Notes |
|------|--------|-------|
| Web meta theme-color | Done | Corrected from #4a7c6a to #2D6A4F |
| Web favicon.svg | Done | Corrected from #4a7c6a to #2D6A4F |
| Bundled CSS/JS colors | Needs review | Cannot rebuild Perplexity Pages bundle locally; may still contain #4a7c6a |

## 3. i18n (Mobile App)

| Item | Status | Notes |
|------|--------|-------|
| EN/FR coverage | ~80% | Per project spec; full audit requires `src/lib/i18n.ts` (56 KB) |
| Untranslated strings | **7 found** | Hardcoded English strings identified in source code (see below) |

### Hardcoded Strings (not using `t()`)

| File | Line | String | Fix |
|------|------|--------|-----|
| `app/(auth)/login.tsx` | 26 | `"Please enter your email and password."` | Add `t("auth.requiredFields")` |
| `app/(auth)/login.tsx` | 33 | `"Login failed."` | Add `t("auth.loginFailed")` |
| `app/(auth)/register.tsx` | 29 | `"Please enter your email and password."` | Add `t("auth.requiredFields")` |
| `app/(auth)/register.tsx` | 38 | `"Registration failed."` | Add `t("auth.registerFailed")` |
| `app/(tabs)/ask.tsx` | 184 | `"New conversation"` | Add `t("nav.newConversation")` |
| `app/(tabs)/ask.tsx` | 432 | `"Flagged — discuss with your clinician"` | Add `t("nav.flaggedEscalation")` |
| `app/(tabs)/settings.tsx` | 255 | `"Account"` (SectionHeader) | Add `t("settings.account")` |

## 4. Code Quality (Mobile App)

| Item | Status | Notes |
|------|--------|-------|
| Test suites (api, backend integration, i18n, utils) | Unknown | Requires clearday-mobile repo access to run |
| ESLint config | Present | eslint-config-expo/flat; 0 errors, 18 warnings across 7 files |
| Production bundle | Builds OK | Android: 1757 modules, iOS: 1675 modules (Metro) |

### ESLint Warnings (18 total, 0 errors)

From ESLint cache analysis — all are unused imports/variables:

| File | Warning | Fix |
|------|---------|-----|
| `src/components/ui.tsx` | Unused `ScrollView` | Remove import |
| `app/(tabs)/_layout.tsx` | Duplicate import from `expo-router`; unused `Text` | Merge imports, remove `Text` |
| `app/(tabs)/index.tsx` | Unused `formatDate`, `InfoBanner`, `SectionHeader`, `ActivityIndicator`; duplicate import from `i18n` | Remove unused, merge imports |
| `app/(tabs)/learn.tsx` | Unused `useQuery`, `Input` | Remove imports |
| `app/(tabs)/log.tsx` | Unused `SEVERITY_LABELS`, `setLogDate`, `SectionHeader`, `ActivityIndicator` | Remove unused |
| `app/(tabs)/patterns.tsx` | Unused `Platform` | Remove import |
| `app/(tabs)/summary.tsx` | Unused `ActivityIndicator`, other | Remove imports |

## 5. Release Prep

| Item | Status | Notes |
|------|--------|-------|
| EAS config | Present | eas.json has dev/preview/production profiles; ASC App ID 6776464254, EAS project 3522d57f |
| Production EAS build | Not created | No production build submitted yet |
| App config | Present | app.json: bundle `app.clearday.mobile`, scheme `clearday`, typed routes enabled |
| Play Store listing draft | Not started | Needs description, screenshots plan, content rating |
| App Store listing draft | Not started | Needs description, screenshots plan, age rating |
| Privacy/health-data disclosures | Not started | Required for both stores |

## 6. Compliance Checklist

> **Not legal advice.** Items flagged here need review by a qualified professional.

| Obligation | Status | Notes |
|------------|--------|-------|
| GDPR — Consent mechanism | **Present** | Registration has explicit consent toggle with health-data explanation (`register.tsx:117-136`). Consent is required before account creation. |
| GDPR — Data minimization | Needs review | Collects: displayName (optional), email, password, symptoms, cycles, bleeding logs, AI conversations. Appears proportionate to purpose. |
| GDPR — Storage/retention policy | Not verified | Define retention periods for symptom logs. Backend (Base44) retention unknown. |
| GDPR — Right to deletion | **Present** | Account deletion via `POST /api/v1/profile/delete-request` with scheduled deletion date and cancel option (`settings.tsx:104-121`). |
| GDPR — Right to access/export | **Gap** | Clinician summary export exists (Share Sheet .txt) but full data export/portability not visible in Settings. Need dedicated data export feature. |
| GDPR — DPA with Base44 | Not verified | Data processor agreement needed if Base44 processes EU health data. |
| Quebec Law 25 — Privacy policy | **Gap** | Privacy section exists in Settings with descriptive text, but no link to full privacy policy. Must be in French. |
| Quebec Law 25 — Privacy impact assessment | Not verified | Required for health data processing. |
| Quebec Law 25 — Data incident response | Not verified | Breach notification procedures. |
| Quebec Law 25 — Consent for health data | **Present** | Explicit consent at registration, separate from account creation. |
| App Store — Health data disclosure | Not started | Apple requires health data privacy nutrition labels. |
| Play Store — Health data disclosure | Not started | Google Data Safety section required. |

## 7. Clinical Safety

| Item | Status | Notes |
|------|--------|-------|
| AI safety flags | **Verified** | `containsRefusal`, `containsRedFlagEscalation`, `isEmergencyEscalation` on every Message type (`ask.tsx:42-45`). Propagated through SSE `done` event (`ask.tsx:113-117`). |
| Safety boundary (Ask) | **Verified** | `InfoBanner` with `t("nav.boundaryNote")` displayed above chat (`ask.tsx:326-332`). |
| Red flag escalation UI | **Verified** | Amber warning banner on flagged messages: "Flagged — discuss with your clinician" (`ask.tsx:427-434`). **Note:** this string is hardcoded, needs i18n. |
| Safety footer (Dashboard) | **Verified** | `t("dashboard.safetyFooter")` at bottom of dashboard (`index.tsx:147-150`). |
| Safety banner (Articles) | **Verified** | `InfoBanner` with `t("article.safety")` on every article detail page (`[slug].tsx:128`). |
| Safety note (Symptom log) | **Verified** | `t("symptom.safetyNote")` at bottom of symptom log form (`log.tsx:157-159`). |
| Emergency text (Auth) | **Verified** | `t("auth.emergency")` on login and register screens (`login.tsx:112`, `register.tsx:151`). |
| Flagged events (Summary) | **Verified** | `containsFlaggedEvents` on clinician summaries with amber warning banner (`summary.tsx:211-218`). |
| Descriptive-only patterns | **Verified** | Patterns tab shows frequency, impact bars, cycle lengths — all descriptive. Includes `t("insights.aboutBody")` disclaimer and per-section notes (`patterns.tsx`). |
| Bleeding warnings | **Verified** | Post-coital and postmenopausal bleeding flags with amber clinical notes (`log.tsx:238-243`). |
| Consent at registration | **Verified** | Explicit health-data consent block with educational disclaimer and required toggle (`register.tsx:117-136`). |

## 8. Mobile App Structure (from uploaded files)

**7 tabs** (not 6 as in spec — Patterns tab was added):
- **Auth**: `/(auth)/login`, `/(auth)/register`
- **Tabs**: Dashboard `/`, Log `/log`, Learn `/learn`, Patterns `/patterns`, Ask `/ask`, Summary `/summary`, Settings `/settings`
- **Detail**: `/article/[slug]`

Key source files: `src/components/ui.tsx`, `src/hooks/useAuth.ts`, `src/hooks/useLang.ts`, `src/lib/api.ts`, `src/lib/i18n.ts`, `src/lib/queryClient.ts`, `src/lib/utils.ts`

API endpoint: `https://api.base44.com/api/apps/69e4d5f11e2c1bdb65d7ccde/functions/cleardayCore2`

### API Endpoints (confirmed from source)

| Endpoint | Method | Screen |
|----------|--------|--------|
| `/api/v1/ai/conversations` | GET, POST | Ask |
| `/api/v1/ai/conversations/:id/messages` | GET | Ask |
| `/api/v1/ai/conversations/:id/stream` | POST (SSE) | Ask |
| `/api/v1/logs/symptoms` | POST | Log |
| `/api/v1/logs/cycles` | POST | Log |
| `/api/v1/logs/bleeding` | POST | Log |
| `/api/v1/education/articles` | GET (via qk) | Learn |
| `/api/v1/summary` | POST, GET (via qk) | Summary |
| `/api/v1/dashboard` | GET (via qk) | Dashboard, Patterns |
| `/api/v1/profile` | GET, PATCH | Settings |
| `/api/v1/profile/delete-request` | POST, DELETE | Settings |

Dev server note: `libgtk-3.so.0` error on headless Linux is cosmetic (React Native DevTools GUI); does not affect app.

## Next Actions

1. **Fix 7 hardcoded strings** — translate and add to `src/lib/i18n.ts` EN/FR
2. **Fix 18 ESLint warnings** in clearday-mobile (all unused imports — mechanical cleanup)
3. **Full i18n audit** of `src/lib/i18n.ts` (56 KB) — verify all `t()` keys have both EN and FR values
4. **Add data export feature** — Settings needs full data export for GDPR portability
5. **Add privacy policy link** — Settings privacy section needs link to full policy (in French for Quebec Law 25)
6. **Run test suites** to verify green baseline
7. **Draft store listings** for Play Store and App Store
8. **Prepare privacy/health-data disclosures** for both stores
9. **Engage qualified professional** for GDPR and Quebec Law 25 compliance review
