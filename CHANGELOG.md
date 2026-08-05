# Changelog

## v1.0.0

First public release.

- Eight behaviours: `onboarding`, `morning-brief`, `meeting-prep`, `transcript-to-actions`, `daily-transcript-sweep`, `end-of-day-close`, `weekly-review`, `connection-check`.
- Six workspace files and four output folders, created automatically by `onboarding` when they do not exist.
- Capability registry (`connections.md`) tracking Calendar, Email, Documents, Transcripts, Chat, Tasks, and CRM by job rather than by vendor.
- Three-gate nudge policy, one capability line per brief maximum, permanent silencing on request.
- Ten approval gates. The system drafts and never sends.
- Single-source build producing the Claude plugin, the Claude drop-in folder, per-behaviour upload ZIPs, and the ChatGPT project pack.
