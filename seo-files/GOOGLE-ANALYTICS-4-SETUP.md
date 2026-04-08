# Google Analytics 4 Setup Guide
## Sinofuse Distributor Website

### Overview
This guide walks you through setting up Google Analytics 4 (GA4) for the Sinofuse distributor website to track user behavior, measure conversions, and analyze traffic from 13 target countries.

---

## Step 1: Create GA4 Property

### 1.1 Access Google Analytics
1. Go to [Google Analytics](https://analytics.google.com)
2. Sign in with your Google account
3. Click **Admin** (gear icon, bottom left)

### 1.2 Create New Property
1. In the **Property** column, click **Create Property**
2. Enter property name: `Sinofuse Distributor Website`
3. Select **Reporting time zone**: Choose your primary business timezone
4. Select **Currency**: USD (or your preferred currency)
5. Click **Next**

### 1.3 Provide Business Information
1. **Industry category**: Manufacturing / Electronics
2. **Business size**: Select appropriate size
3. **How do you intend to use Google Analytics**: 
   - [x] Measure customer engagement
   - [x] Generate leads
   - [x] Drive online sales
   - [x] Optimize site experience
4. Click **Create**

### 1.4 Accept Terms of Service
1. Select your country/region
2. Review and accept the Terms of Service
3. Click **I Accept**

---

## Step 2: Set Up Data Stream

### 2.1 Add Web Data Stream
1. In the **Property** column, click **Data Streams**
2. Click **Add stream** > **Web**
3. Enter website URL: `https://sinofuse.elec-distributor.com`
4. Enter stream name: `Sinofuse Website - Global`
5. Click **Create stream**

### 2.2 Get Measurement ID
After creating the stream, you'll see:
```
Measurement ID: G-XXXXXXXXXX
```
**Save this ID** - you'll need it for the tracking code.

### 2.3 Enhanced Measurement
Enable these enhanced measurement events:
- [x] Page views (automatic)
- [x] Scrolls
- [x] Outbound clicks
- [x] Site search
- [x] Video engagement
- [x] File downloads
- [x] Form interactions

---

## Step 3: Install GA4 Tracking Code

### 3.1 Global Site Tag (gtag.js)
Add this code to the `<head>` section of ALL pages, including localized pages:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-XXXXXXXXXX', {
    'send_page_view': true,
    'cookie_flags': 'SameSite=None;Secure'
  });
