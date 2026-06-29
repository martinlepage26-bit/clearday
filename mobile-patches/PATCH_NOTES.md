# Mobile Code Patches

Apply these patched files to the `clearday-mobile` repo to fix the issues below.

## Fixes

### 1. `src/lib/utils.ts` — Hardcoded English symptom labels
**Bug:** `symptomLabel()` returned hardcoded English strings, ignoring the user's language setting. French users saw English symptom names everywhere this function was called (dashboard, patterns, summaries).

**Fix:** Replaced hardcoded label map with i18n key lookup using `t()` from `@/lib/i18n`. Now uses existing `symptom.*` translation keys (e.g. `symptom.hotFlashes` → "Bouffées de chaleur" in FR).

### 2. `src/components/ui.tsx` — Unused `ScrollView` import
**Issue:** `ScrollView` was imported from `react-native` but never used in the file.

**Fix:** Removed unused import.

### 3. `src/lib/i18n.ts` — Missing translation keys
**Issue:** The following keys are referenced in components but missing from the i18n dictionary:
- `auth.requiredFields`
- `auth.loginFailed`
- `auth.registerFailed`
- `nav.flaggedEscalation`
- `settings.account`

**Fix:** Add the block below to `i18n.ts` after the existing auth section:

```typescript
Object.assign(strings, {
  "auth.requiredFields":    { en: "Please fill in all required fields", fr: "Veuillez remplir tous les champs requis" },
  "auth.loginFailed":       { en: "Login failed. Please check your credentials.", fr: "Échec de connexion. Veuillez vérifier vos identifiants." },
  "auth.registerFailed":    { en: "Registration failed. Please try again.", fr: "Échec de l'inscription. Veuillez réessayer." },
  "nav.flaggedEscalation":  { en: "This response has been flagged. If you are in distress, please contact a clinician or call emergency services.", fr: "Cette réponse a été signalée. Si vous êtes en détresse, veuillez contacter un clinicien ou appeler les services d'urgence." },
  "settings.account":       { en: "Account",             fr: "Compte" },
});
```
