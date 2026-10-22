# Omar's Projects

An Astro site showcasing Omar's games and other projects.

## Editing project content

Add or update project details in [`src/consts.ts`](src/consts.ts). Each entry in
`PROJECTS` controls one project page:

- `description` is the short summary shown on the home page and project page.
- `about` is the introductory text on the project page.
- `development` and `challenges` are optional paragraph arrays for the
  corresponding sections. Add text to show those sections.

The project page layout is [`src/pages/projects/[slug].astro`](src/pages/projects/%5Bslug%5D.astro).
It generates a route per game using its `slug` (for example,
`/projects/petrichor/`). Projects with a `websiteUrl` link directly to their own
site instead; the school project website is served from `public/school-project/`.

## Commands

| Command | Action |
| :--- | :--- |
| `npm install` | Installs dependencies |
| `npm run dev` | Starts the local development server at `localhost:4321` |
| `npm run check` | Checks Astro and TypeScript |
| `npm run lint` | Runs ESLint |
| `npm run build` | Builds the production site |

## Deployments

The container workflow builds and pushes the current server-rendered Astro app
image to ECR. The separate `StaticSiteStack` workflow publishes the standalone
full Astro site, including `public/school-project/`, to S3 and CloudFront; it
does not replace the container workflow. Both workflows run on pushes to
`main`.

Configure the GitHub repository secrets `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY` before enabling either AWS deployment workflow. The
static deployment prints its CloudFront HTTPS URL as the `SiteUrl` stack
output.
