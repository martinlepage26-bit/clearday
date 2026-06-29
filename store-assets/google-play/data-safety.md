# Clearday — Google Play Data Safety Questionnaire

## Data Collection & Sharing

### Data types collected

| Data type | Collected | Shared | Purpose |
|-----------|-----------|--------|---------|
| Email address | Yes | No | Account creation, authentication |
| Name (display name) | Yes (optional) | No | Personalization |
| Health info (symptoms, severity) | Yes | No | Symptom tracking, pattern analysis |
| Health info (menstrual cycles) | Yes | No | Cycle tracking |
| Health info (bleeding logs) | Yes | No | Bleeding pattern tracking |
| App interactions (AI conversations) | Yes | No | Educational AI navigator |
| App interactions (article views) | Yes | No | Education library usage |

### Data NOT collected

- Location
- Financial information
- Photos or videos
- Audio
- Files and documents
- Contacts
- Calendar
- Device identifiers (beyond what Expo provides)
- Browsing history

## Security

| Question | Answer |
|----------|--------|
| Is data encrypted in transit? | Yes (HTTPS/TLS) |
| Is data encrypted at rest? | Yes (auth token in expo-secure-store; server-side encryption per Base44) |
| Can users request data deletion? | Yes (Settings > Account > Delete Account) |
| Deletion mechanism | POST /api/v1/profile/delete-request — scheduled deletion with cancellation option |

## Data handling

| Question | Answer |
|----------|--------|
| Is data processing required for the app to function? | Yes — symptom and cycle data is core functionality |
| Is health data shared with third parties? | No |
| Is health data used for advertising? | No |
| Is health data used for analytics? | Only aggregate pattern display to the user themselves |
| Can users opt out of data collection? | Users can choose not to log; account deletion removes all data |

## Privacy policy URL
https://martinlepage26-bit.github.io/clearday/privacy-policy.html

## Notes for submission

- Health data is classified as "sensitive" by Google Play. The Data Safety section must explicitly declare health data collection.
- The app does NOT use HealthKit, Google Fit, or any device health APIs.
- All health data is self-reported by the user through manual entry.
- AI conversations are processed server-side via the Base44 backend. The AI is educational only and includes safety flags (containsRefusal, containsRedFlagEscalation, isEmergencyEscalation).
