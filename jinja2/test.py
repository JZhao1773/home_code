from jinja2 import Environment, FileSystemLoader
import pandas as pd

def get_jinja2_templ(templ, dir='jinja2_templates'):
        loader = FileSystemLoader(dir)
        env = Environment(loader=loader)
        template = env.get_template(env.get_template(templ))
        return template

def get_data_from_excel(file='data.xlsx'):
        df = pd.read_excel(file)
        data = df.to_dict(orient='records')
        return data


if __name__ == '__main__':
        template = get_jinja2_templ(templ='jinja2_demo.j2')
        data = get_data_from_excel()
        result = template.render(data=data)
        print(data)
