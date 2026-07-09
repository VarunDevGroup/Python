import xml.etree.ElementTree as ET
data='''<person><Name>Varun Sharma</Name><Age>44</Age><Phone type='work'>+919831410307</Phone>
    <classes>
    <class>Class 1</class>
    <class>Class 2</class>
    <class>Class 3</class>
    <class>Class 4</class>
    <class>Class 5</class>
    </classes></person>'''

tree= ET.fromstring(data)
print(tree.find('Name').text)
print(tree.find('Phone').get('type'))

classes= tree.findall('classes/class')
print(len(classes))
for cls in classes:
    print(cls.text)
