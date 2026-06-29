import { t, getLang } from "./i18n";

export function today(): string {
  return new Date().toISOString().split("T")[0];
}

export function formatDate(dateStr: string): string {
  const d = new Date(dateStr + (dateStr.includes("T") ? "" : "T00:00:00"));
  return d.toLocaleDateString(getLang() === "fr" ? "fr-CA" : "en-CA", {
    month: "short",
    day: "numeric",
    year: "numeric",
  });
}

const SYMPTOM_I18N_KEYS: Record<string, string> = {
  hotFlashes: "symptom.hotFlashes",
  nightSweats: "symptom.nightSweats",
  sleepDisruption: "symptom.sleepDisruption",
  moodChanges: "symptom.moodChanges",
  anxiety: "symptom.anxiety",
  brainFog: "symptom.brainFog",
  irritability: "symptom.irritability",
  fatigue: "symptom.fatigue",
  jointPain: "symptom.jointPain",
  headache: "symptom.headache",
  palpitations: "symptom.palpitations",
  vaginalDryness: "symptom.vaginalDryness",
  urinarySymptoms: "symptom.urinarySymptoms",
  functionalImpact: "symptom.functionalImpact",
};

export function symptomLabel(key: string): string {
  const i18nKey = SYMPTOM_I18N_KEYS[key];
  return i18nKey ? t(i18nKey) : key;
}

/** Returns a hex colour for severity 0–4 */
export function severityColor(v: number): string {
  return ["#6B7280", "#2D6A4F", "#F59E0B", "#EF4444", "#7C3AED"][
    Math.min(v, 4)
  ] ?? "#6B7280";
}

/** Clamp a number between min and max */
export function clamp(v: number, min: number, max: number) {
  return Math.max(min, Math.min(max, v));
}
