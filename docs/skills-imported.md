# Imported skills

Nine third-party skills were copied into `.claude/skills/` on 27 September 2026. Each folder keeps
its authors' text, carries a one-line `SOURCE` file and the upstream licence as `LICENSE`, and opens
with a house-rules note that puts this repository's CLAUDE.md and writing rules ahead of the skill.
The only other edit is in `seo-content`, where three paths now point at the two files copied in
beside it.

The upstream repositories are https://github.com/obra/superpowers, https://github.com/Leonxlnx/taste-skill, https://github.com/IrtezaAsadRizvi/article-writing-skills, https://github.com/AgriciDaniel/claude-seo and https://github.com/irinabuht12-oss/marketing-skills, and each address is the git remote of the local clone that its copy was taken from, checked 27 September 2026.

| Skill and what it is for in this repository | Upstream repository, path, commit and licence |
|---|---|
| `brainstorming` explores intent and options before a spine or a design is written, and it closes open branches by asking one question at a time. | It comes from `skills/brainstorming` in obra/superpowers at commit `8ca22db` and carries the MIT licence. |
| `verification-before-completion` requires fresh proof, meaning the output of the verify command, before any claim that a pack or a fix is done. | It comes from `skills/verification-before-completion` in obra/superpowers at commit `8ca22db` and carries the MIT licence. |
| `taste-skill`, which loads under its frontmatter name `design-taste-frontend`, sets the visual direction for demo pages, companion pages and slide visuals so that they avoid the generic look. | It comes from `skills/taste-skill` in Leonxlnx/taste-skill at commit `ce26fc2` and carries the MIT licence. |
| `minimalist-skill`, which loads under the name `minimalist-ui`, is the restrained editorial variant for study notes pages, cheat sheets and print-first material. | It comes from `skills/minimalist-skill` in Leonxlnx/taste-skill at commit `ce26fc2` and carries the MIT licence. |
| `redesign-skill`, which loads under the name `redesign-existing-projects`, audits an existing page or deck and upgrades it where it stands. | It comes from `skills/redesign-skill` in Leonxlnx/taste-skill at commit `ce26fc2` and carries the MIT licence. |
| `karpathy-article-writing` is the persona-driven analytical lens for study notes, pre-reads and explainers, and it builds intuition from first principles and a worked example. | It comes from the `andrej-karpathy` folder in IrtezaAsadRizvi/article-writing-skills at commit `a96fe24`, renamed here to match its frontmatter name, and it carries the MIT licence. |
| `seo-content-brief` writes briefs for public-facing pages such as the wiki and public posts, and it is never used for classroom material. | It comes from `skills/seo-content-brief` in AgriciDaniel/claude-seo at commit `e77e783` and carries the MIT licence. |
| `seo-content` gives every written artifact its last-mile cleanup of AI-typical phrasing and invisible Unicode characters, and its E-E-A-T scoring applies to public pages only. | It comes from `skills/seo-content` in AgriciDaniel/claude-seo at commit `e77e783` and carries the MIT licence, and `scripts/content_humanize.py` and `skills/seo/references/eeat-framework.md` were copied in from the same commit. |
| `content-repurposer` turns a finished day pack or a capstone story into announcement posts and newsletters for public channels. | It comes from `skills/content-repurposer` in irinabuht12-oss/marketing-skills at commit `1bb135e`, which has no licence file, so this copy relies on the README's statement that the skills are MIT licensed. |

## gsd-core

`gsd-core` from https://github.com/open-gsd/gsd-core (commit `19a7b1f`, MIT, git remote checked 27 September 2026) is recorded here
and left out of `.claude/skills/`, because its skills `@`-include files from `~/.claude/gsd-core/`
and rely on its npm runtime. It installs from the npm package `@opengsd/gsd-core` with
`npx @opengsd/gsd-core@latest`, which asks for the runtime and the scope. The project's runtime guide
gives `npx @opengsd/gsd-core@latest --claude --global` for a Claude Code install across every project,
and `--local` in place of `--global` scopes it to one project. Its `package.json` asks for Node.js 24
or later and npm 10 or later. The npm registry listed 1.15.0 as the latest published version on
27 September 2026, which matches the `package.json` at the cloned commit.

## Unresolved dependencies

A few references point outside the copied folders and stay unresolved. The architectural path in
`brainstorming` ends by invoking a `writing-plans` skill that was not imported, the skill also names
an optional `elements-of-style` writing skill, and its visual companion needs Node.js to run
`scripts/server.cjs`. In `seo-content`, the Google update check runs `seo_updates.py` through the
claude-seo launcher and needs the upstream `data/google-updates.json`, the GEO section points at
`skills/seo-geo/references/google-ai-optimization-guide.md` and the `seo-geo` skill, and the last
section calls the plugin's `/seo flow` commands, so those parts work only alongside the full
claude-seo plugin. The DataForSEO and Ahrefs integrations in the two seo skills and the Ryze
connector suggested at the end of `content-repurposer` are optional and need connectors this
repository does not configure. The block library that section 12 of `taste-skill` describes has no
files upstream at `ce26fc2`, so there was nothing to copy.
