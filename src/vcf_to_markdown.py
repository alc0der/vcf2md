import os
import click
import vobject
from typing import Dict, Any

def parse_vcf(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as f:
        vcard = vobject.readOne(f)

    data = {
        'nickname': vcard.nickname.value if hasattr(vcard, 'nickname') else None,
        'first_name': vcard.n.value.given,
        'last_name': vcard.n.value.family,
        'full_name': vcard.fn.value,
        'email': vcard.email.value if hasattr(vcard, 'email') else None,
        'phone': vcard.tel.value if hasattr(vcard, 'tel') else None,
    }
    return data

def generate_markdown(data: Dict[str, Any], use_name_in_h1: bool) -> str:
    name = data['nickname'] or f"{data['first_name']} {data['last_name']}"

    markdown = f"# {name}\n\n" if use_name_in_h1 else ""

    markdown += "## Info\n\n"
    markdown += f"Full Name\n: {data['full_name']}\n"
    if data['nickname']:
        markdown += f"Nickname\n: {data['nickname']}\n"

    markdown += "\n## Channels\n\n"
    if data['email']:
        markdown += f"Email\n: {data['email']}\n"
    if data['phone']:
        markdown += f"Phone\n: {data['phone']}\n"

    return markdown

def get_output_filename(data: Dict[str, Any]) -> str:
    name = data['nickname'] or f"{data['first_name']} {data['last_name']}"
    return f"{name}.md"

@click.command()
@click.option('--input', '-i', required=True, help='Directory where VCF files are located')
@click.option('--output', '-o', required=True, help='Directory where Markdown files will be outputted')
@click.option('--use-name-in-h1', is_flag=True, default=False, help='Use the name as an H1 header in the Markdown file')
def main(input: str, output: str, use_name_in_h1: bool):
    if not os.path.exists(output):
        os.makedirs(output)

    for filename in os.listdir(input):
        if filename.endswith('.vcf'):
            vcf_path = os.path.join(input, filename)
            data = parse_vcf(vcf_path)
            markdown_content = generate_markdown(data, use_name_in_h1)
            output_filename = get_output_filename(data)
            output_path = os.path.join(output, output_filename)

            with open(output_path, 'w') as f:
                f.write(markdown_content)

            click.echo(f"Converted {filename} to {output_filename}")

if __name__ == '__main__':
    main()
