import xml.etree.ElementTree as et

with open('/usr/share/X11/xkb/rules/evdev.xml') as f:
    t = et.parse(f)

    root = t.getroot()
    layouts = root.find('layoutList')

    ns_hits = layouts.findall(".//description[.='Notosic']")
    if len(ns_hits) > 0:
        print("Notosic already in!")
        exit()
    
    # append our own keyboard layout
    layout = et.SubElement(layouts, 'layout')
    kb_config = et.SubElement(layout, 'configItem')
    # set the keyboard name
    kb_name = et.SubElement(kb_config, 'name')
    kb_name.text = 'ns'
    # set the keyboard descriptions
    kb_short = et.SubElement(kb_config, 'shortDescription')
    kb_short.text = 'ns'
    kb_desc = et.SubElement(kb_config, 'description')
    kb_desc.text = 'Notosic'

    lang_list = et.SubElement(kb_config, 'languageList')
    lang = et.SubElement(lang_list, 'iso639Id')
    lang.text = 'gre' # ISO-639-2/B

    variant_list = et.SubElement(layout, 'variantList')
    variant_dicts = [{ 'name': 'simple', 'desc': 'Notosic (simple)' }]
    
    if len(variant_dicts) > 0:
        for v in variant_dicts:
            var = et.SubElement(variant_list, 'variant')
            var_conf = et.SubElement(var, 'configItem')
            et.SubElement(var_conf, 'name').text = v['name']
            et.SubElement(var_conf, 'description').text = v['desc']

    t.write('evdev.xml')
