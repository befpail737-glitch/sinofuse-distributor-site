# Schema Markup Validation Checklist
## Sinofuse Distributor Website

### Overview
This checklist helps validate all Schema.org markup across the Sinofuse distributor website to ensure rich snippets appear in Google search results.

---

## Schema Types Implemented

### 1. Organization Schema
**Purpose**: Define the business entity

**Location**: All pages (in `<head>`)

**Required Properties**:
- [ ] `@context`: "https://schema.org"
- [ ] `@type`: "Organization"
- [ ] `name`: "LiTong Inc."
- [ ] `url`: "https://sinofuse.elec-distributor.com/"
- [ ] `logo`: Logo URL
- [ ] `contactPoint`: Contact information

**Validation Tool**: [Google Rich Results Test](https://search.google.com/test/rich-results)

**Test URL**: `https://sinofuse.elec-distributor.com/`

---

### 2. LocalBusiness Schema
**Purpose**: Define local business locations for each country

**Locations**: All 13 localized pages

**Required Properties**:
- [ ] `@context`: "https://schema.org"
- [ ] `@type`: "LocalBusiness"
- [ ] `name`: Country-specific name
- [ ] `address`: PostalAddress object
  - [ ] `streetAddress`
  - [ ] `addressLocality`
  - [ ] `addressRegion`
  - [ ] `postalCode`
  - [ ] `addressCountry`
- [ ] `telephone`
- [ ] `email`
- [ ] `url`

**Country-Specific Pages to Validate**:
| Country | URL | Status |
|---------|-----|--------|
| Vietnam | /vn/ | ⬜ |
| Germany | /de/ | ⬜ |
| India | /in/ | ⬜ |
| USA | /us/ | ⬜ |
| Japan | /jp/ | ⬜ |
| South Korea | /kr/ | ⬜ |
| Mexico | /mx/ | ⬜ |
| Turkey | /tr/ | ⬜ |
| Italy | /it/ | ⬜ |
| Poland | /pl/ | ⬜ |
| France | /fr/ | ⬜ |
| Malaysia | /my/ | ⬜ |
| Brazil | /br/ | ⬜ |

---

### 3. FAQPage Schema
**Purpose**: Enable FAQ rich snippets

**Locations**: Homepage + all localized pages

**Required Properties**:
- [ ] `@context`: "https://schema.org"
- [ ] `@type`: "FAQPage"
- [ ] `mainEntity`: Array of Question objects
  - [ ] Each Question has:
    - [ ] `@type`: "Question"
    - [ ] `name`: Question text
    - [ ] `acceptedAnswer`: Answer object
      - [ ] `@type`: "Answer"
      - [ ] `text`: Answer text

**Validation Checklist**:
- [ ] Minimum 2 questions per page
- [ ] Questions are relevant to the page content
- [ ] Answers are concise (recommended < 320 characters)
- [ ] No duplicate questions across pages

---

### 4. BreadcrumbList Schema
**Purpose**: Enable breadcrumb navigation in search results

**Locations**: All pages with hierarchical structure

**Required Properties**:
- [ ] `@context`: "https://schema.org"
- [ ] `@type`: "BreadcrumbList"
- [ ] `itemListElement`: Array of ListItem objects
  - [ ] Each ListItem has:
    - [ ] `@type`: "ListItem"
    - [ ] `position`: Number (1, 2, 3...)
    - [ ] `name`: Page name
    - [ ] `item`: Page URL

**Example Structure**:
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://sinofuse.elec-distributor.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Products",
      "item": "https://sinofuse.elec-distributor.com/products/"
    }
  ]
}
```

---

## Validation Tools

### Primary Tools

#### 1. Google Rich Results Test
**URL**: https://search.google.com/test/rich-results

**Usage**:
1. Enter page URL or paste code
2. Click "Test URL"
3. Review detected schema types
4. Check for errors and warnings

**What to Look For**:
- ✅ "Valid" status
- ✅ All intended schema types detected
- ❌ No critical errors
- ⚠️ Address any warnings

#### 2. Schema.org Validator
**URL**: https://validator.schema.org/

**Usage**:
1. Enter page URL or paste JSON-LD
2. Review validation results
3. Check for missing required properties

#### 3. Google Search Console - Rich Results Report
**Location**: GSC > Enhancements > Rich Results

**Monitors**:
- Valid rich results
- Invalid rich results
- Trends over time

---

## Validation Process

### Step 1: Validate Homepage
**URL**: `https://sinofuse.elec-distributor.com/`

**Check for**:
- [ ] Organization Schema present
- [ ] LocalBusiness Schema present (for Vietnam warehouse)
- [ ] FAQPage Schema present
- [ ] No errors in Rich Results Test

### Step 2: Validate Localized Pages
Test each of the 13 localized pages:

