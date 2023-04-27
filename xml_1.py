'''<studentsList>
    <student>
        <firstName>Blaise</firstName>
        <lastName>Pascal</lastName>
        <certificate>True</certificate>
        <scores>
            <modele1>70</modele1>
            <modele2>80</modele2>
            <modele3>90</modele3>
        </scores>
    </student>
    <student>
        <firstName>Francis</firstName>
        <lastName>Bacon</lastName>
        <certificate>True</certificate>
        <scores>
            <modele1>80</modele1>
            <modele2>80</modele2>
            <modele3>80</modele3>
        </scores>
    </student>
</studentsList>'''

#  копируем xml файл(сначала его считываем, а затем записываем в другой файл
from xml.etree import ElementTree

tree = ElementTree.parse('example.xml')
root = tree.getroot()
tree.write('example_copy.xml')
