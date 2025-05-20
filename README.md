# An archive of the Hot in Here Radio show that aired on WCBN-FM 88.3 Ann Arbor

- Audio filies are hosted on Mi-Video: https://seas.mivideo.it.umich.edu/channel/Podcast%3A+It%27s+Hot+in+Here/321422382
- Blog posts embed a player from Mi-Video (Kaltura) and use an `articleID` in the front matter of each post to source the appropriate audio file.
- The archive was converted from a backup of the old Wordpress site and runs on [11ty](https://www.11ty.dev/), [using eleventy-base-blog](https://github.com/11ty/eleventy-base-blog) v9.
- Older episodes are available at https://archive.org/details/SNREHotInHere and appear as embeds on their individual posts. (These still need to be fixed!)
- Even older episodes (2008-2010) are archived here: https://archive.org/details/hotinhere

---

To run locally: 
1. Clone this repository
2. `npm install`
3. `npx @11ty/eleventy --serve`

Deploying:
- [pagefind](https://pagefind.app/) needs to run in order to do the search indexing:
`npx @11ty/eleventy && npx pagefind --site _site`
- otherwise, follow the official 11ty instructions https://www.11ty.dev/docs/deployment/
