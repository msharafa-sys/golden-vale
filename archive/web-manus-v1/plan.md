# Golden Vale Website — Implementation and Design Plan

## Product scope and source boundaries

Build an Arabic-first, responsive, single-page company website for **جولدن فيل للدعاية والإعلان وتنظيم الفعاليات | Golden Vale** using the supplied 2026 company-profile PDF as the source of company wording, services and contact details. Deliver a working website preview; publication is not part of this request.

The page will include the company introduction and Riyadh base, vision and mission, served sectors, five service lines, differentiators, a concise project-delivery approach, and contact details. Arabic is the primary language and all principal content is presented right-to-left. Use the English brand name only as a secondary brand treatment.

**Evidence and publication guardrails:**
- Use only statements and contact details present in the supplied profile; do not add market claims, awards, certifications, named projects, client identities, testimonials, results or guarantees.
- Omit the numerical achievement panel (team experience, team size, client and project counts) because some figures appear difficult to reconcile with the stated 2026 company founding and the profile does not clarify their scope.
- Do not reproduce identifiable third-party customer branding from the profile photographs. Use original AI-created **illustrative concept imagery** for the hero and material-detail section; label those images as visual concepts and never as Golden Vale project evidence. Do not use search-result stock photographs as company work.
- Contact details are the profile's phone number (+966 50 622 1548), email (fd-0@hotmail.com) and Riyadh, Saudi Arabia location. WhatsApp is a direct link to that same supplied phone number; it does not imply a new contact channel or form backend.
- The site is static and requires no login, server, database, customer-data collection or form submission.

## Design direction

- **Design movement:** contemporary Saudi corporate editorial, drawing on the supplied profile's restrained luxury-print art direction and architectural event imagery.
- **Core principles:** clear RTL hierarchy; tangible, production-led storytelling; restrained premium details; useful contact paths without marketing overclaim.
- **Color philosophy:** deep espresso gives the fabrication and event work visual weight; warm ivory softens large text fields; aged brass/gold signals material finish and a memorable accent. Use gold sparingly for rules, numbering and key actions, not as a large flat background.
- **Layout paradigm:** an asymmetric, magazine-like long page with a spacious split hero, offset image-text pairs, staggered sector/service groupings and a deliberately paced dark-light sequence. Avoid a generic centered-card wall.
- **Signature elements:** an outlined portal/arch motif echoing an event entrance; fine brass hairline dividers and editorial index numbers; a restrained monogram-derived mark beside the bilingual wordmark.
- **Interaction philosophy:** clear anchor navigation, an accessible compact mobile menu, precise focus states and direct phone/email/WhatsApp links. No interaction suggests capabilities the static site does not have.
- **Animation:** brief opacity/translate reveals and menu transitions only; no parallax or motion essential to understanding; respect `prefers-reduced-motion` and provide visible focus feedback.
- **Typography system:** Noto Sans Arabic for Arabic body/headings with a system sans-serif fallback; DM Sans for interface labels and numerals; a restrained high-contrast serif for the spaced Latin `GOLDEN VALE` wordmark. Keep body copy comfortably readable and headings short.
- **Brand essence:** a Riyadh-based Saudi provider bringing advertising, event and exhibition concepts into physical form through coordinated design, production and installation. Personality: **precise, imaginative, dependable**.
- **Brand voice:** direct, confident and concrete; say what is designed, fabricated and installed, not generic superlatives. Example lines: “نصنع حضورًا يُرى ويُتذكّر.” and “من الفكرة إلى الموقع — نرافق تنفيذ فعاليتك.”
- **Wordmark & logo:** use a custom outlined portal/arch emblem with a compact `GV` monogram and a carefully spaced Latin wordmark beside the Arabic company name. Treat this as a website art-direction concept derived from the supplied profile, not as a claim that a new official corporate logo has been approved.
- **Signature brand color:** aged brass `#B79A63`, supported by espresso `#211914` and warm ivory `#F4F0E8`.

## Implementation approach and structure

Use the initialized Webdev **static** setup (Vite static development/build on port 3000) and create a semantic, content-bearing HTML page with plain JavaScript enhancement. This keeps the full Arabic page in the initial HTML for sharing and crawling, avoids adding runtime services, and retains a small, fast static deployment path. Build the preview with the project's prepared `pnpm dev:static`; the existing static build is `pnpm build:static` to `dist/public`.

```text
/home/ubuntu/goldval/
├── plan.md                         # approved implementation and design decisions
├── TODO.md                         # scoped deliverable outcomes
├── app.config.ts                   # quoted project-logo URL used by checkpoint sync
└── client/
    ├── index.html                  # full Arabic RTL document, metadata and semantic page content
    ├── src/site.css                # brand tokens, responsive layout, components and motion rules
    ├── src/site.js                 # mobile navigation and progressive enhancement
    └── public/
        ├── manus-routes.json       # route manifest for the one public page (/)
        ├── favicon.svg              # compact portal/monogram mark
        └── images/
            ├── hero-concept.png     # illustrative event-installation visual, not a project record
            └── material-concept.png # illustrative production-material detail, not a workshop photo
```

No server endpoints, application database, login, external form processor or new package is needed. All frontend image references remain relative and use assets hosted in the project. The initial document receives a descriptive Arabic title, a concise meta description and relevant meta keywords. Since no canonical production domain has been supplied and this task does not publish a site, do not guess a canonical URL, `og:url`, or public social-image URL.

## Content map

1. Sticky brand header and working anchor navigation.
2. Hero with the supplied positioning line “نصنع حضورًا يُرى ويُتذكّر” and a direct service/contact CTA.
3. About section: Saudi integrated advertising/events company founded in Riyadh in 2026.
4. Vision and mission, using the profile wording without adding claims.
5. Served sectors: entertainment destinations, government entities, trade exhibitions and real-estate developers.
6. Five service areas: exhibition stands; events and activations; signage and lighting; print and display; promotional gifts and uniforms.
7. Differentiators from the profile, expressed without unverifiable counts or new guarantees: in-house production workshop; specialist installation; internal design; coordinated services from one supplier; responsive execution; attention to the opening schedule.
8. A concise, source-grounded delivery sequence: understand the brief, prepare/design the concept, fabricate/finish, then install and hand over on site.
9. Contact block with functional telephone, email and WhatsApp links and the stated Riyadh location.

## Operational notes

The initialized project has `server:false`, `database:false`, runtime port `3000`, `publishing.auto_publish:false`, and TypeScript diagnostics registered. Keep publication off unless separately requested. Before checkpointing, add a quoted, durable HTTPS `logoUrl` in the project-root `app.config.ts` using a small publicly uploaded project mark, as required by the Webdev workflow.
