---
name: Modern Stoic AI Security
colors:
  surface: '#061422'
  surface-dim: '#061422'
  surface-bright: '#2d3a49'
  surface-container-lowest: '#020f1c'
  surface-container-low: '#0f1d2a'
  surface-container: '#13212e'
  surface-container-high: '#1e2b39'
  surface-container-highest: '#293644'
  on-surface: '#d6e4f7'
  on-surface-variant: '#c6c6ca'
  inverse-surface: '#d6e4f7'
  inverse-on-surface: '#243240'
  outline: '#8f9094'
  outline-variant: '#45474a'
  surface-tint: '#c6c6ca'
  primary: '#c6c6ca'
  on-primary: '#2f3034'
  primary-container: '#121417'
  on-primary-container: '#7d7e82'
  inverse-primary: '#5d5e62'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c1c8ca'
  on-tertiary: '#2b3234'
  tertiary-container: '#0e1517'
  on-tertiary-container: '#788082'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e6'
  primary-fixed-dim: '#c6c6ca'
  on-primary-fixed: '#1a1c1f'
  on-primary-fixed-variant: '#45474a'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#dde4e6'
  tertiary-fixed-dim: '#c1c8ca'
  on-tertiary-fixed: '#161d1f'
  on-tertiary-fixed-variant: '#41484a'
  background: '#061422'
  on-background: '#d6e4f7'
  surface-variant: '#293644'
typography:
  display-lg:
    fontFamily: Source Serif 4
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Source Serif 4
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Source Serif 4
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Source Serif 4
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  code-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 32px
  gutter: 24px
  section-gap: 64px
---

## Brand & Style

The design system is built on the principles of Stoic philosophy—logic, focus, and clarity—tailored for the high-stakes environment of cloud security. The target audience is senior DevOps and Security Engineers who require high-density information processed through a lens of calm authority.

The design style is **Minimalist-Technical**. It rejects the frantic energy of typical security dashboards in favor of a grounded, intentional workspace. By utilizing a "Modern Stoic" aesthetic, the system emphasizes substance over flourish. Every pixel must serve a purpose; if an element does not contribute to a decision or an understanding, it is removed. The emotional response is one of controlled confidence and unwavering focus.

## Colors

The palette is strictly curated to minimize visual noise and highlight "virtue" (actionable insights).

- **Primary (Ground):** A deep charcoal (#121417) serves as the foundation, providing a non-reflective, focus-oriented background.
- **Secondary (Virtue):** A muted gold (#D4AF37) is used sparingly as the accent color. It represents "The Light of Reason" and is reserved for primary actions, critical insights, and successful resolutions.
- **Surface & Muted:** Slate grays and stone tones are used for container hierarchy, ensuring the UI feels architectural and solid.
- **Semantic Status:** 
    - *Logic (Info):* Muted Blue-Grey.
    - *Prudence (Warning):* Burnt Ochre.
    - *Courage (Danger):* Deep Madder Red.
    - *Temperance (Success):* Sage Green.

## Typography

Typography establishes the hierarchy between wisdom (strategy) and logic (execution).

- **Headings (Source Serif 4):** Represents the "Stoic Sage." It provides an authoritative, editorial feel to high-level security summaries and system states.
- **Body (Geist):** A highly legible, neutral sans-serif for descriptions and narrative logs. It remains unobtrusive to allow the content to lead.
- **Data & Metadata (JetBrains Mono):** All technical data, AWS resource IDs, and timestamps use monospaced type to signify precision and algorithmic logic. 

Letter spacing is increased for labels to enhance legibility in dark environments, while headings use tight tracking to appear more "set in stone."

## Layout & Spacing

The layout utilizes a **Fixed Grid** on desktop (12 columns) and a fluid layout on mobile. The philosophy is "The Breath of Reason"—generous whitespace is used to isolate components and prevent cognitive overload during security incidents.

- **Margins:** 32px standard margin for all screen edges.
- **Gutters:** 24px fixed gutters to maintain a rigorous structural rhythm.
- **Alignment:** Content is strictly aligned to the baseline grid. 
- **Mobile Reflow:** On mobile, the 12-column grid collapses to 4 columns. Complex data tables should transform into vertically stacked "Log Cards" to maintain readability.

## Elevation & Depth

This design system avoids traditional drop shadows, which are viewed as unnecessary "noise." Instead, it uses **Tonal Layers** and **Low-Contrast Outlines**.

- **Level 0 (Base):** Primary background (#121417).
- **Level 1 (Surfaces):** Containers use a slightly lighter slate (#1C1F23) with a 1px solid border (#2D3436).
- **Active State:** Elements in focus or active use a subtle inner glow or the "Virtue Gold" border.
- **Depth:** Depth is conveyed through subtle differences in value (lightness) rather than physical distance. A higher-priority modal will have a slightly lighter background than the page beneath it, creating a "stacked stone" effect.

## Shapes

The shape language is **Soft (0.25rem)**. The system avoids sharp, aggressive corners to prevent a "hostile" UI feel, but also avoids overly rounded or pill shapes that feel too casual. The 4px (0.25rem) radius provides just enough softening to feel modern and professional while maintaining a "solid block" architecture. 

Large containers (cards) follow the `rounded-lg` (0.5rem) token to emphasize their role as structural anchors.

## Components

Components are designed to feel like heavy, tactile objects that have been digitally refined.

- **Buttons:** Rectangular with a 4px radius. The primary button is solid "Virtue Gold" with black text. Secondary buttons are ghost buttons with a stone-gray border.
- **Structured Roadmaps:** Vertical timelines using thick 2px lines and monospaced labels. Completed steps are marked with the gold accent; pending steps are muted stone.
- **Status Trackers:** Minimalist bars with no gradients. Use high-contrast fills for active metrics and low-contrast fills for background capacity.
- **Session Logs:** Use a dark-mode terminal aesthetic. High-contrast white for commands, muted grey for timestamps, and the gold accent for AI-generated insights or "Reasoning" steps.
- **Input Fields:** Flat backgrounds with a bottom-only border that turns gold on focus. This mimics traditional formal stationery while remaining functional for high-speed data entry.
- **Cards:** No shadows. Use a 1px border and a subtle header background color to separate "Wisdom" (header) from "Logic" (content).