</script>
```

**Replace `G-XXXXXXXXXX` with your actual Measurement ID.**

### 3.2 Pages to Update
Add the tracking code to:
- [ ] [index.html](file:///c:/Users/ymlt/Desktop/sinofuse-distributor-site-master/index.html)
- [ ] [about.html](file:///c:/Users/ymlt/Desktop/sinofuse-distributor-site-master/about.html)
- [ ] [contact.html](file:///c:/Users/ymlt/Desktop/sinofuse-distributor-site-master/contact.html)
- [ ] All product pages
- [ ] All solution pages
- [ ] All 13 localized pages:
  - [ ] /vn/index.html
  - [ ] /de/index.html
  - [ ] /in/index.html
  - [ ] /us/index.html
  - [ ] /jp/index.html
  - [ ] /kr/index.html
  - [ ] /mx/index.html
  - [ ] /tr/index.html
  - [ ] /it/index.html
  - [ ] /pl/index.html
  - [ ] /fr/index.html
  - [ ] /my/index.html
  - [ ] /br/index.html

---

## Step 4: Configure Events

### 4.1 Automatically Collected Events
These events are tracked automatically:
- `page_view` - Page views
- `session_start` - Session starts
- `first_visit` - First-time visitors
- `user_engagement` - User engagement

### 4.2 Enhanced Measurement Events
Enable in Data Stream settings:
- `scroll` - Page scrolling (90% depth)
- `click` - Outbound link clicks
- `search` - Site search usage
- `video_start`, `video_complete` - Video engagement
- `file_download` - File downloads

### 4.3 Custom Events to Track

#### Contact Form Submission
```javascript
gtag('event', 'contact_form_submit', {
  'event_category': 'engagement',
  'event_label': 'contact_page',
  'country': 'US' // or detected country
});
```

#### Quote Request
```javascript
gtag('event', 'quote_request', {
  'event_category': 'lead_generation',
  'event_label': 'product_page',
  'product_category': 'EV Fuses'
});
```

#### Phone Call Click
```javascript
gtag('event', 'phone_call_click', {
  'event_category': 'contact',
  'event_label': 'phone_number',
  'country_code': '+1'
});
```

#### Email Click
```javascript
gtag('event', 'email_click', {
  'event_category': 'contact',
  'event_label': 'email_address'
});
```

#### Product View
```javascript
gtag('event', 'product_view', {
  'event_category': 'ecommerce',
  'event_label': product_name,
  'product_category': category,
  'country': detected_country
});
```

---

## Step 5: Set Up Conversions

### 5.1 Mark Events as Conversions
1. In GA4, go to **Admin** > **Events**
2. Toggle **Mark as conversion** for:
   - `contact_form_submit`
   - `quote_request`
   - `phone_call_click`
   - `email_click`

### 5.2 Create Conversion Events
1. Go to **Admin** > **Conversions**
2. Click **New conversion event**
3. Add custom conversion names:
   - `contact_lead`
   - `quote_lead`
   - `phone_lead`
   - `email_lead`

---

## Step 6: Configure Custom Dimensions

### 6.1 User Properties
Set up user properties for segmentation:

| Property Name | Description | Example Values |
|---------------|-------------|----------------|
| `user_country` | User's country | US, DE, JP, VN |
| `user_language` | Browser language | en, de, ja, vi |
| `user_type` | Customer type | new, returning |

### 6.2 Event Parameters
Track custom parameters with events:

```javascript
gtag('event', 'page_view', {
  'page_location': window.location.href,
  'page_title': document.title,
  'country_detected': 'US',
  'language_detected': 'en'
});
```

---

## Step 7: Set Up Audiences

### 7.1 Create Audiences

#### High-Intent Visitors
- Condition: Session duration > 2 minutes AND Pages per session > 3
- Description: Users showing strong interest

#### Quote Requesters
- Condition: Event `quote_request` exists
- Description: Users who requested quotes

#### Contact Page Visitors
- Condition: Page view contains "/contact"
- Description: Users who visited contact page

#### By Country
Create separate audiences for each target country:
- United States Visitors
- Germany Visitors
- Japan Visitors
- Vietnam Visitors
- (etc. for all 13 countries)

### 7.2 Audience Configuration
1. Go to **Audiences** (left sidebar)
2. Click **New audience**
3. Select **Create a custom audience**
4. Define conditions
5. Click **Save**

---

## Step 8: Configure Reports

### 8.1 Standard Reports to Monitor

#### Acquisition Reports
- **Traffic acquisition**: Source/medium performance
- **User acquisition**: New user sources
- **Sessions**: Session metrics by channel

#### Engagement Reports
- **Events**: Event counts and trends
- **Conversions**: Conversion rates by event
- **Pages and screens**: Top performing pages

#### Monetization Reports
- **Ecommerce purchases**: (if applicable)
- **In-app purchases**: (if applicable)

#### Retention Reports
- **Retention**: User return rates
- **User engagement**: Engagement over time

### 8.2 Create Custom Reports

#### Country Performance Report
Dimensions:
- Country
- Session source

Metrics:
- Sessions
- Users
- Engagement rate
- Conversions

#### Localized Page Performance
Dimensions:
- Page path
- Country

Metrics:
- Page views
- Average engagement time
- Bounce rate
- Conversions

---

## Step 9: Set Up Google Search Console Integration

### 9.1 Link GSC to GA4
1. In GA4, go to **Admin** > **Product Links**
2. Click **Search Console Links**
3. Click **Link**
4. Select your GSC property
5. Select your GA4 data stream
6. Click **Next** > **Submit**

### 9.2 View GSC Data in GA4
After linking, access GSC data in:
- **Reports** > **Acquisition** > **Search Console**
- Queries report
- Landing pages report
- Countries report
- Devices report

---

## Step 10: Configure Data Retention and Privacy

### 10.1 Data Retention Settings
1. Go to **Admin** > **Data Settings** > **Data Retention**
2. Set **Event data retention**: 14 months (recommended)
3. Set **Reset user data on new activity**: On

### 10.2 Privacy Settings
1. Go to **Admin** > **Data Settings** > **Privacy Settings**
2. Configure:
   - [x] Google signals (if applicable)
   - [x] Granular location and device data collection
   - [x] Allow ads personalization

### 10.3 GDPR Compliance
For German and EU visitors:
- Implement consent mode
- Respect user privacy choices
- Document data processing activities

---

## Step 11: Test Implementation

### 11.1 Real-Time Reports
1. Go to **Reports** > **Realtime**
2. Open your website in another tab
3. Verify your visit appears in real-time

### 11.2 DebugView
1. Install [Google Analytics Debugger](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna) Chrome extension
2. Open your website
3. Check browser console for GA4 events
4. Verify events fire correctly

### 11.3 Event Testing
Trigger each custom event and verify in:
- **Admin** > **Events** (24-48 hour delay)
- **Realtime** > **Event count by event name** (immediate)

---

## Step 12: Regular Monitoring

### Daily Checks
- [ ] Realtime traffic levels
- [ ] Any traffic anomalies
- [ ] Conversion events firing

### Weekly Reviews
- [ ] Traffic acquisition sources
- [ ] Top performing pages
- [ ] Event counts and trends
- [ ] Conversion rates

### Monthly Analysis
- [ ] Country performance comparison
- [ ] Localized page performance
- [ ] User engagement metrics
- [ ] Goal completion rates
- [ ] Audience growth

### Quarterly Reporting
- [ ] Comprehensive traffic analysis
- [ ] Conversion funnel analysis
- [ ] ROI by marketing channel
- [ ] User behavior insights
- [ ] Strategic recommendations

---

## Quick Reference

### Important IDs
| Item | Value |
|------|-------|
| Measurement ID | G-XXXXXXXXXX |
| Property ID | XXXXXXXXX |
| Stream ID | XXXXXXXXX |

### Key URLs
| Resource | URL |
|----------|-----|
| GA4 Dashboard | https://analytics.google.com |
| Realtime Reports | https://analytics.google.com/analytics/web/#/realtime |
| DebugView | https://analytics.google.com/analytics/web/#/debugview |

### Event Reference
| Event Name | Trigger | Category |
|------------|---------|----------|
| page_view | Automatic | Engagement |
| contact_form_submit | Form submission | Lead Generation |
| quote_request | Quote button click | Lead Generation |
| phone_call_click | Phone link click | Contact |
| email_click | Email link click | Contact |

---

## Support Resources

- [GA4 Help Center](https://support.google.com/analytics/topic/9143232)
- [GA4 Developer Documentation](https://developers.google.com/analytics/devguides/collection/ga4)
- [Google Analytics YouTube Channel](https://www.youtube.com/channel/UCJ5UyIAa5nEGksjcdp43Ixw)

---

*Last Updated: 2026-04-08*
*Next Review: 2026-05-08*
