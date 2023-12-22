import xml.etree.ElementTree as et

# get inputs
layout_alias = input("Two letter name for your keyboard layout: ")
layout_name = input("Name of your layout (usually language name in English): ")
lang_code = input("The ISO-639-2/B language code for your layout (cf. https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)\n")

# prompt for adding variants
add_variants = input("Would you like to add more variants? [N/y]: ")
if (add_variants.upper() = "N") || add_variants == "" :
    print("Not adding variants.")
elif add_variants = "y":
    print("Adding variants ...")
    c = True
    variant_dicts = []

    while c:
        # add variant to the list
        n = input("Keyboard variant alias? ('simple', 'dvorak', etc.): ")
        desc = layout_name + ' ' + n
        variant_dicts.append({ 'name': n, 'desc': desc })

        # prompt whether to continue adding variants
        more_variant = input("Add another variant? [N/y]: ")
        if more_variant.upper() != "Y":
            print("Finished adding variants.")
            c = False

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
    kb_name.text = layout_alias
    # set the keyboard descriptions
    kb_short = et.SubElement(kb_config, 'shortDescription')
    kb_short.text = layout_alias
    kb_desc = et.SubElement(kb_config, 'description')
    kb_desc.text = layout_name

    lang_list = et.SubElement(kb_config, 'languageList')
    lang = et.SubElement(lang_list, 'iso639Id')
    lang.text = 'gre' # ISO-639-2/B

    variant_list = et.SubElement(layout, 'variantList')
    
    if len(variant_dicts) > 0:
        for v in variant_dicts:
            var = et.SubElement(variant_list, 'variant')
            var_conf = et.SubElement(var, 'configItem')
            et.SubElement(var_conf, 'name').text = v['name']
            et.SubElement(var_conf, 'description').text = v['desc']

    t.write('evdev.xml')
