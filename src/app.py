import jinja2
import sys
from contexts import CONTEXTS

def render_template(input_name, output_name, contexts):
    with open(input_name, 'r') as file:
        html_page = file.read()

    output = jinja2.Environment().from_string(html_page).render(contexts)
    with open(output_name,'wb') as file:
        file.write(output.encode('utf-8'))

def render_from_argv():
    if len(sys.argv) != 4:
        print('error in the arguments: input_name output_name contexts')
    else:
        render_template(sys.argv[1], sys.argv[2], CONTEXTS[sys.argv[3]])

if __name__ == '__main__':
    render_from_argv()