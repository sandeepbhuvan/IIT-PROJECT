from jinja2 import Template

def main():
    file = open("login.j2")
    template = Template(file.read())
    file.close()
    rendered_template = template.render()
    output_file = open("output.html", "w")
    output_file.write(rendered_template)
    output_file.close()

if __name__ == "__main__":
    main()
