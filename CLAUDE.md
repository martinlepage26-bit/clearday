@AGENTS.md

# Clearday — Agent Context

## Stack
- Expo 56 / React Native 0.85 / TypeScript
- TanStack Query v5, expo-router, expo-secure-store
- NativeWind 4 + Tailwind 3.4
- SSE streaming for AI responses
- i18n: EN/FR via `src/lib/i18n.ts` (t() accessor, ~80% coverage)

## Key identifiers
- Bundle ID: `app.clearday.mobile`
- EAS project: `3522d57f-6d80-4856-8f03-6e4c88bf1404`
- API: `https://api.base44.com/api/apps/69e4d5f11e2c1bdb65d7ccde/functions/cleardayCore2`
- Brand primary: `#2D6A4F`, background: `#F7F8F5`

## Repo layout (this repo: clearday)
- `store-assets/google-play/` — Play Store listing, data safety, feature graphic, screenshots plan
- `store-assets/app-store/` — App Store Connect metadata
- `store-assets/screenshots/` — 13 generated screenshots (1242×2688px)
- `mobile-patches/` — patched source files for clearday-mobile with fixes
- `privacy-policy.html` — root copy served via GitHub Pages
- `LAUNCH-GUIDE.md` — step-by-step Play Store submission guide
- `PROGRESS.md` — full progress tracker

## Mobile patches (apply to clearday-mobile)
- `mobile-patches/src/lib/utils.ts` — fix: symptomLabel() now uses i18n t() instead of hardcoded English
- `mobile-patches/src/components/ui.tsx` — fix: removed unused ScrollView import
- `mobile-patches/PATCH_NOTES.md` — missing i18n keys to add (auth.requiredFields, auth.loginFailed, auth.registerFailed, nav.flaggedEscalation, settings.account)

## Clinical safety — NEVER remove or weaken
- AI flags: `containsRefusal`, `containsRedFlagEscalation`, `isEmergencyEscalation` on every message
- `SafetyBoundary` and `InfoBanner` components must remain on Ask, Patterns, Articles screens
- Safety footer: "educational tool; does not diagnose, prescribe, or replace medical care"
- All patterns/trends must be descriptive only, never diagnostic

## GitHub Pages
- Privacy policy live at: `https://martinlepage26-bit.github.io/clearday/privacy-policy.html`
- Workflow: `.github/workflows/pages.yml` (enabled, runs on push to main)

## Loop routine context
Last completed (2026-06-29):
- GitHub Pages enabled and live ✅
- 13 screenshots generated ✅
- App Store metadata saved ✅
- Play Store feature graphic generated (1024×500px) ✅
- Mobile code patches committed ✅
- PR #3 open on claude/serene-albattani-aab3wt

Remaining (user credential-gated):
1. EAS production build: `eas build --profile production --platform android`
2. Google Play Console listing (use store-assets/google-play/)
3. Upload .aab + submit for review
