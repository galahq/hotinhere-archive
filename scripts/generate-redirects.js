import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

// Directory containing blog posts
const BLOG_DIR = path.join(process.cwd(), 'content/blog');

// Function to convert a slug to the old podcast format
function getOldSlug(slug) {
    // Remove the YYYY-MM-DD- prefix to get the clean slug
    return slug.replace(/^\d{4}-\d{2}-\d{2}-/, '');
}

// Function to generate redirects
async function generateRedirects() {
    const redirects = [];
    
    // Read all blog post directories
    const blogDirs = fs.readdirSync(BLOG_DIR);
    
    for (const dir of blogDirs) {
        const postPath = path.join(BLOG_DIR, dir, 'index.md');
        
        // Skip if not a blog post directory
        if (!fs.existsSync(postPath)) continue;
        
        // Read the markdown file
        const fileContent = fs.readFileSync(postPath, 'utf8');
        const { data } = matter(fileContent);
        
        // Skip if no date
        if (!data.date) continue;
        
        // Format the date as YYYY-MM-DD
        const date = new Date(data.date).toISOString().split('T')[0];
        
        // Get the old and new slugs
        const newSlug = dir;
        const oldSlug = getOldSlug(dir);
        
        // Add the redirect rule
        redirects.push(`/podcast/${oldSlug}/ /blog/${newSlug}/ 301`);
    }
    
    // Sort redirects alphabetically
    redirects.sort();
    
    // Add header comment
    const content = `# Redirect old podcast URLs to new blog URLs\n${redirects.join('\n')}\n`;
    
    // Write to _redirects file in the site root
    fs.writeFileSync(path.join(process.cwd(), '_redirects'), content);
    
    console.log(`Generated ${redirects.length} redirect rules`);
}

generateRedirects().catch(console.error); 