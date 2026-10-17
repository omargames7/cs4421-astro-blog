import { describe, expect, it } from 'vitest';
import { PROJECTS } from './consts';

describe('project content', () => {
	it('uses a unique, non-empty slug for each project', () => {
		const slugs = PROJECTS.map((project) => project.slug);

		expect(slugs.every((slug) => slug.trim().length > 0)).toBe(true);
		expect(new Set(slugs).size).toBe(slugs.length);
	});

	it('provides editable content sections for every project', () => {
		for (const project of PROJECTS) {
			expect(project.name.trim().length).toBeGreaterThan(0);
			expect(project.description.trim().length).toBeGreaterThan(0);
			if (!project.websiteUrl) {
				expect(project.about.length).toBeGreaterThan(0);
				expect(project.development).toBeDefined();
				expect(project.challenges).toBeDefined();
			}
		}
	});

	it('links the school project directly to its original website', () => {
		const schoolProject = PROJECTS.find((project) => project.websiteUrl);

		expect(schoolProject?.websiteUrl).toBe('/school-project/');
	});
});
