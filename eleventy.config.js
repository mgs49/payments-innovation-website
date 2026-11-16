import fs from "node:fs";
import markdownIt from "markdown-it";
import { EleventyHtmlBasePlugin } from "@11ty/eleventy";

// Served from https://payments-innovation.com/ once the file src/CNAME exists.
// Until then GitHub Pages serves it from https://mgs49.github.io/payments-innovation-website/.
const hasCustomDomain = fs.existsSync("src/CNAME");
const pathPrefix = process.env.PATH_PREFIX || (hasCustomDomain ? "/" : "/payments-innovation-website/");
const site = JSON.parse(fs.readFileSync("src/_data/site.json", "utf8"));

export default function (eleventyConfig) {
  eleventyConfig.addPlugin(EleventyHtmlBasePlugin);
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy("src/CNAME");
  eleventyConfig.addPassthroughCopy({ "src/robots.txt": "robots.txt" });
  eleventyConfig.addPassthroughCopy({ "src/.nojekyll": ".nojekyll" });

  const md = markdownIt({ html: true, linkify: false, typographer: false, breaks: false });
  // A heading that is just a year ("## 2026") gets an id (#y2026) so the year links
  // at the top of the lectures and publications pages can jump to it.
  const headingOpen = md.renderer.rules.heading_open || ((t, i, o, e, self) => self.renderToken(t, i, o));
  md.renderer.rules.heading_open = (tokens, idx, options, env, self) => {
    const text = ((tokens[idx + 1] && tokens[idx + 1].content) || "").trim();
    if (/^(19|20)\d\d$/.test(text)) {
      tokens[idx].attrSet("id", "y" + text);
      tokens[idx].attrSet("class", "year");
    }
    return headingOpen(tokens, idx, options, env, self);
  };
  eleventyConfig.setLibrary("md", md);

  // Pages always link to the personal site by its real address, https://www.salmony.co.uk/.
  // While that site is still a preview, the links are pointed at the preview instead
  // (set "personalUrl" in src/_data/site.json to the real address at go-live).
  eleventyConfig.addTransform("personal-site-links", function (content) {
    if ((this.page.outputPath || "").endsWith(".html") && site.personalUrl !== "https://www.salmony.co.uk") {
      return content.replaceAll("https://www.salmony.co.uk/", site.personalUrl + "/");
    }
    return content;
  });

  eleventyConfig.addFilter("startsWith", (value, prefix) => String(value || "").startsWith(prefix));

  return {
    pathPrefix,
    dir: { input: "src", output: "_site", includes: "_includes", data: "_data" },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    templateFormats: ["md", "njk", "html"],
  };
}
