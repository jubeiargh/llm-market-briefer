import markdown


def markdown_to_html(markdown_text: str, title: str = "Market Briefing") -> str:
    """
    Convert markdown text into a styled HTML page.
    """
    body_html = markdown.markdown(
        markdown_text,
        extensions=["extra", "smarty"],  # optional: smart quotes, tables, etc.
        output_format="html5",
    )

    # Wrap in a basic styled HTML template
    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #f9f9f9;
                padding: 2rem;
                max-width: 800px;
                margin: auto;
                color: #333;
                line-height: 1.6;
            }}
            h1, h2, h3 {{
                color: #0b5cad;
            }}
            ul {{
                padding-left: 1.5rem;
            }}
            blockquote {{
                border-left: 4px solid #ccc;
                padding-left: 1rem;
                color: #666;
                font-style: italic;
            }}
            code {{
                background: #eee;
                padding: 0.2rem 0.4rem;
                border-radius: 3px;
                font-family: monospace;
            }}
            pre code {{
                display: block;
                padding: 1rem;
                background: #272822;
                color: #f8f8f2;
                overflow-x: auto;
            }}
        </style>
    </head>
    <body>
        {body_html}
    </body>
    </html>
    """
    return html
