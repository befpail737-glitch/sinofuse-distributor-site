# Schema Markup 验证指南

**项目**: Sinofuse Distributor GEO SEO  
**日期**: 2026-04-08

---

## 快速验证步骤

### 1. 使用 Google Rich Results Test

1. 访问: https://search.google.com/test/rich-results
2. 输入页面 URL: `https://sinofuse.elec-distributor.com/`
3. 点击 "Test URL"
4. 查看验证结果

### 2. 预期验证结果

| Schema 类型 | 状态 | 检测到的元素 |
|-------------|------|--------------|
| Organization | ✅ | 名称、URL、Logo、描述 |
| LocalBusiness | ✅ | 地址、电话、营业时间 |
| FAQPage | ✅ | 4 个问题及答案 |
| Product | ✅ | 4 个产品类别 |
| BreadcrumbList | ✅ | 面包屑导航 |

---

## Schema 代码片段

### Organization Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "LiTong - Sinofuse Distributor",
  "url": "https://sinofuse.elec-distributor.com/",
  "logo": "https://sinofuse.elec-distributor.com/images/logo.png",
  "description": "Official Sinofuse authorized distributor...",
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "sales",
    "availableLanguage": ["English", "German", "Vietnamese"]
  }
}
```

**验证要点**:
- [ ] name 字段不为空
- [ ] url 格式正确
- [ ] logo URL 可访问

### LocalBusiness Schema

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "LiTong - Sinofuse Distributor",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Industrial Zone",
    "addressLocality": "Ho Chi Minh City",
    "addressCountry": "VN"
  },
  "telephone": "+84-28-XXXX-XXXX"
}
```

**验证要点**:
- [ ] address 完整
- [ ] telephone 格式正确
- [ ] geo 坐标准确

### FAQPage Schema

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Are you an authorized Sinofuse distributor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, LiTong is an official authorized..."
      }
    }
  ]
}
```

**验证要点**:
- [ ] 至少 2 个问题
- [ ] 每个问题都有答案
- [ ] 文本长度适中

---

## 常见验证错误

### 错误 1: "Missing field 'name'"

**原因**: Organization Schema 缺少 name 字段
**修复**: 添加 name 字段
```json
"name": "LiTong - Sinofuse Distributor"
```

### 错误 2: "Invalid URL"

**原因**: URL 格式不正确或不可访问
**修复**: 检查 URL 格式
```json
"url": "https://sinofuse.elec-distributor.com/"
```

### 错误 3: "Missing field 'address'"

**原因**: LocalBusiness 缺少地址
**修复**: 添加完整地址
```json
"address": {
  "@type": "PostalAddress",
  "addressLocality": "Ho Chi Minh City",
  "addressCountry": "VN"
}
```

---

## 验证清单

### 部署前验证

- [ ] JSON 格式有效 (使用 JSON 验证器)
- [ ] 所有必需字段已填写
- [ ] URL 可访问
- [ ] 图片 URL 有效

### 部署后验证

- [ ] Rich Results Test 通过
- [ ] 无错误或警告
- [ ] 所有 Schema 类型被识别
- [ ] 预览显示正确

---

## 高级验证

### 使用 Google Search Console

1. 访问: https://search.google.com/search-console
2. 选择网站属性
3. 导航到 "Enhancements"
4. 查看 Schema 报告

### 使用 Schema.org 验证器

1. 访问: https://validator.schema.org/
2. 输入页面 URL 或粘贴代码
3. 查看详细验证结果

---

## 预期 SERP 功能

验证通过后，页面可能获得以下 SERP 功能：

| 功能 | 描述 | 触发 Schema |
|------|------|-------------|
| 知识面板 | 品牌信息展示 | Organization |
| 本地包 | 地图和地址显示 | LocalBusiness |
| FAQ 折叠 | 问题展开显示 | FAQPage |
| 面包屑 | 导航路径显示 | BreadcrumbList |
| 产品轮播 | 产品图片展示 | Product |
