
import os
import re

r = re.compile("(?:([^-]+)\n)+-+\n+((?:[^:]+\n)+)")

def get_abstract(path):
    with open(path, encoding='utf-8') as readme_file:2
        content = readme_file.read()
        groups = r.match(content).groups()
        return map(lambda s: s.strip(), groups)

def gen_abstract_dict():
    generated_dict = {}
    for root, _, files in os.walk(".", topdown=False):
        awesome_type = os.path.split(root)[0].strip("./\\")
        for file_name in files:
            if file_name == "README.md" and root != ".":
                path = os.path.join(root, file_name)
                name, abstract = get_abstract(path)
                if awesome_type not in generated_dict:
                    generated_dict[awesome_type] = ""
                generated_dict[awesome_type] += "### [{name}]({path}) \n\n {abstract} \n\n".format(name=name, abstract=abstract, path=path)
        
    return generated_dict

if __name__ == "__main__":
    import sys
    template = open('README.md.template', encoding='utf-8').read()
    out_file = open("README.md", "w", encoding='utf-8')
    abstract = gen_abstract_dict()
    out_file.write(template.format(**abstract))