from lxml import etree

tree = etree.parse("./src/web_page.html")
# print(etree.tostring(tree))

title_elem = tree.find("head/title")
print(title_elem.text)

hello_elem = tree.find("body/p")
print(hello_elem.text)

list_items = tree.findall("body/ul/li")
for li in list_items:
    a = li.find("a")
    if a is not None:
        print(F"{li.text.strip()} {a.text}")
    else:
        print(li.text)