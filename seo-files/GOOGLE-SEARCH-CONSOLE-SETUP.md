# Google Search Console Setup Guide
## Sinofuse Distributor Website

### Overview
This guide walks you through setting up Google Search Console (GSC) for the Sinofuse distributor website to monitor SEO performance, track keyword rankings, and identify technical issues.

---

## Step 1: Property Setup

### 1.1 Create GSC Account
1. Go to [Google Search Console](https://search.google.com/search-console)
2. Sign in with your Google account
3. Click "Add Property"

### 1.2 Add Domain Property (Recommended)
```
Property Type: Domain
domain: sinofuse.elec-distributor.com
```
**Why Domain Property?**
- Covers all subdomains (www, blog, etc.)
- Covers all protocols (http/https)
- Covers all path prefixes

### 1.3 Verify Ownership

#### Method 1: DNS TXT Record (Recommended)
Add this TXT record to your DNS configuration:
```
Type: TXT
Name: @
Value: [Google will provide unique verification code]
TTL: 3600
```

**DNS Provider Instructions:**
- **Cloudflare**: DNS > Records > Add Record
- **GoDaddy**: My Products > DNS > Manage
- **Namecheap**: Domain List > Manage > Advanced DNS

#### Method 2: HTML File Upload
1. Download the verification HTML file from GSC
2. Upload to root directory: `c:\Users\ymlt\Desktop\sinofuse-distributor-site-master\`
3. Verify at: `https://sinofuse.elec-distributor.com/google[code].html`

#### Method 3: HTML Meta Tag
Add to `<head>` section of [index.html](file:///c:/Users/ymlt/Desktop/sinofuse-distributor-site-master/index.html):
```html
<meta name="google-site-verification" content="YOUR_VERIFICATION_CODE" />
```

---

## Step 2: Submit Sitemap

### 2.1 Sitemap URL
```
https://sinofuse.elec-distributor.com/sitemap.xml
```

### 2.2 Submit Process
1. In GSC, go to **Sitemaps** (left sidebar)
2. Enter sitemap URL
3. Click **Submit**

### 2.3 Sitemap Status Check
After submission, monitor:
- **Status**: Success / Error
- **Discovered URLs**: Should show ~200+ URLs
- **Indexed URLs**: Will populate over time

---

## Step 3: Configure International Targeting

### 3.1 Set Geographic Target (if applicable)
For the main site (global audience):
1. Go to **Legacy tools and reports** > **International Targeting**
2. Set **Country** to "Unlisted" (global audience)

### 3.2 Hreflang Monitoring
GSC will automatically detect hreflang tags. Monitor:
- **Coverage** > **International targeting** report
- Check for hreflang errors or warnings

---

## Step 4: Add Users and Permissions

### 4.1 User Roles
| Role | Permissions | Recommended For |
|------|-------------|-----------------|
| **Owner** | Full control | Primary admin |
| **Full User** | View all data, perform most actions | SEO team |
| **Restricted User** | View most data | Clients, stakeholders |

### 4.2 Add Users
1. Go to **Settings** > **Users and permissions**
2. Click **Add user**
3. Enter email address
4. Select permission level
5. Click **Add**

---

## Step 5: Essential Reports to Monitor

### 5.1 Performance Report
**Location**: Left sidebar > Performance

**Key Metrics:**
- **Total Clicks**: Organic traffic volume
- **Total Impressions**: Visibility in search results
- **Average CTR**: Click-through rate
- **Average Position**: Keyword rankings

**Filters to Set Up:**
1. **Queries**: Track "Sinofuse distributor", "EV fuses", "PV fuses"
2. **Pages**: Monitor localized pages performance
3. **Countries**: Track performance by target markets
4. **Devices**: Desktop vs Mobile vs Tablet

### 5.2 Coverage Report
**Location**: Left sidebar > Coverage

**Status Categories:**
- **Error**: Pages with crawl issues (fix immediately)
- **Valid with warnings**: Pages indexed but have issues
- **Valid**: Successfully indexed pages
- **Excluded**: Pages intentionally not indexed

**Common Issues to Watch:**
- 404 errors
- Soft 404s
- Server errors (5xx)
- Redirect errors

### 5.3 Core Web Vitals
**Location**: Experience > Core Web Vitals

**Metrics:**
- **LCP** (Largest Contentful Paint): < 2.5s
- **FID** (First Input Delay): < 100ms
- **CLS** (Cumulative Layout Shift): < 0.1

**Priority Pages:**
- Homepage
- Product category pages
- Localized landing pages

### 5.4 Mobile Usability
**Location**: Experience > Mobile Usability

**Check for:**
- Text too small to read
- Viewport not set
- Content wider than screen
- Clickable elements too close

### 5.5 Rich Results
**Location**: Enhancements > Rich Results

**Schema Types to Monitor:**
- Organization
- LocalBusiness
- FAQPage
- BreadcrumbList

---

## Step 6: Set Up Email Notifications

### 6.1 Enable Email Alerts
1. Go to **Settings** > **Email preferences**
2. Enable notifications for:
   - [x] Performance changes
   - [x] Coverage issues
   - [x] Mobile usability issues
   - [x] Core Web Vitals issues

---

## Step 7: Connect with Google Analytics

### 7.1 Link GSC with GA4
1. In GSC: **Settings** > **Associations** > **Google Analytics**
2. Select your GA4 property
3. Click **Associate**

### 7.2 Benefits
- See GSC data in GA4 interface
- Combine search data with user behavior data
- Track organic traffic conversions

---

## Step 8: Regular Monitoring Checklist

### Weekly Tasks
- [ ] Check Performance report for traffic changes
- [ ] Review Coverage report for new errors
- [ ] Monitor Core Web Vitals scores

### Monthly Tasks
- [ ] Analyze top performing queries
- [ ] Review indexed pages count
- [ ] Check for new backlink data
- [ ] Export performance data for reporting

### Quarterly Tasks
- [ ] Comprehensive SEO audit
- [ ] Review and update sitemap
- [ ] Analyze competitor performance
- [ ] Plan content strategy based on search data

---

## Step 9: Troubleshooting Common Issues

### Issue: Sitemap "Couldn't fetch"
**Solution:**
1. Verify sitemap URL is accessible
2. Check for XML syntax errors
3. Ensure proper HTTP headers (Content-Type: application/xml)
4. Resubmit after fixes

### Issue: Pages not indexed
**Possible Causes:**
- robots.txt blocking
- Noindex meta tag
- Canonical pointing elsewhere
- Low quality content

**Solution:**
1. Check Coverage report for specific reason
2. Use URL Inspection tool
3. Request indexing after fixes

### Issue: Hreflang errors
**Common Errors:**
- Missing return links
- Incorrect language codes
- Conflicting hreflang tags

**Solution:**
1. Validate with [hreflang checker](https://technicalseo.com/tools/hreflang/)
2. Fix errors in page templates
3. Re-crawl affected pages

---

## Step 10: Advanced Features

### 10.1 URL Inspection Tool
**Use for:**
- Checking index status of specific URLs
- Viewing rendered HTML
- Requesting indexing
- Checking mobile usability

### 10.2 Removals Tool
**Use for:**
- Temporarily hiding URLs from search
- Removing outdated content
- Handling sensitive information

### 10.3 Security Issues Report
**Monitors:**
- Malware detection
- Hacked content
- Social engineering

---

## Quick Reference

### Important URLs
| Resource | URL |
|----------|-----|
| GSC Dashboard | https://search.google.com/search-console |
| Sitemap | https://sinofuse.elec-distributor.com/sitemap.xml |
| Robots.txt | https://sinofuse.elec-distributor.com/robots.txt |

### Key Dates
- **Sitemap Last Updated**: 2026-04-08
- **Localized Pages Added**: 2026-04-08
- **Next Review**: 2026-05-08

---

## Support Resources

- [GSC Help Center](https://support.google.com/webmasters)
- [GSC Community Forum](https://support.google.com/webmasters/community)
- [Google Search Central Blog](https://developers.google.com/search/blog)

---

*Last Updated: 2026-04-08*
*Next Review: 2026-05-08*
