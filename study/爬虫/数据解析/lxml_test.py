"""

xpath语法
nodename	选取此节点的所有子节点。
/	从根节点选取。  即绝对路径
//	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。 即相对路径
.	选取当前节点。
..	选取当前节点的父节点。
@	选取属性。
"""

from lxml import etree

text = """
<div class="wgt-searchbar wgt-searchbar-new wgt-searchbar-main cmn-clearfix wgt-searchbar-large">
<div class="logo-container">
<a class="logo cmn-inline-block" title="到百科首页" href="/">
<span class="cmn-baike-logo">
<em class="cmn-icon cmn-icons cmn-icons_logo-bai"></em>
</span>
</a>
</div>
</div>
"""
# 创建 element对象
html = etree.HTML(text) #能够自动补全html缺失的标签
print(html)
print(html.xpath("//a/@title"))
