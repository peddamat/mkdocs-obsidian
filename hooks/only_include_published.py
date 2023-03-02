import os, logging, typing, frontmatter
from typing import Optional

import mkdocs.plugins
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files
from mkdocs.config.defaults import MkDocsConfig

log = logging.getLogger('mkdocs')

def is_page_published(meta: typing.Dict) -> bool:
    if 'publish' in meta:
        return meta['publish'] == True

def on_files(files: Files, *, config: MkDocsConfig) -> Optional[Files]:
    base_docs_url = config["docs_dir"]

    for file in files.documentation_pages():
        abs_path = os.path.join(base_docs_url, file.src_uri)
        with open(abs_path, 'r') as raw_file:
            try:
                metadata = frontmatter.load(raw_file).metadata
                if is_page_published(metadata):
                    log.info(f"Adding published document {file.src_uri}")
                else:
                    files.remove(file)
            except:
                log.error(f"IncludePublishedFilesPlugin found malformed frontmatter in {file.src_uri} (skipping)!")

    return files

def on_post_page(output: str, *, page: Page, config: MkDocsConfig) -> Optional[str]:
    if not is_page_published(page.meta):
        return ''

    return output