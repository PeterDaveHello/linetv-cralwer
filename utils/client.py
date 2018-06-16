from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import queue
import shutil
import urllib.request
import concurrent.futures

class Pattern:
    def __init__(self):
        self.url = '{root}/{prefix}{index}.{ext}?{query}'
        self.file = '{path}/{part}-{index}.{ext}'

class Client:
    def __init__(self):
        self.tasks = []
        self.pattern = Pattern()

    def add(self, **kwargs):
        # rename
        path = kwargs['path']

        for i in range(0, len(kwargs['list'])):
            # rename
            url = kwargs['list'][i]

            # url related
            root = url[:url.rfind('/')]
            query = url[url.find('?')+1:]
            prefix = url[url.rfind('/')+1:url.rfind('-')+1]
            index = url[url.rfind('-')+1:url.rfind('.')]
            ext = url[url.rfind('.')+1:url.find('?')]

            for j in range(0, 300):
                self.tasks.append({
                    'file': self.pattern.file.format(
                        path=path,
                        part=i,
                        index=str(j).rjust(len(index), '0'),
                        ext=ext
                    ),
                    'url': self.pattern.url.format(
                        root=root,
                        prefix=prefix,
                        index=str(j).rjust(len(index), '0'),
                        ext=ext,
                        query=query
                    )
                })

    def get(self, task):
        with urllib.request.urlopen(task['url']) as response, open(task['file'], 'wb') as outfile:
            shutil.copyfileobj(response, outfile)

    def run(self, **kwargs):
        with concurrent.futures.ThreadPoolExecutor(max_workers=kwargs['threads']) as executor:
            futures = executor.map(self.get, self.tasks)

client = Client()
