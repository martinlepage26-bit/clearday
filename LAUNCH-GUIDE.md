# Clearday — Google Play Launch Guide

Step-by-step instructions for submitting Clearday to Google Play Store.

## Prerequisites

- [ ] Google Play Developer account ($25 one-time fee) — https://play.google.com/console/signup
- [ ] EAS CLI installed: `npm install -g eas-cli`
- [ ] Logged into EAS: `eas login`
- [ ] `clearday-mobile` repo cloned locally with dependencies installed

## Step 1: Host the Privacy Policy

Google Play requires a publicly accessible privacy policy URL.

**Option A — GitHub Pages (free, recommended)**

1. The privacy policy is already at `store-assets/privacy-policy.html` in this repo.
2. Enable GitHub Pages on this repo: Settings → Pages → Source: Deploy from branch → `main` → `/` (root).
3. Rename or copy the file:
   ```bash
   cp store-assets/privacy-policy.html privacy-policy.html
   ```
4. Your URL will be: `https://martinlepage26-bit.github.io/clearday/privacy-policy.html`

**Option B — Custom domain**

If you have a domain (e.g., `clearday.app`), deploy the HTML there.

## Step 2: Build the Production APK/AAB

From the `clearday-mobile` directory:

```bash
# Build Android App Bundle (required for Play Store)
eas build --profile production --platform android
```

This will:
- Use the `production` profile from `eas.json`
- Generate an `.aab` file (Android App Bundle)
- Handle code signing via EAS

The build takes 10-20 minutes. EAS provides a download link when complete.

## Step 3: Create Google Play Console Listing

### 3.1 Create the App

1. Go to https://play.google.com/console
2. Click "Create app"
3. App name: `Clearday: Perimenopause`
4. Default language: English (United States)
5. App or game: App
6. Free or paid: Free
7. Accept declarations

### 3.2 Store Listing

Copy from `store-assets/google-play/listing.md`:

- **App name** (30 chars): `Clearday: Perimenopause`
- **Short description** (80 chars): `Track symptoms, understand patterns, and prepare for your doctor visits.`
- **Full description**: Copy the full description section from `listing.md`
- **Category**: Health & Fitness
- **Contact email**: martinlepage.ai@gmail.com

### 3.3 Screenshots

Follow the plan in `store-assets/google-play/screenshots-plan.md`:

1. Run the app on a device or emulator (Pixel 6 or similar, 1080x2400)
2. Capture 6 screenshots per the plan:
   - Screenshot 1: Dashboard (hero)
   - Screenshot 2: Symptom tracking (Log tab)
   - Screenshot 3: Patterns tab
   - Screenshot 4: AI navigator (Ask tab)
   - Screenshot 5: Clinician summary
   - Screenshot 6: Education library (Learn tab)
3. Add text overlays using a tool like Figma, Canva, or screenshots.pro
4. Export as PNG, 9:16 aspect ratio (1080x1920 or 1242x2208)

### 3.4 Feature Graphic (1024x500)

Create a simple graphic:
- Background: `#2D6A4F` gradient
- Center: App icon + "Clearday" wordmark
- Tagline: "Perimenopause support that prepares you for your doctor."

### 3.5 App Icon

- Must be 512x512 PNG (no alpha)
- Use the existing app icon from `clearday-mobile/assets/images/icon.png`

## Step 4: Data Safety Section

Fill in the Google Play Data Safety form using `store-assets/google-play/data-safety.md` as reference.

Key declarations:
- **Collects health data**: Yes (symptoms, cycles, bleeding — self-reported)
- **Shares data with third parties**: No
- **Data encrypted in transit**: Yes
- **Users can request deletion**: Yes
- **Privacy policy URL**: (from Step 1)

## Step 5: Content Rating

1. Go to App content → Content rating
2. Start the IARC questionnaire
3. Answer: health/medical information, no violence, no sexual content, no gambling, no user-generated content sharing
4. Expected rating: **Everyone** (PEGI 3 / ESRB Everyone)

## Step 6: Health App Declarations

Google Play has additional requirements for health apps:

1. Go to App content → Health apps
2. Declare:
   - App provides health-related information: Yes
   - App is NOT a medical device: Correct
   - App does NOT provide diagnosis or treatment: Correct
   - App provides educational information: Yes
3. Include the safety disclaimer from the app in the store listing

## Step 7: Target Audience

1. Go to App content → Target audience and content
2. Target age group: 18+ (perimenopause audience)
3. App is NOT designed for children: Correct

## Step 8: Upload the Build

1. Go to Release → Production
2. Click "Create new release"
3. Upload the `.aab` file from Step 2
4. Release name: `1.0.0`
5. Release notes:
   ```
   Initial release of Clearday — perimenopause symptom tracking, 
   pattern visualization, AI-powered education, and clinician summary 
   generation. Available in English and French.
   ```
6. Review and roll out

## Step 9: Submit for Review

1. Verify all sections show green checkmarks in the Dashboard
2. Click "Send for review"
3. Google review typically takes 1-7 days for new apps

## Pre-Submission Checklist

- [ ] Privacy policy hosted at public URL
- [ ] Production EAS build completed (.aab)
- [ ] Store listing filled in (name, descriptions, category)
- [ ] 6 screenshots uploaded (phone, 9:16)
- [ ] Feature graphic uploaded (1024x500)
- [ ] App icon uploaded (512x512)
- [ ] Data safety section completed
- [ ] Content rating questionnaire completed
- [ ] Health app declarations filled in
- [ ] Target audience set to 18+
- [ ] Contact email verified
- [ ] .aab uploaded to production track
- [ ] Release notes written

## French Store Listing (Optional but Recommended)

Google Play supports localized listings. Add a French translation:

1. Go to Store listing → Manage translations → Add language → French
2. Translate:
   - App name: `Clearday : Périménopause`
   - Short description: `Suivez vos symptômes, comprenez vos tendances et préparez vos rendez-vous médicaux.`
   - Full description: Translate the English description (the app's i18n already covers FR)
3. Upload French screenshots (optional — same screenshots work if text overlays are translated)

## Post-Launch

- Monitor the Play Console for crashes and ANRs
- Respond to user reviews
- Plan updates based on the items in `PROGRESS.md` (i18n fixes, ESLint cleanup, data export feature)

## Troubleshooting

**EAS build fails**: Check `eas.json` production profile, ensure `app.json` has correct `android.package` (`app.clearday.mobile`).

**Play Store rejects for health claims**: Ensure all copy says "educational tool" and "does not diagnose, prescribe, or replace medical care." Remove any language that implies diagnosis or treatment.

**Data safety rejection**: Double-check that health data is declared as collected. Google is strict about health data declarations.
