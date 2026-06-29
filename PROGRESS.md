# Clearday Progress Tracker

Last updated: 2026-06-29

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
| EN/FR coverage | ~80% | Per project spec; needs audit in clearday-mobile repo |
| Untranslated strings | Not audited | Requires access to clearday-mobile source |

## 4. Code Quality (Mobile App)

| Item | Status | Notes |
|------|--------|-------|
| Test suites (api, backend integration, i18n, utils) | Unknown | Requires clearday-mobile repo access |
| ESLint config | Present | eslint-config-expo/flat (from uploaded eas.json) |

## 5. Release Prep

| Item | Status | Notes |
|------|--------|-------|
| EAS config | Present | eas.json has dev/preview/production profiles; ASC App ID 6776464254 |
| Production EAS build | Not created | No production build submitted yet |
| Play Store listing draft | Not started | Needs description, screenshots plan, content rating |
| App Store listing draft | Not started | Needs description, screenshots plan, age rating |
| Privacy/health-data disclosures | Not started | Required for both stores |

## 6. Compliance Checklist

> **Not legal advice.** Items flagged here need review by a qualified professional.

| Obligation | Status | Notes |
|------------|--------|-------|
| GDPR — Consent mechanism | Not verified | Health data = special category; explicit consent required |
| GDPR — Data minimization | Not verified | Audit what data is collected vs. needed |
| GDPR — Storage/retention policy | Not verified | Define retention periods for symptom logs |
| GDPR — Right to deletion | Not verified | Must support account + data deletion |
| GDPR — Right to access/export | Not verified | Must provide data portability |
| GDPR — DPA with Base44 | Not verified | Data processor agreement needed if Base44 processes EU health data |
| Quebec Law 25 — Privacy policy | Not verified | Must be available in French |
| Quebec Law 25 — Privacy impact assessment | Not verified | Required for health data processing |
| Quebec Law 25 — Data incident response | Not verified | Breach notification procedures |
| Quebec Law 25 — Consent for health data | Not verified | Explicit consent, separate from ToS |
| App Store — Health data disclosure | Not started | Apple requires HealthKit/health data privacy nutrition labels |
| Play Store — Health data disclosure | Not started | Google Data Safety section required |

## 7. Clinical Safety

| Item | Status | Notes |
|------|--------|-------|
| AI safety flags | Assumed present | containsRefusal, containsRedFlagEscalation, isEmergencyEscalation |
| SafetyBoundary component | Assumed present | In clearday-mobile |
| Safety footer | Assumed present | "educational tool; does not diagnose, prescribe, or replace medical care" |
| Descriptive-only patterns | Assumed present | Trends/patterns never diagnostic |

## Next Actions

1. **Access clearday-mobile repo** to audit i18n coverage, run test suites, and verify clinical safety components
2. **Rebuild or update bundled assets** to use canonical brand color #2D6A4F throughout
3. **Draft store listings** for Play Store and App Store
4. **Prepare privacy/health-data disclosures** for both stores
5. **Engage qualified professional** for GDPR and Quebec Law 25 compliance review
