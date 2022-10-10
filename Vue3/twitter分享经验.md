# Twitter 分享开发心得

## 使用 `https://twitter.com/intent/tweet` 唤起推特的分享功能

```javascript
https://twitter.com/intent/tweet?text=xxx&url=xxx&hashtags=xxx

text:       推文文本，长度不超过280个字符
url:        嵌套的推文超链接，可以引导进入某个页面
hashtags:   #标签，可以做一个主题的强调

```

## 推文超链接的爬虫内容

使用`<meta>` 标签来进行推特爬虫的数据加载

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Euler Esports" />
<meta name="twitter:description" content="This is description." />
<meta name="twitter:image" content="xxxurl" />
```

---

# 遇到其中的一些坑

> ## 第一个坑
>
> > 推文的超链接进行了爬虫拿取数据，但是，如果这个链接是带着端口以及数字 IP 的链接，爬虫是抓取不到数据的

> > 超链接的 Meta 属性如果是动态生成的，爬虫也是拿不到数据的，只能通过 js 动态生成一个 html 去让爬虫扫描
