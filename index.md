---
layout: default
title: Webarchiv
---

# Tohle NEbude peklo!

You can use the [editor on GitHub](https://github.com/kvasnicaj/kvasnicaj.github.io/edit/master/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

## lidi nemusí prožívat peklo...

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

_kurzíva_

[Link](url) and ![Image](src)
```
http://github.com - automatic!



[odkaz na wa](http://www.webarchiv.cz)

![frenchie](http://img1.goodhouse.ru/upload/img_get/dd/dd9f9c264826d36836617513bf23f97d_fitted_700x.jpg)



For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/kvasnicaj/kvasnicaj.github.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.


# 1. kapitola

* První řádek
  * První a půl tý
  * První a drůh tý
* Druhý řádek

   tady už není seznam



   | Tables        | Are           | Cool  |
   | ------------- |:-------------:| -----:|
   | col 3 is      | right-aligned | $1600 |
   | col 2 is      | centered      |   $12 |
   | zebra stripes | are neat      |    $1 |

   




### metadata
{% for repository in site.github.public_repositories %}
  * [{{ repository.name }}]({{ repository.html_url }})
{% endfor %}
