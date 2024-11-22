# pdf2text

Dockerized service to extract text from PDF files, using [pypdf](https://github.com/py-pdf/pypdf).

## Options

| name               | required | possible values     | default  |
| ------------------ | -------- | ------------------- | -------- |
| `file`             | yes      | -                   | -        |
| `mode`             | no       | `layout` \| `plain` | `layout` |
| `space_vertically` | no       | true/false          | false    |
| `scale_weight`     | no       | float values        | 1.25     |

## Examples

Default Extraction Mode:

```bash
curl -X POST -F "file=@sample.pdf" http://localhost:5000/extract-text
```

Custom Parameters for Layout Preservation:

```bash
curl -X POST \
-F "file=@sample.pdf" \
-F "mode=plain" \
-F "space_vertically=true" \
-F "scale_weight=1.5" \
http://localhost:7357/extract-text
```
