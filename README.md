# VCF to Markdown

<version>0.1.0</version>

A CLI command to convert VCF files to Markdown (Extended Markdown). The CLI commands names the markdown files based on the nickname and fallback to first name last name if the nickname is not assigned. The tool uses an `## Info` section for things like name and a `## Channels` section for things like phone number. The data is placed in a Definition Lists.

## Arguments

--input -i: A directory where VCF files are located
--output -o: A directory where Markdown files will be outputted

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Poetry (for dependency management)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/vcf_to_markdown.git
   cd vcf_to_markdown
   ```

2. Install the project dependencies using Poetry:
   ```
   poetry install
   ```

### Usage

To convert VCF files to Markdown, use the following command:

```
poetry run vcf_to_markdown --input /path/to/vcf/files --output /path/to/output/directory
```

Or, if you've activated the Poetry shell:

```
vcf_to_markdown --input /path/to/vcf/files --output /path/to/output/directory
```

This will process all .vcf files in the input directory and generate corresponding Markdown files in the output directory.

### Example

If you have a VCF file named `john_doe.vcf` in the directory `/home/user/contacts`, and you want to save the Markdown files in `/home/user/markdown_contacts`, you would run:

```
vcf_to_markdown --input /home/user/contacts --output /home/user/markdown_contacts
```

This will generate a Markdown file (e.g., `John_Doe.md` or `JohnnyD.md` if a nickname is present) in the `/home/user/markdown_contacts` directory.
```