**For Each Page**:
1. Open Rich Results Test
2. Enter localized URL (e.g., `/vn/`)
3. Verify LocalBusiness Schema
4. Verify FAQPage Schema
5. Document any errors

### Step 3: Validate Product Pages
**Sample URLs to Test**:
- `/products/new-energy-vehicle/index.html`
- `/products/photovoltaic/PV312-Series.html`
- `/products/industrial/RS309-Mf-H-40A.html`

**Check for**:
- [ ] Product Schema (if implemented)
- [ ] BreadcrumbList Schema
- [ ] Organization Schema

### Step 4: Validate Solution Pages
**Sample URLs to Test**:
- `/solutions/automotive/index.html`
- `/solutions/energy-storage/index.html`
- `/solutions/photovoltaic/index.html`

---

## Common Issues and Solutions

### Issue 1: "Missing field" Error
**Example**: "Missing field 'addressLocality'"

**Solution**:
1. Check LocalBusiness Schema
2. Ensure all required address fields are present
3. Verify no empty values

### Issue 2: "Invalid value type" Error
**Example**: "Expected type Text but got Number"

**Solution**:
1. Check data types in Schema
2. Ensure telephone numbers are strings: `"+1-555-010-8888"`
3. Ensure URLs are valid and absolute

### Issue 3: "Duplicate property" Warning
**Example**: Multiple `name` properties

**Solution**:
1. Review JSON-LD structure
2. Ensure no duplicate keys at same level
3. Consolidate duplicate information

### Issue 4: Schema Not Detected
**Possible Causes**:
- Script tag outside `<head>`
- Invalid JSON syntax
- JavaScript errors preventing rendering

**Solution**:
1. Move `<script type="application/ld+json">` to `<head>`
2. Validate JSON syntax with [JSONLint](https://jsonlint.com/)
3. Check browser console for JS errors

---

## Testing Checklist by Page Type

### Homepage (index.html)
- [ ] Organization Schema
- [ ] LocalBusiness Schema (Vietnam)
- [ ] FAQPage Schema (minimum 3 Q&A)
- [ ] All required properties present
- [ ] Rich Results Test: Valid

### Localized Pages (13 countries)
For each country page:
- [ ] LocalBusiness Schema with correct address
- [ ] Organization Schema
- [ ] FAQPage Schema (country-specific questions)
- [ ] hreflang tags present
- [ ] Rich Results Test: Valid

### Product Category Pages
- [ ] BreadcrumbList Schema
- [ ] Organization Schema
- [ ] Product Schema (if applicable)
- [ ] Rich Results Test: Valid

### Product Detail Pages
- [ ] Product Schema
- [ ] BreadcrumbList Schema
- [ ] Organization Schema
- [ ] Rich Results Test: Valid

### Solution Pages
- [ ] BreadcrumbList Schema
- [ ] Organization Schema
- [ ] Article Schema (if blog content)
- [ ] Rich Results Test: Valid

### Contact Page
- [ ] Organization Schema
- [ ] ContactPoint information
- [ ] LocalBusiness Schema
- [ ] Rich Results Test: Valid

---

## Automated Testing

### Using Google's API
```bash
# Test URL with Rich Results API
curl "https://search.google.com/test/rich-results?url=https://sinofuse.elec-distributor.com/"
```

### Using Schema Validator CLI
```bash
# Install schema validator
npm install -g schema-validator

# Validate page
schema-validator https://sinofuse.elec-distributor.com/
```

---

## Monitoring Schedule

### Weekly
- [ ] Check GSC Rich Results report for new errors
- [ ] Validate any newly published pages
- [ ] Monitor for Google algorithm updates affecting rich snippets

### Monthly
- [ ] Full validation of all 13 localized pages
- [ ] Review rich snippet impressions in GSC
- [ ] Update FAQ content based on new customer questions

### Quarterly
- [ ] Comprehensive schema audit
- [ ] Review and update LocalBusiness information
- [ ] Test new schema types (if applicable)
- [ ] Document performance impact of rich snippets

---

## Documentation

### Schema Implementation Log
| Date | Page | Schema Type | Changes | Validated By |
|------|------|-------------|---------|--------------|
| 2026-04-08 | Homepage | Organization | Initial setup | ⬜ |
| 2026-04-08 | /vn/ | LocalBusiness | Vietnam location | ⬜ |
| 2026-04-08 | /de/ | LocalBusiness | Germany location | ⬜ |
| ... | ... | ... | ... | ... |

### Error Log
| Date | Page | Error | Resolution | Status |
|------|------|-------|------------|--------|
| | | | | |

---

## Resources

- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)
- [Google Search Gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery)
- [Schema.org Documentation](https://schema.org/docs/schemas.html)

---

*Last Updated: 2026-04-08*
*Next Review: 2026-05-08*
